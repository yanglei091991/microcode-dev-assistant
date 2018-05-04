#include "ucp_socket.h"
#include <errno.h>
#include <stdarg.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <sys/uio.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stddef.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include "QByteArray"
#include "QDebug"
#include <pwd.h>
#include <unistd.h>

#define MAXLINE 8192
#define	CLI_PATH	"/var/tmp/"
#define	CLI_PERM	S_IRWXU			/* rwx for user only */

static void	err_doit(int, int, const char *, va_list);

/*
 * Nonfatal error related to a system call.
 * Print a message and return.
 */
void
err_ret(const char *fmt, ...)
{
    va_list		ap;

    va_start(ap, fmt);
    err_doit(1, errno, fmt, ap);
    va_end(ap);
}

/*
 * Fatal error related to a system call.
 * Print a message and terminate.
 */
void
err_sys(const char *fmt, ...)
{
    va_list		ap;

    va_start(ap, fmt);
    err_doit(1, errno, fmt, ap);
    va_end(ap);
    exit(1);
}

/*
 * Nonfatal error unrelated to a system call.
 * Error code passed as explict parameter.
 * Print a message and return.
 */
void
err_cont(int error, const char *fmt, ...)
{
    va_list		ap;

    va_start(ap, fmt);
    err_doit(1, error, fmt, ap);
    va_end(ap);
}

/*
 * Fatal error unrelated to a system call.
 * Error code passed as explict parameter.
 * Print a message and terminate.
 */
void
err_exit(int error, const char *fmt, ...)
{
    va_list		ap;

    va_start(ap, fmt);
    err_doit(1, error, fmt, ap);
    va_end(ap);
    exit(1);
}

/*
 * Fatal error related to a system call.
 * Print a message, dump core, and terminate.
 */
void
err_dump(const char *fmt, ...)
{
    va_list		ap;

    va_start(ap, fmt);
    err_doit(1, errno, fmt, ap);
    va_end(ap);
    abort();		/* dump core and terminate */
    exit(1);		/* shouldn't get here */
}

/*
 * Nonfatal error unrelated to a system call.
 * Print a message and return.
 */
void
err_msg(const char *fmt, ...)
{
    va_list		ap;

    va_start(ap, fmt);
    err_doit(0, 0, fmt, ap);
    va_end(ap);
}

/*
 * Fatal error unrelated to a system call.
 * Print a message and terminate.
 */
void
err_quit(const char *fmt, ...)
{
    va_list		ap;

    va_start(ap, fmt);
    err_doit(0, 0, fmt, ap);
    va_end(ap);
    exit(1);
}

/*
 * Print a message and return to caller.
 * Caller specifies "errnoflag".
 */
static void
err_doit(int errnoflag, int error, const char *fmt, va_list ap)
{
    char	buf[MAXLINE];

    vsnprintf(buf, MAXLINE-1, fmt, ap);
    if (errnoflag)
        snprintf(buf+strlen(buf), MAXLINE-strlen(buf)-1, ": %s",
          strerror(error));
    strcat(buf, "\n");
    fflush(stdout);		/* in case stdout and stderr are the same */
    fputs(buf, stderr);
    fflush(NULL);		/* flushes all stdio output streams */
}

/*
 *
 *           cli_conn
 *
 *
 *
 * Create a client endpoint and connect to a server.
 * Returns fd if all OK, <0 on error.
 */
int
cli_conn(const char *name)
{
    int					fd, len, err, rval;
    struct sockaddr_un	un, sun;
    int					do_unlink = 0;

    if (strlen(name) >= sizeof(un.sun_path)) {
        errno = ENAMETOOLONG;
        return(-1);
    }

    //printf("&&&&&&&&&&&&&&%s\n",name);

    /* create a UNIX domain stream socket */
    if ((fd = socket(AF_UNIX, SOCK_STREAM, 0)) < 0)
        return(-1);

    /* fill socket address structure with our address */
    memset(&un, 0, sizeof(un));
    un.sun_family = AF_UNIX;
    sprintf(un.sun_path, "%s%05ld", CLI_PATH, (long)getpid());
    len = offsetof(struct sockaddr_un, sun_path) + strlen(un.sun_path);

    unlink(un.sun_path);		/* in case it already exists */
    if (bind(fd, (struct sockaddr *)&un, len) < 0) {
        rval = -2;
        goto errout;
    }
    if (chmod(un.sun_path, CLI_PERM) < 0) {
        rval = -3;
        do_unlink = 1;
        goto errout;
    }

    /* fill socket address structure with server's address */
    memset(&sun, 0, sizeof(sun));
    sun.sun_family = AF_UNIX;
    strcpy(sun.sun_path, name);
    len = offsetof(struct sockaddr_un, sun_path) + strlen(name);
    if (connect(fd, (struct sockaddr *)&sun, len) < 0) {
        printf("^^^^^^^connect refused^^^^^^^^^^^^%0d%s\n",fd,sun.sun_path);
        rval = -4;
        do_unlink = 1;
        goto errout;
    }
    //printf("###^^^^^^^^^^^^^^^^^^^%0d%s\n",fd,sun.sun_path);
    return(fd);

errout:
    err = errno;
    close(fd);
    if (do_unlink)
        unlink(un.sun_path);
    errno = err;
    return(rval);
}



/*
 *
 *       cs_open
 *
 *
 * Open the file by sending the "name" and "oflag" to the
 * connection server and reading a file descriptor back.
 */
