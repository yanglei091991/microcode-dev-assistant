#ifndef UCP_SOCKET_H
#define UCP_SOCKET_H

#include <errno.h>
#include <unistd.h>
#include "addresswidget.h"

#define	CL_OPEN "open"
#define CS_OPEN "/tmp/opend.socket"
#define BUFSIZE 2048

int csopen(char *);
int cli_conn(const char *name);
int recv_fd(int, struct ProjectData *);

#endif // UCP_SOCKET_H