int
csopen(char *name)
{
    int			n;
    char			buf[BUFSIZE];
    static int		csfd = -1;

    for(int i=0; i<200; i++){
        buf[i] = '\0';
    }
    strcpy(buf,name);
    //printf("@@@@@@@@@@@%s\n",buf);

    char csBuf[BUFSIZE];
    strcpy(csBuf,CS_OPEN);
    struct passwd *pwd;
    pwd = getpwuid(getuid());
    strcat(csBuf,pwd->pw_name);
    qDebug()<<"######connect####:"<<csBuf;
    //if (csfd < 0) {		/* open connection to conn server */
        if ((csfd = cli_conn(csBuf)) < 0) {
            printf("@@@@@@@@@@@%s%0d\n",buf,csfd);
            err_ret("cli_conn error");
            qDebug()<<"###########cli_conn error############";
            return(-1);
        }
    //}



    n = write(csfd, buf, sizeof(buf));
    if(n < 0){
        printf("server fd:%0d csopen write error!\n",csfd);
        qDebug()<<"server fd:"<<csfd<<"csopen write error!\n";
     }

    /* read back descriptor; returned errors handled by write() */
    return(csfd);
}



/*
 *
 *             recv_fd
 *
 * *
 * Receive a file descriptor from a server process.  Also, any data
 * received is passed to (*userfunc)(STDERR_FILENO, buf, nbytes).
 * We have a 2-byte protocol for receiving the fd from send_fd().
 */
int
recv_fd(int fd, struct ProjectData *pdata)
{
    char  buf[MAXLINE];
    char  cmd_buf[20];
    int nr;
    char *dm_buf;

    nr = read(fd,buf,8105);//sizeof(buf));
    QString s;
    s.prepend(buf);
    qDebug()<<"Run_data1:"<<s.mid(0,100);
    if(nr > 0){
        sscanf(buf,"%[^:]",cmd_buf);
        if(strcmp(cmd_buf,"pc")==0){
            sscanf(buf,"%*[^:]:%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d",&pdata->spu_pc,&pdata->mpu_pc[0]
                    ,&pdata->mpu_pc[1],&pdata->mpu_pc[2],&pdata->mpu_pc[3],&pdata->mpu_pc[4],&pdata->mpu_pc[5],&pdata->mpu_pc[6]
                    ,&pdata->mpu_pc[7],&pdata->mpu_pc[8],&pdata->mpu_pc[9],&pdata->mpu_pc[10],&pdata->mpu_pc[11],&pdata->mpu_pc[12]
                    ,&pdata->mpu_pc[13],&pdata->mpu_pc[14],&pdata->mpu_pc[15],&pdata->mpu_pc[16],&pdata->mpu_pc[17]);
            qDebug()<<"pc#####:"<<"spu"<<pdata->spu_pc<<"mpu"<<pdata->mpu_pc[0];
        }

        if(strcmp(cmd_buf,"break")==0){
            //s.prepend(buf);
            qDebug()<<"Break:"<<s;
        }


        if(strcmp(cmd_buf,"dm")==0){
             dm_buf = (char*)malloc(8100);
             sscanf(buf,"%*[^:]:%s",dm_buf);
             if(strcmp(dm_buf,"trans_null_dm_data")!=0){

                 char byte_tmp[8100];
                 memcpy(byte_tmp,buf+3,8100);
                 pdata->dm_trans += 1;
                 QByteArray byte;
                 byte = QByteArray((char*)byte_tmp,8100);
                 qDebug()<<"This is the size of byte trans:"<<byte.size();
                 pdata->memorydata.append(byte);
                 if(pdata->dm_trans == 195){
                     //qDebug()<<"dm_dataxxxxxyy:"<<pdata->memorydata;
                    pdata->dm_trans = 0;
                 }
             } else {
                 qDebug()<<"Does not trans any DM data@@@@@@@@@@@@@@@";
                 pdata->dm_trans = 0;
             }
             //qDebug()<<"dm_dataxxxxx:"<<pdata->memorydata;
             if(pdata->dm_trans >0)
                qDebug()<<"dm_data*****"<<pdata->dm_trans;
            free(dm_buf);
        }

        if(strcmp(cmd_buf,"reg")==0){
             //dm_buf = (char*)malloc(8100);
             //sscanf(buf,"%*[^:]:%s",dm_buf);
             QString reg_data = s.mid(4,8100);
             pdata->t_reg.append(reg_data.toLatin1());
             //qDebug()<<"reg_dataxxxx:"<<pdata->t_reg;
             qDebug()<<"reg_dataxxxx:"<<pdata->t_reg.length();
             //free(dm_buf);
        }


        if(strcmp(cmd_buf,"regread")==0){
            qDebug()<<"~~~~~~~~~~~~~~~~came into readreg";
            QString find_index = "pc:";
            int tmp = s.indexOf(find_index);
            if(tmp > 0){
                std::string str = s.toStdString();
                const char* pc_line = str.c_str();
                sscanf(pc_line,"%*[^:]:%*[^:]:%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d",&pdata->spu_pc,&pdata->mpu_pc[0]
                    ,&pdata->mpu_pc[1],&pdata->mpu_pc[2],&pdata->mpu_pc[3],&pdata->mpu_pc[4],&pdata->mpu_pc[5],&pdata->mpu_pc[6]
                    ,&pdata->mpu_pc[7],&pdata->mpu_pc[8],&pdata->mpu_pc[9],&pdata->mpu_pc[10],&pdata->mpu_pc[11],&pdata->mpu_pc[12]
                    ,&pdata->mpu_pc[13],&pdata->mpu_pc[14],&pdata->mpu_pc[15],&pdata->mpu_pc[16],&pdata->mpu_pc[17]);
                qDebug()<<"~~~~~~~~~~~~~~~~~~~~rerunpc#####:"<<"spu"<<pdata->spu_pc<<"mpu"<<pdata->mpu_pc[0];
            }
        }

    } else {
        close(fd);
        return(-1);
    }

    close(fd);
    return(0);
}
