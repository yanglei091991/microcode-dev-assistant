#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QTextEdit"
#include <QHBoxLayout>
#include <unistd.h>
#include <QDebug>

ProjectData projectdata;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent)
{

//    QTextEdit * textEdit=new QTextEdit;

//    setCorner(Qt::BottomRightCorner,dock3 );

    QRect rec = QApplication::desktop()->screenGeometry();
    int height = rec.height();
    int width = rec.width();
    scaleFactorX = double(width) /1920;
    scaleFactorY = double(height) /1080;
    qDebug()<<height;
    qDebug()<<width;
    qDebug()<<scaleFactorX;
    qDebug()<<scaleFactorY;

    setupData();

    createActions();
    createStatusBar();
    createDockWindows();
    createFloatDock();
//    dock4->resize(500,500);
//    setBaseSize(500,600);
//    this->resize(800,500);
    this->setGeometry(1050*scaleFactorX,150*scaleFactorY,850*scaleFactorX,800*scaleFactorY);
//    setMinimumHeight(500);
//    setSizePolicy(QSizePolicy::Ignored,QSizePolicy::Ignored);
    setWindowTitle(tr("Dock Widgets"));

}

MainWindow::~MainWindow()
{

}

void MainWindow::showRegData( ){
    QPair<QString, QString> pair;
    QList<QPair<QString, QString> > listofPairs;

    if(projectdata.mpu_pc[0] < 0)
        projectdata.mpu_pc[0] = 0;
    if(projectdata.spu_pc < 0)
        projectdata.spu_pc = 0;

    pair.first = "MPU_PC";
    pair.second = QString::number(projectdata.mpu_pc[0],16);
    listofPairs.append(pair);

    pair.first = "SPU_PC";
    pair.second = QString::number(projectdata.spu_pc,16);
    listofPairs.append(pair);

    TableModel *model0 = new TableModel(listofPairs);
    this->addressWidget->tableView[0]->setModel(model0);


    listofPairs.clear();
    /**************************ALU*******************************/
    char* showData = (char*) malloc(128+15+1);
    for(int i=0; i<6; i++){
        QString pair_name ="IALU.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        *(showData+128+15) = '\0';
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }

    for(int i=0; i<6; i++){
        QString pair_name ="IMAC.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8)
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*6];
                else if(j<15)
                    *(showData+j*9+k) = '_';
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }

    for(int i=0; i<6; i++){
        QString pair_name ="IFALU.T";
        pair_name.insert(7,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8)
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*6*2];
                else if(j<15)
                    *(showData+j*9+k) = '_';
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }

    for(int i=0; i<6; i++){
        QString pair_name ="IFMAC.T";
        pair_name.insert(7,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8)
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*6*3];
                else if(j<15)
                    *(showData+j*9+k) = '_';
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }


    TableModel *model1 = new TableModel(listofPairs);
    this->addressWidget->tableView[1]->setModel(model1);


    listofPairs.clear();
    /*******************************SHU********************************/
    for(int i=0; i<8; i++){
        QString pair_name ="SHU0.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*24];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    for(int i=0; i<8; i++){
        QString pair_name ="SHU1.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*32];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    for(int i=0; i<8; i++){
        QString pair_name ="SHU2.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*40];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    for(int i=0; i<3; i++){
        QString pair_name ="SHU.TB";
        pair_name.insert(3,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*48];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    TableModel *model2 = new TableModel(listofPairs);
    this->addressWidget->tableView[2]->setModel(model2);

    listofPairs.clear();
    /*******************************BIU********************************/
    for(int i=0; i<4; i++){
        QString pair_name ="BIU0.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*51];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    for(int i=0; i<4; i++){
        QString pair_name ="BIU1.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*55];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    for(int i=0; i<4; i++){
        QString pair_name ="BIU2.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*59];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    TableModel *model3 = new TableModel(listofPairs);
    this->addressWidget->tableView[3]->setModel(model3);

    listofPairs.clear();
    /*********************MFetch*****************************/
    char* showData1 = (char*) malloc(6);
    for(int i=0; i<16; i++){
        QString pair_name ="KI";
        pair_name.insert(2,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<6; j++){
            *(showData1+j) = projectdata.t_reg[i*6+j+128*63];
        }
        pair.second = QString(QLatin1String(showData1));
        listofPairs.append(pair);
    }
    TableModel *model4 = new TableModel(listofPairs);
    this->addressWidget->tableView[4]->setModel(model4);

    listofPairs.clear();
    /*********************MReg*****************************/
    for(int i=0; i<64; i++){
        QString pair_name ="MReg";
        pair_name.insert(4,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*63+16*6];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    TableModel *model5 = new TableModel(listofPairs);
    this->addressWidget->tableView[5]->setModel(model5);

    listofPairs.clear();
    char* showData2 = (char*) malloc(8);
    /*********************SPU*****************************/
    for(int i=0; i<32; i++){
        QString pair_name ="R";
        pair_name.insert(1,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<8; j++){
            *(showData2+j) = projectdata.t_reg[i*8+j+128*127+16*6];
        }
        pair.second = QString(QLatin1String(showData2));
        listofPairs.append(pair);
    }
    for(int i=0; i<4; i++){
        QString pair_name ="SVR";
        pair_name.insert(3,QString::number(i,10));
        pair.first = pair_name;
        for(int j=0; j<16; j++){
            for(int k=0; k<9; k++){
                if(k<8){
                    *(showData+j*9+k) = projectdata.t_reg[i*128+j*8+k+128*127+16*6+32*8];

                }
                else if(j<15){
                    *(showData+j*9+k) = '_';

                }
            }
        }
        pair.second = QString(QLatin1String(showData));
        listofPairs.append(pair);
    }
    TableModel *model6 = new TableModel(listofPairs);
    this->addressWidget->tableView[6]->setModel(model6);

    free(showData);
    free(showData1);
    free(showData2);
}

void MainWindow::setupData(){
    projectdata.regviewtablelist << "Main"<<"CUs" << "SHU" << "BIU"<< "MFetch" << "MReg" << "SPU";

    /**************************************************************/
    //QVector< QList<QPair<QString, QString>>>   vectorListofPairs;
    QPair<QString, QString> pair;
    QList<QPair<QString, QString> > listofPairs;


    pair.first = " MPU_PC";
    pair.second = "#";
    listofPairs.append(pair);
    pair.first = " SPU_PC";
    pair.second = "#";
    listofPairs.append(pair);
    projectdata.vectorListofPairs.append(listofPairs);
    listofPairs.clear();


    /**************************ALU*******************************/
    for(int i=0; i<6; i++){
        QString pair_name ="IALU.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        pair.second = "00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000";
        listofPairs.append(pair);
    }

    for(int i=0; i<6; i++){
        QString pair_name ="IMAC.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        pair.second = QString::number(i,10);
        listofPairs.append(pair);
    }

    for(int i=0; i<6; i++){
        QString pair_name ="IFALU.T";
        pair_name.insert(7,QString::number(i,10));
        pair.first = pair_name;
        pair.second = QString::number(i,10);
        listofPairs.append(pair);
    }

    for(int i=0; i<6; i++){
        QString pair_name ="IFMAC.T";
        pair_name.insert(7,QString::number(i,10));
        pair.first = pair_name;
        pair.second = QString::number(i,10);
        listofPairs.append(pair);
    }
    projectdata.vectorListofPairs.append(listofPairs);
    listofPairs.clear();

    /*******************************SHU********************************/
    for(int i=0; i<8; i++){
        QString pair_name ="SHU0.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        pair.second = "00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000";
        listofPairs.append(pair);
    }
    for(int i=0; i<8; i++){
        QString pair_name ="SHU1.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        pair.second = QString::number(i,10);
        listofPairs.append(pair);
    }
    for(int i=0; i<8; i++){
        QString pair_name ="SHU2.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        pair.second = QString::number(i,10);
        listofPairs.append(pair);
    }
    for(int i=0; i<3; i++){
        QString pair_name ="SHU.TB";
        pair_name.insert(3,QString::number(i,10));
        pair.first = pair_name;
        pair.second = "00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000";
        listofPairs.append(pair);
    }
    projectdata.vectorListofPairs.append(listofPairs);
    listofPairs.clear();

    /*******************************BIU********************************/
    for(int i=0; i<4; i++){
        QString pair_name ="BIU0.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        pair.second = "00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000";
        listofPairs.append(pair);
    }
    for(int i=0; i<4; i++){
        QString pair_name ="BIU1.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        pair.second = QString::number(i,10);
        listofPairs.append(pair);
    }
    for(int i=0; i<4; i++){
        QString pair_name ="BIU2.T";
        pair_name.insert(6,QString::number(i,10));
        pair.first = pair_name;
        pair.second = QString::number(i,10);
        listofPairs.append(pair);
    }
    projectdata.vectorListofPairs.append(listofPairs);
    listofPairs.clear();

    /*********************MFetch*****************************/
    for(int i=0; i<16; i++){
        QString pair_name ="KI";
        pair_name.insert(2,QString::number(i,10));
        pair.first = pair_name;
        pair.second = "000000";
        listofPairs.append(pair);
    }
    projectdata.vectorListofPairs.append(listofPairs);
    listofPairs.clear();


    /*********************MReg*****************************/
    for(int i=0; i<64; i++){
        QString pair_name ="MReg";
        pair_name.insert(4,QString::number(i,10));
        pair.first = pair_name;
        pair.second = "00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000";
        listofPairs.append(pair);
    }
    projectdata.vectorListofPairs.append(listofPairs);
    listofPairs.clear();

    /*********************SPU*****************************/
    for(int i=0; i<32; i++){
        QString pair_name ="R";
        pair_name.insert(1,QString::number(i,10));
        pair.first = pair_name;
        pair.second = "00000000";
        listofPairs.append(pair);
    }
    for(int i=0; i<4; i++){
        QString pair_name ="SVR";
        pair_name.insert(3,QString::number(i,10));
        pair.first = pair_name;
        pair.second = "00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000";
        listofPairs.append(pair);
    }
    projectdata.vectorListofPairs.append(listofPairs);
    listofPairs.clear();


   projectdata.memorydata = QByteArray("");
}

//! [2]
void MainWindow::newLetter()
{
//    textEdit->clear();

//    QTextCursor cursor(textEdit->textCursor());
//    cursor.movePosition(QTextCursor::Start);
//    QTextFrame *topFrame = cursor.currentFrame();
//    QTextFrameFormat topFrameFormat = topFrame->frameFormat();
//    topFrameFormat.setPadding(16);
//    topFrame->setFrameFormat(topFrameFormat);

//    QTextCharFormat textFormat;
//    QTextCharFormat boldFormat;
//    boldFormat.setFontWeight(QFont::Bold);
//    QTextCharFormat italicFormat;
//    italicFormat.setFontItalic(true);

//    QTextTableFormat tableFormat;
//    tableFormat.setBorder(1);
//    tableFormat.setCellPadding(16);
//    tableFormat.setAlignment(Qt::AlignRight);
//    cursor.insertTable(1, 1, tableFormat);
//    cursor.insertText("The Firm", boldFormat);
//    cursor.insertBlock();
//    cursor.insertText("321 City Street", textFormat);
//    cursor.insertBlock();
//    cursor.insertText("Industry Park");
//    cursor.insertBlock();
//    cursor.insertText("Some Country");
//    cursor.setPosition(topFrame->lastPosition());
//    cursor.insertText(QDate::currentDate().toString("d MMMM yyyy"), textFormat);
//    cursor.insertBlock();
//    cursor.insertBlock();
//    cursor.insertText("Dear ", textFormat);
//    cursor.insertText("NAME", italicFormat);
//    cursor.insertText(",", textFormat);
//    for (int i = 0; i < 3; ++i)
//        cursor.insertBlock();
//    cursor.insertText(tr("Yours sincerely,"), textFormat);
//    for (int i = 0; i < 3; ++i)
//        cursor.insertBlock();
//    cursor.insertText("The Boss", textFormat);
//    cursor.insertBlock();
//    cursor.insertText("ADDRESS", italicFormat);
}
void MainWindow::loadFile(const QString &fileName){
    QFile file(fileName);
    if (!file.open(QFile::ReadOnly | QFile::Text)) {
        QMessageBox::warning(this, tr("Application"),
                             tr("Cannot read file %1:\n%2.")
                             .arg(QDir::toNativeSeparators(fileName), file.errorString()));
        return;
    }

    QTextStream in(&file);
    qDebug()<<"filename"<<file.fileName();
    projectdata.SPUFileDir = file.fileName();

    SPUEdit->setPlainText(in.readAll());
    SPUEdit->breakpoints.clear();

    int xiegang = fileName.lastIndexOf("/");
    QString SPUDIR = fileName.left(xiegang+1);

    QString spupcfile = SPUDIR +"PC_LineNumber_UCPS32.txt";
    QFile spufile(spupcfile);
    if(!spufile.open(QIODevice::ReadOnly|QIODevice::Text)){
        return;
    }
    QTextStream sputxtInput(&spufile);
    QString spulinestr;

    ////////add by chenrzh 11.22
    projectdata.spulineindex.clear();
    projectdata.spupcline.clear();

    while(!sputxtInput.atEnd()){
        spulinestr = sputxtInput.readLine();
        spulinestr.remove("PC=");
        spulinestr.remove(" Line number:");
        QStringList sl =spulinestr.split(',');
        bool ok;
        int tmp_a = sl.first().toInt(&ok,16);
        int tmp_b = sl.last().toInt(&ok,10);
        projectdata.spupcline.append(tmp_a);
        projectdata.spulineindex.append(tmp_b);
    }

//    setCurrentFile(fileName);
    statusBar()->showMessage(tr("File loaded"), 2000);
}

void MainWindow::loadFile2(const QString &fileName){
    QFile file(fileName);
    if (!file.open(QFile::ReadOnly | QFile::Text)) {
        QMessageBox::warning(this, tr("Application"),
                             tr("Cannot read file %1:\n%2.")
                             .arg(QDir::toNativeSeparators(fileName), file.errorString()));
        return;
    }

    QTextStream in(&file);
    qDebug()<<"filename"<<file.fileName();
    projectdata.MPUFileDir = file.fileName();

    QString textMPUCode = in.readAll();
    MPUEdit->setPlainText(textMPUCode);
    MPUEdit->breakpoints.clear();

    int xiegang = fileName.lastIndexOf("/");
    QString MPUDIR = fileName.left(xiegang+1);

    QString mpupcfile = MPUDIR +"PC_LineNO.txt";
    QFile mpufile(mpupcfile);
    if(!mpufile.open(QIODevice::ReadOnly|QIODevice::Text)){
        return;
    }
    QTextStream mputxtInput(&mpufile);
    QString mpulinestr;

    //////////////////////add by chenrzh 11.22
    projectdata.mpulineindex.clear();
    projectdata.mpupcline.clear();


    while(!mputxtInput.atEnd()){
        mpulinestr = mputxtInput.readLine();
        mpulinestr.remove("PC=");
        mpulinestr.remove(" Line number:");
        QStringList sl =mpulinestr.split(',');
        bool ok;
        int tmp_a = sl.first().toInt(&ok,16);
        int tmp_b = sl.last().toInt(&ok,10);
        projectdata.mpupcline.append(tmp_a);
        projectdata.mpulineindex.append(tmp_b);
    }

///////////////read file
    for(int i =0;i<17;i++){
        //add code here
        QString filename2;
        int j=i+1;
        if (j<10){
        filename2 = MPUDIR+"slot-ins0"+QString::number(j,10)+".txt";
        }
        else {
            filename2 = MPUDIR + "slot-ins" + QString::number(j,10)+".txt";
        }

        QFile file(filename2);
        if (!file.open(QFile::ReadOnly | QFile::Text)) {
            QMessageBox::warning(this, tr("Application"),
                                 tr("Cannot read file %1:\n%2.")
                                 .arg(QDir::toNativeSeparators(filename2), file.errorString()));
            return;
        }


        QTextStream in(&file);

        QString textMPUCode = in.readAll();
        floatEdit[i]->setPlainText(textMPUCode);
//
//        QTextCursor text_cursor(floatEdit[i]->document()->findBlockByNumber(10+i*5));
//        floatEdit[i]->setTextCursor(text_cursor);
//        floatEdit[i]->centerCursor();
    }
    file.close();

//    setCurrentFile(fileName);
    statusBar()->showMessage(tr("File loaded"), 2000);
}

void MainWindow::open(){
    QString fileName = QFileDialog::getOpenFileName(this);
    if(!fileName.isEmpty())
        loadFile(fileName);
}
void MainWindow::open2(){
    QString fileName = QFileDialog::getOpenFileName(this);
    if(!fileName.isEmpty())
        loadFile2(fileName);


}
void MainWindow::save(){

}

void MainWindow::saveAs(){

}
void MainWindow::run(){

//    QTextCursor text_cursor(SPUEdit->document()->findBlockByNumber(100));
//    SPUEdit->setTextCursor(text_cursor);
//    SPUEdit->verticalScrollBar()->setValue(12);
//    SPUEdit->centerCursor();
//    dock4->show();
//    resi
//    QList<QDockWidget*> tmpDockWidget;
//    tmpDockWidget.append(dock3);
//    tmpDockWidget.append(dock4);
//    QList<int> tmpSizeList;
//    tmpSizeList.append(500*scaleFactorY);
//    resizeDocks(tmpDockWidget,tmpSizeList,Qt::Vertical);
//    commandStatus = 0;

    /**********************add file path here********************************/
    //char* line = (char*)"run:spu_edit_file:mpu_edit_file";
    char* line = (char*) malloc(1000);
    char* spu_dir;
    QByteArray spu_dir_tmp = projectdata.SPUFileDir.toLatin1();
    spu_dir = spu_dir_tmp.data();
    char* mpu_dir;
    QByteArray mpu_dir_tmp = projectdata.MPUFileDir.toLatin1();
    mpu_dir = mpu_dir_tmp.data();
    sprintf(line,"run:%s:%s",spu_dir,mpu_dir);
    int fd = csopen(line);
    recv_fd(fd,&projectdata);
    free(line);

    /****************************add break here*****************************/
    char* break_line = (char*)malloc(1000);
    strcpy(break_line,"break:");
    for(int i=0; i<SPUEdit->breakpoints.length();i++){
        char* point_tmp = (char*)malloc(20);
        for(int j=0; j<projectdata.spulineindex.count(); j++){
            if(projectdata.spulineindex.at(j)>=SPUEdit->breakpoints.at(i)+1){
                sprintf(point_tmp,"%0d:",projectdata.spupcline.at(j));
                break;
            }
        }
        strcat(break_line,point_tmp);
        free(point_tmp);
    }
    strcat(break_line,"$");
    for(int i=0; i<MPUEdit->breakpoints.length();i++){
        char* point_tmp = (char*)malloc(20);       
        for(int j=0; j<projectdata.mpulineindex.count(); j++){
            if(projectdata.mpulineindex.at(j)>=MPUEdit->breakpoints.at(i)+1){
                sprintf(point_tmp,"%0d:",projectdata.mpupcline.at(j));
                break;
            }
        }
        strcat(break_line,point_tmp);
        free(point_tmp);
    }
    fd = csopen(break_line);
    recv_fd(fd,&projectdata);
    free(break_line);

    char* pc_read_line = (char*)"pc_read";
    fd = csopen(pc_read_line);
    recv_fd(fd,&projectdata);

    char* pc_line = (char*)"pc";
    fd = csopen(pc_line);
    recv_fd(fd,&projectdata);

    char* readreg_read_line = (char*)"readreg_read";
    fd = csopen(readreg_read_line);
    recv_fd(fd,&projectdata);

    /*****************pc to line**************/
    int spu_line = 0;
    int mpu_line[18];
    for(int i=0; i<18; i++){
        mpu_line[i] = 0;
    }

    for(int i=0; i<projectdata.spupcline.count(); i++){
        if(projectdata.spupcline.at(i)==projectdata.spu_pc){
            spu_line = projectdata.spulineindex.at(i)-1;
            break;
        }
    }
    for(int i=0; i<projectdata.mpupcline.count(); i++){
        if(projectdata.mpupcline.at(i)==projectdata.mpu_pc[0]){
            mpu_line[0] = projectdata.mpulineindex.at(i)-1;
            break;
        }
    }
    for(int m=1; m<18; m++){
        for(int i=0; i<projectdata.mpupcline.count(); i++){
            if(projectdata.mpupcline.at(i)==projectdata.mpu_pc[m]){
                mpu_line[m] = projectdata.mpulineindex.at(i)-1;
                qDebug()<<"#####This is mpu puc i want:"<<projectdata.mpu_pc[m]<<","<<mpu_line[m];
                break;
            }
        }
    }


    QTextCursor spu_text_cursor(SPUEdit->document()->findBlockByNumber(spu_line));
    SPUEdit->setTextCursor(spu_text_cursor);
    SPUEdit->centerCursor();
    dock4->show();
    qDebug()<<"Run_data:spu_pc"<<projectdata.spu_pc;

    QTextCursor mpu_text_cursor(MPUEdit->document()->findBlockByNumber(mpu_line[0]));
    MPUEdit->setTextCursor(mpu_text_cursor);
    MPUEdit->centerCursor();
    dock4->show();
    qDebug()<<"Run_data:mpu_pc"<<projectdata.mpu_pc[0];


    //mpu_line[17] = mpu_line[17]-3;
    //if(mpu_line[17]<0) mpu_line[17] = 0;

    for(int m=1; m<18; m++){
        QTextCursor text_cursor(floatEdit[m-1]->document()->findBlockByNumber(mpu_line[18-m]));
        floatEdit[m-1]->setTextCursor(text_cursor);
        floatEdit[m-1]->centerCursor();
        dock4->show();
        qDebug()<<"Run_data:Mpu_pc"<<projectdata.mpu_pc[m];
    }



    for(int i=0; i<3; i++){
        char* readreg_line = (char*)"readreg";
        fd = csopen(readreg_line);
        recv_fd(fd,&projectdata);
    }
    showRegData();
    projectdata.t_reg.clear();


    char* readdm_read_line = (char*)"readdm_read";
    fd = csopen(readdm_read_line);
    recv_fd(fd,&projectdata);

    char* readdm_line = (char*)"readdm";
    fd = csopen(readdm_line);
    recv_fd(fd,&projectdata);
    //qDebug()<<"This is want to dm0";


    if(projectdata.dm_trans == 1){
        for(int i=0; i<projectdata.dm_full_count; i++){
            char* dm_data_line = (char*)"readdm";            
            //qDebug()<<"This is want to dm"<<i+1;
            fd = csopen(dm_data_line);
            recv_fd(fd,&projectdata);

        }
    }

    memoryviewer->setData(projectdata.memorydata.left(1572864));
    projectdata.memorydata.clear();

    //qDebug()<<"Run_data:memorydata:"<<projectdata.memorydata;

    //chrzControl
        //setnumber
                //      SPUEdit->setTextCursor(text_cursor);
                //      SPUEdit->centerCursor();
                //      dock4->show();
        //setMemory
        //     projectdata.memorydata = QByteArray("abcdefg!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        //     qDebug()<<projectdata.memorydata.toHex();
                //      memoryviewer->setData(projectdata.memorydata);
       // paint or delete the breakpoint in view
                //    int blockNumber = 2;
                //    int index = SPUEdit->breakpoints.indexOf(blockNumber);
                //    if(index != -1){
                //        SPUEdit->breakpoints.remove(index);
                //    }
                //    else
                //        SPUEdit->breakpoints<<blockNumber;
                //    SPUEdit->update();


}

void MainWindow::step(){

    qDebug()<<"step";
    commandStatus = 1;
    qDebug()<<SPUEdit->breakpoints.size();
//    int blockNumber = 2;
//    int index = SPUEdit->breakpoints.indexOf(blockNumber);
//    if(index != -1){
//        SPUEdit->breakpoints.remove(index);
//    }
//    else
//        SPUEdit->breakpoints<<blockNumber;
//    SPUEdit->update();

    //chrzControl

    char* line = (char*)malloc(20);
    strcpy(line,"step");
    int fd = csopen(line);
    recv_fd(fd,&projectdata);
    free(line);

    /****************************add break here*****************************/
    char* break_line = (char*)malloc(1000);
    strcpy(break_line,"break:");
    for(int i=0; i<SPUEdit->breakpoints.length();i++){
        char* point_tmp = (char*)malloc(20);
        for(int j=0; j<projectdata.spulineindex.count(); j++){
            if(projectdata.spulineindex.at(j)>=SPUEdit->breakpoints.at(i)+1){
                sprintf(point_tmp,"%0d:",projectdata.spupcline.at(j));
                break;
            }
        }
        strcat(break_line,point_tmp);
        free(point_tmp);
    }
    strcat(break_line,"$");
    for(int i=0; i<MPUEdit->breakpoints.length();i++){
        char* point_tmp = (char*)malloc(20);
        for(int j=0; j<projectdata.mpulineindex.count(); j++){
            if(projectdata.mpulineindex.at(j)>=MPUEdit->breakpoints.at(i)+1){
                sprintf(point_tmp,"%0d:",projectdata.mpupcline.at(j));
                break;
            }
        }
        strcat(break_line,point_tmp);
        free(point_tmp);
    }
    qDebug()<<"##################this is break in step:"<<break_line;
    fd = csopen(break_line);
    recv_fd(fd,&projectdata);
    free(break_line);

    char* pc_read_line = (char*)"pc_read";
    fd = csopen(pc_read_line);
    recv_fd(fd,&projectdata);

    char* pc_line = (char*)"pc";
    fd = csopen(pc_line);
    recv_fd(fd,&projectdata);

    char* readreg_read_line = (char*)"readreg_read";
    fd = csopen(readreg_read_line);
    recv_fd(fd,&projectdata);

    /*****************pc to line**************/
    int spu_line = 0;
    int mpu_line[18];
    for(int i=0; i<18; i++){
        mpu_line[i] = 0;
    }

    for(int i=0; i<projectdata.spupcline.count(); i++){
        if(projectdata.spupcline.at(i)==projectdata.spu_pc){
            spu_line = projectdata.spulineindex.at(i)-1;
            break;
        }
    }
    for(int i=0; i<projectdata.mpupcline.count(); i++){
        if(projectdata.mpupcline.at(i)==projectdata.mpu_pc[0]){
            mpu_line[0] = projectdata.mpulineindex.at(i)-1;
            break;
        }
    }
    for(int m=1; m<18; m++){
        for(int i=0; i<projectdata.mpupcline.count(); i++){
            if(projectdata.mpupcline.at(i)==projectdata.mpu_pc[m]){
                mpu_line[m] = projectdata.mpulineindex.at(i)-1;
                break;
            }
        }
    }


    QTextCursor spu_text_cursor(SPUEdit->document()->findBlockByNumber(spu_line));
    SPUEdit->setTextCursor(spu_text_cursor);
    SPUEdit->centerCursor();
    dock4->show();
    qDebug()<<"Run_data:spu_pc"<<projectdata.spu_pc;

    QTextCursor mpu_text_cursor(MPUEdit->document()->findBlockByNumber(mpu_line[0]));
    MPUEdit->setTextCursor(mpu_text_cursor);
    MPUEdit->centerCursor();
    dock4->show();
    qDebug()<<"Run_data:mpu_pc"<<projectdata.mpu_pc[0];

    for(int m=1; m<18; m++){
        QTextCursor text_cursor(floatEdit[m-1]->document()->findBlockByNumber(mpu_line[18-m]));
        floatEdit[m-1]->setTextCursor(text_cursor);
        floatEdit[m-1]->centerCursor();
        dock4->show();
        qDebug()<<"Run_data:Mpu_pc"<<projectdata.mpu_pc[m];
    }



    for(int i=0; i<3; i++){
        char* readreg_line = (char*)"readreg";
        fd = csopen(readreg_line);
        recv_fd(fd,&projectdata);
    }
    showRegData();
    projectdata.t_reg.clear();



    char* readdm_read_line = (char*)"readdm_read";
    fd = csopen(readdm_read_line);
    recv_fd(fd,&projectdata);

    char* readdm_line = (char*)"readdm";
    fd = csopen(readdm_line);
    recv_fd(fd,&projectdata);


    if(projectdata.dm_trans == 1){
        for(int i=0; i<projectdata.dm_full_count; i++){
            char* dm_data_line = (char*)"readdm";
            fd = csopen(dm_data_line);
            recv_fd(fd,&projectdata);

        }
    }

    memoryviewer->setData(projectdata.memorydata.left(1572864));
    projectdata.memorydata.clear();

}

void MainWindow::reRun(){

    /*QString fileName = QFileDialog::getOpenFileName(this, "Open File",QDir::homePath());
           if(!fileName.isEmpty()){
               file.setFileName(fileName);
               memoryviewer->setData(file);
               qDebug()<<"fsfds";
           }
    commandStatus = 2;*/
    //chrzControl

    /**********************add file path here********************************/
    //char* line = (char*)"run:spu_edit_file:mpu_edit_file";
    char* line = (char*) malloc(1000);
    char* spu_dir;
    QByteArray spu_dir_tmp = projectdata.SPUFileDir.toLatin1();
    spu_dir = spu_dir_tmp.data();
    char* mpu_dir;
    QByteArray mpu_dir_tmp = projectdata.MPUFileDir.toLatin1();
    mpu_dir = mpu_dir_tmp.data();
    sprintf(line,"rerun:%s:%s",spu_dir,mpu_dir);
    int fd = csopen(line);
    recv_fd(fd,&projectdata);
    free(line);

    QTextCursor spu_text_cursor_start(SPUEdit->document()->findBlockByNumber(0));
    SPUEdit->setTextCursor(spu_text_cursor_start);
    SPUEdit->centerCursor();
    dock4->show();

    QTextCursor mpu_text_cursor_start(MPUEdit->document()->findBlockByNumber(0));
    MPUEdit->setTextCursor(mpu_text_cursor_start);
    MPUEdit->centerCursor();
    dock4->show();

    for(int m=1; m<18; m++){
        QTextCursor text_cursor(floatEdit[m-1]->document()->findBlockByNumber(0));
        floatEdit[m-1]->setTextCursor(text_cursor);
        floatEdit[m-1]->centerCursor();
        dock4->show();
        qDebug()<<"Run_data:Mpu_pc"<<projectdata.mpu_pc[m];
    }

    /****************************add break here*****************************/
    char* break_line = (char*)malloc(1000);
    strcpy(break_line,"break:");
    for(int i=0; i<SPUEdit->breakpoints.length();i++){
        char* point_tmp = (char*)malloc(20);
        for(int j=0; j<projectdata.spulineindex.count(); j++){
            if(projectdata.spulineindex.at(j)>=SPUEdit->breakpoints.at(i)+1){
                sprintf(point_tmp,"%0d:",projectdata.spupcline.at(j));
                break;
            }
        }
        strcat(break_line,point_tmp);
        free(point_tmp);
    }
    strcat(break_line,"$");
    for(int i=0; i<MPUEdit->breakpoints.length();i++){
        char* point_tmp = (char*)malloc(20);
        for(int j=0; j<projectdata.mpulineindex.count(); j++){
            if(projectdata.mpulineindex.at(j)>=MPUEdit->breakpoints.at(i)+1){
                sprintf(point_tmp,"%0d:",projectdata.mpupcline.at(j));
                break;
            }
        }
        strcat(break_line,point_tmp);
        free(point_tmp);
    }
    fd = csopen(break_line);
    recv_fd(fd,&projectdata);
    free(break_line);

    char* pc_read_line = (char*)"pc_read";
    fd = csopen(pc_read_line);
    recv_fd(fd,&projectdata);

    char* pc_line = (char*)"pc";
    fd = csopen(pc_line);
    recv_fd(fd,&projectdata);

    char* readreg_read_line = (char*)"readreg_read";
    fd = csopen(readreg_read_line);
    recv_fd(fd,&projectdata);

    /*****************pc to line**************/
    int spu_line = 0;
    int mpu_line[18];
    for(int i=0; i<18; i++){
        mpu_line[i] = 0;
    }

    for(int i=0; i<projectdata.spupcline.count(); i++){
        if(projectdata.spupcline.at(i)==projectdata.spu_pc){
            spu_line = projectdata.spulineindex.at(i)-1;
            break;
        }
    }
    for(int i=0; i<projectdata.mpupcline.count(); i++){
        if(projectdata.mpupcline.at(i)==projectdata.mpu_pc[0]){
            mpu_line[0] = projectdata.mpulineindex.at(i)-1;
            break;
        }
    }
    for(int m=1; m<18; m++){
        for(int i=0; i<projectdata.mpupcline.count(); i++){
            if(projectdata.mpupcline.at(i)==projectdata.mpu_pc[m]){
                mpu_line[m] = projectdata.mpulineindex.at(i)-1;
                break;
            }
        }
    }


    QTextCursor spu_text_cursor(SPUEdit->document()->findBlockByNumber(spu_line));
    SPUEdit->setTextCursor(spu_text_cursor);
    SPUEdit->centerCursor();
    dock4->show();
    qDebug()<<"Run_data:spu_pc"<<projectdata.spu_pc;

    QTextCursor mpu_text_cursor(MPUEdit->document()->findBlockByNumber(mpu_line[0]));
    MPUEdit->setTextCursor(mpu_text_cursor);
    MPUEdit->centerCursor();
    dock4->show();
    qDebug()<<"Run_data:mpu_pc"<<projectdata.mpu_pc[0];

    for(int m=1; m<18; m++){
        QTextCursor text_cursor(floatEdit[m-1]->document()->findBlockByNumber(mpu_line[18-m]));
        floatEdit[m-1]->setTextCursor(text_cursor);
        floatEdit[m-1]->centerCursor();
        dock4->show();
        qDebug()<<"Run_data:Mpu_pc"<<projectdata.mpu_pc[m];
    }



    for(int i=0; i<3; i++){
        char* readreg_line = (char*)"readreg";
        fd = csopen(readreg_line);
        recv_fd(fd,&projectdata);
    }
    showRegData();
    projectdata.t_reg.clear();



    char* readdm_read_line = (char*)"readdm_read";
    fd = csopen(readdm_read_line);
    recv_fd(fd,&projectdata);

    char* readdm_line = (char*)"readdm";
    fd = csopen(readdm_line);
    recv_fd(fd,&projectdata);

    if(projectdata.dm_trans == 1){
        for(int i=0; i<projectdata.dm_full_count; i++){
            char* dm_data_line = (char*)"readdm";
            fd = csopen(dm_data_line);
            recv_fd(fd,&projectdata);

        }
    }

    memoryviewer->setData(projectdata.memorydata.left(1572864));
    projectdata.memorydata.clear();
}


void MainWindow::stop(){

    char* line = (char*)malloc(20);
    strcpy(line,"stop");
    int fd = csopen(line);
    recv_fd(fd,&projectdata);
    free(line);

    char* pc_read_line = (char*)"pc_read";
    fd = csopen(pc_read_line);
    recv_fd(fd,&projectdata);

    char* pc_line = (char*)"pc";
    fd = csopen(pc_line);
    recv_fd(fd,&projectdata);

    /*****************pc to line**************/
    int spu_line = 0;
    int mpu_line[18];
    for(int i=0; i<18; i++){
        mpu_line[i] = 0;
    }

    for(int i=0; i<projectdata.spupcline.count(); i++){
        if(projectdata.spupcline.at(i)==projectdata.spu_pc){
            spu_line = projectdata.spulineindex.at(i)-1;
            break;
        }
    }
    for(int i=0; i<projectdata.mpupcline.count(); i++){
        if(projectdata.mpupcline.at(i)==projectdata.mpu_pc[0]){
            mpu_line[0] = projectdata.mpulineindex.at(i)-1;
            break;
        }
    }
    for(int m=1; m<18; m++){
        for(int i=0; i<projectdata.mpupcline.count(); i++){
            if(projectdata.mpupcline.at(i)==projectdata.mpu_pc[m]){
                mpu_line[m] = projectdata.mpulineindex.at(i)-1;
                break;
            }
        }
    }


    QTextCursor spu_text_cursor(SPUEdit->document()->findBlockByNumber(spu_line));
    SPUEdit->setTextCursor(spu_text_cursor);
    SPUEdit->centerCursor();
    dock4->show();
    qDebug()<<"Run_data:spu_pc"<<projectdata.spu_pc;

    QTextCursor mpu_text_cursor(MPUEdit->document()->findBlockByNumber(mpu_line[0]));
    MPUEdit->setTextCursor(mpu_text_cursor);
    MPUEdit->centerCursor();
    dock4->show();
    qDebug()<<"Run_data:mpu_pc"<<projectdata.mpu_pc[0];

    for(int m=1; m<18; m++){
        QTextCursor text_cursor(floatEdit[m-1]->document()->findBlockByNumber(mpu_line[18-m]));
        floatEdit[m-1]->setTextCursor(text_cursor);
        floatEdit[m-1]->centerCursor();
        dock4->show();
        qDebug()<<"Run_data:Mpu_pc"<<projectdata.mpu_pc[m];
    }

    char* readreg_read_line = (char*)"readreg_read";
    fd = csopen(readreg_read_line);
    recv_fd(fd,&projectdata);

    for(int i=0; i<3; i++){
        char* readreg_line = (char*)"readreg";
        fd = csopen(readreg_line);
        recv_fd(fd,&projectdata);
    }
    showRegData();
    projectdata.t_reg.clear();



    char* readdm_read_line = (char*)"readdm_read";
    fd = csopen(readdm_read_line);
    recv_fd(fd,&projectdata);

    char* readdm_line = (char*)"readdm";
    fd = csopen(readdm_line);
    recv_fd(fd,&projectdata);

    if(projectdata.dm_trans == 1){
        for(int i=0; i<projectdata.dm_full_count; i++){
            char* dm_data_line = (char*)"readdm";
            fd = csopen(dm_data_line);
            recv_fd(fd,&projectdata);

        }
    }

    memoryviewer->setData(projectdata.memorydata.left(1572864));
    projectdata.memorydata.clear();
}

void MainWindow::createActions(){

//new
    QMenu *fileMenu = menuBar() -> addMenu(tr("&File"));
    QToolBar *fileToolBar = addToolBar(tr("File"));
//    const QIcon newIcon = QIcon::fromTheme("document-new",QIcon(":/images/new.png"));
//    QAction *newLetterAct = new QAction(newIcon, tr("&New Letter"), this);
//    newLetterAct->setShortcuts(QKeySequence::New);
//    newLetterAct->setStatusTip(tr("Create a new form letter"));
//    connect(newLetterAct, &QAction::triggered, this, &MainWindow::newLetter);
//    fileToolBar->addAction(newLetterAct);
//    fileMenu->addAction(newLetterAct);
//open1
    const QIcon openIcon = QIcon(":/images/open2.png");
    QAction *openAct = new QAction(openIcon,tr("&Open SPU"),this);
    openAct->setShortcut(QKeySequence::Open);
    openAct->setStatusTip(tr("Open a SPU file"));
    connect(openAct,&QAction::triggered,this,&MainWindow::open);
    fileMenu->addAction(openAct);
    fileToolBar->addAction(openAct);
//open2

        const QIcon openIcon2 = QIcon(":/images/open1.png");
        QAction *openAct2 = new QAction(openIcon2,tr("&Open MPU"),this);
        openAct2->setShortcut(QKeySequence::Print);
        openAct2->setStatusTip(tr("Open a MPU file"));
        connect(openAct2,&QAction::triggered,this,&MainWindow::open2);
        fileMenu->addAction(openAct2);
        fileToolBar->addAction(openAct2);

////Save As
//    const QIcon saveAsIcon = QIcon::fromTheme("document-save-as");
//    QAction *saveAsAct = fileMenu->addAction(saveAsIcon, tr("Save &As..."), this, &MainWindow::saveAs);
//    saveAsAct->setShortcuts(QKeySequence::SaveAs);
//    saveAsAct->setStatusTip(tr("Save the document under a new name"));

//run
    QMenu *debugMenu = menuBar()->addMenu(tr("&Debug"));
    QToolBar*debugToolBar = addToolBar(tr("Debug"));
    const QIcon runIcon = QIcon(":/images/run.png");  //view-refresh process-stop
    QAction *runAct = new QAction(runIcon, tr("&Run"), this);
    runAct->setShortcuts(QKeySequence::Refresh);
    runAct->setStatusTip(tr("run the simulation"));
    connect(runAct, &QAction::triggered, this, &MainWindow::run);
    debugMenu->addAction(runAct);
    debugToolBar->addAction(runAct);

    //step
        const QIcon stepIcon = QIcon(":/images/step.png");  //view-refresh process-stop
        QAction *stepAct = new QAction(stepIcon, tr("&Step"), this);
    //    stepIconAct->setShortcuts(QKeySequence::Undo);
        stepAct->setStatusTip(tr("step"));
        connect(stepAct, &QAction::triggered, this, &MainWindow::step);
        debugMenu->addAction(stepAct);
        debugToolBar->addAction(stepAct);

//reRun
    const QIcon undoIcon = QIcon(":/images/reRun.png");  //view-refresh process-stop
    QAction *reRunAct = new QAction(undoIcon, tr("&reRun"), this);
//    reRunAct->setShortcuts(QKeySequence::Undo);
    reRunAct->setStatusTip(tr("rerun the simulation"));
    connect(reRunAct, &QAction::triggered, this, &MainWindow::reRun);
    debugMenu->addAction(reRunAct);
    debugToolBar->addAction(reRunAct);

    //Stop
        const QIcon stopIcon = QIcon(":/images/stop.png");  //view-refresh process-stop
        QAction *stopAct = new QAction(stopIcon, tr("&Stop"), this);
    //    reRunAct->setShortcuts(QKeySequence::Undo);
        stopAct->setStatusTip(tr("stop the simulation"));
        connect(stopAct, &QAction::triggered, this, &MainWindow::stop);
        debugMenu->addAction(stopAct);
        debugToolBar->addAction(stopAct);

    viewMenu = menuBar()->addMenu(tr("&View"));

    menuBar()->addSeparator();

    QMenu *helpMenu = menuBar()->addMenu(tr("&Help"));
    QToolBar*helpToolBar = addToolBar(tr("Help"));
    const QIcon helpIcon = QIcon::fromTheme("help-content"),QIcon(":/images/save.png");
    QAction *aboutAct = new QAction(helpIcon,tr("&Help"),this);
    aboutAct->setShortcuts(QKeySequence::HelpContents);
    aboutAct->setStatusTip(tr("Show the application's About box"));
    connect(aboutAct,&QAction::triggered,this,&QApplication::aboutQt);
    helpToolBar->addAction(aboutAct);
    helpMenu->addAction(aboutAct);

}
void MainWindow::createStatusBar(){
    statusBar()->showMessage(tr("Ready"));
}

void MainWindow::createFloatDock(){

    QStringList floatName;
    //floatName<< "BIU2" <<"BIU1" <<"BIU0" << "MReg5" <<"MReg4"<<"MReg3" << "MReg2" <<"MReg1"<<"MReg0" <<"IFMAC" <<  "IFALU" << "IMAC" << "IALU"  << "SHU2" <<"SHU1"<<"SHU0" << "MFetch";
    floatName<< "MFetch" <<"SHU0" <<"SHU1" << "SHU2" <<"IALU"<<"IMAC" << "IFALU" <<"IFMAC"<<"MReg0" <<"MReg1" <<  "MReg2" << "MReg3" << "MReg4"  << "MReg5" <<"BIU0"<<"BIU1" << "BIU2";


    floatDock[0] = new QDockWidget(floatName[0], this);
    floatDock[0]->setAllowedAreas(Qt::DockWidgetArea_Mask);
    floatEdit[0] = new CodeEditor;
    floatDock[0]->setWidget(floatEdit[0]);
    addDockWidget(Qt::BottomDockWidgetArea, floatDock[0]);
    floatDock[0]->setFloating(true);
    floatDock[0]->setGeometry(100,(150*0+40)*scaleFactorY,280*scaleFactorX,130*scaleFactorY);
    viewMenu->addAction(floatDock[0]->toggleViewAction());


    for (int i=1;i<17;i++){
        floatDock[i] = new QDockWidget(floatName[i], this);
        floatDock[i]->setAllowedAreas(Qt::DockWidgetArea_Mask);
        floatEdit[i] = new CodeEditor;
        floatDock[i]->setWidget(floatEdit[i]);
        floatDock[i]->setFloating(true);
//        floatEdit[i]->setGeometry();

//        floatEdit[i]->setSizePolicy();
        if(i<6){
            floatDock[i]->setGeometry(100,(150*i+40)*scaleFactorY,280*scaleFactorX,130*scaleFactorY);
        } else if (i <12) {
            floatDock[i]->setGeometry(100+300*scaleFactorX,(150*(i-6)+40)*scaleFactorY,280*scaleFactorX,130*scaleFactorY);
        }else {
            floatDock[i]->setGeometry(100+600*scaleFactorX,(150*(i-12)+40)*scaleFactorY,280*scaleFactorX,130*scaleFactorY);
        }
        addDockWidget(Qt::BottomDockWidgetArea, floatDock[i]);

        viewMenu->addAction(floatDock[i]->toggleViewAction());
//        floatEdit[i]->resize(100,200);
    }


}


//! [9]
void MainWindow::createDockWindows()
{
//    QWidget * textwidget = new QWidget(this);
//    textwidget->setWindowFlags(Qt::Widget);
    QVBoxLayout * spuvbox = new QVBoxLayout ;
    SPUEdit = new CodeEditor;
    QLabel *label1 = new QLabel("SPU Code");
    spuvbox->addWidget(label1);
    spuvbox->addWidget(SPUEdit);
    QWidget    * spuwidget = new QWidget;
    spuwidget->setLayout(spuvbox);
    spuvbox->setSpacing(0);
    SPUEdit->setContentsMargins(0,0,0,0);
    label1->setContentsMargins(0,0,0,0);
    SPUEdit->setLineWrapMode(QPlainTextEdit::NoWrap);

    QVBoxLayout * mpuvbox = new QVBoxLayout ;
    MPUEdit = new CodeEditor;
    QLabel *label2 = new QLabel("MPU Code");
    mpuvbox->addWidget(label2);
    mpuvbox->addWidget(MPUEdit);
    QWidget    * mpuwidget = new QWidget;
    mpuwidget->setLayout(mpuvbox);
    mpuvbox->setSpacing(0);
    QSplitter * textsplitter = new QSplitter(Qt::Horizontal,0);
    mpuvbox->setContentsMargins(0,0,0,0);
    spuvbox->setContentsMargins(0,0,0,0);
    MPUEdit->setLineWrapMode(QPlainTextEdit::NoWrap);

    MPUEdit->setContentsMargins(0,0,0,0);
    label2->setContentsMargins(0,0,0,0);
    textsplitter->setHandleWidth(2);
    textsplitter->addWidget(spuwidget);
    textsplitter->addWidget(mpuwidget);
//    textsplitter->setContentsMargins(0,0,0,0);
    setCentralWidget(textsplitter);
    setDockNestingEnabled(true);
// enable the dock can contain tow row(horizontal and vertiacal)

//    QDockWidget *dock = new QDockWidget(tr("SPU code"), this);
//    dock->setAllowedAreas(Qt::DockWidgetArea_Mask);


//    dock->setWidget(SPUEdit);
//    addDockWidget(Qt::TopDockWidgetArea, dock);
//    viewMenu->addAction(dock->toggleViewAction());

//    QDockWidget *dock2 = new QDockWidget(tr("MPU code"), this);
//    dock2->setAllowedAreas(Qt::DockWidgetArea_Mask);
//    addDockWidget(Qt::LeftDockWidgetArea,dock);



//    dock2->setWidget(MPUEdit);
//    splitDockWidget(dock,dock2,Qt::Horizontal);
//    viewMenu->addAction(dock2->toggleViewAction());

//    textwidget->layout()->layout()
//    textwidget->layout()->addWidget(MPUEdit);

//Regs
    QDockWidget *dock3 = new QDockWidget(tr("Registers"), this);
    dock3->setAllowedAreas(Qt::DockWidgetArea_Mask);
    addressWidget = new AddressWidget;
    dock3->setWidget(addressWidget);
    addDockWidget(Qt::BottomDockWidgetArea, dock3);
    viewMenu->addAction(dock3->toggleViewAction());

    dock4 = new QDockWidget(tr("Memory view"), this);
    dock4->setAllowedAreas(Qt::DockWidgetArea_Mask);
    memoryviewer = new MemoryViewer;

    dock4->setWidget(memoryviewer);
    addDockWidget(Qt::RightDockWidgetArea, dock4);
    viewMenu->addAction(dock4->toggleViewAction());
    memoryviewer->setData(projectdata.memorydata);
    dock4->hide();

//    dock4->setMinimumWidth(300);
    for(int i = 0; i<17; i++){
        floatDock[i] = 0;
    }
    QAction *hideAction = new QAction(tr("&HideFloat"),this);
    hideAction->setShortcut(QKeySequence::Replace);
    hideAction->setStatusTip(tr("Hide the float wigets for each slot"));
    connect(hideAction,&QAction::triggered,this,&MainWindow::hideFloat);
    viewMenu->addAction(hideAction);

    QAction *showAction = new QAction(tr("&ShowFloat"),this);
    showAction->setShortcut(QKeySequence::Save);
    showAction->setStatusTip(tr("Show all float wigets for each slot"));
    connect(showAction,&QAction::triggered,this,&MainWindow::showFloat);
    viewMenu->addAction(showAction);

}

void MainWindow::hideFloat(){
    for(int i = 0; i<17; i++){
        floatDock[i]->hide();
//         qDebug()<<"hide ";
//                ->hide();
    }
}

void MainWindow::showFloat(){
    QRect rec = QApplication::desktop()->screenGeometry();
    int height = rec.height();
    int width = rec.width();
    qDebug()<<height;
    qDebug()<<width;
//    scaleFactorX = double(width) ;
//    scaleFactorY = double(height) ;

    for(int i = 0; i<17; i++){
        floatDock[i]->setFloating(true);
        floatDock[i]->show();
////        floatEdit[i]->setGeometry();

////        floatEdit[i]->setSizePolicy();
        if(i<6){
            floatDock[i]->setGeometry(100,(150*i+40)*scaleFactorY,280*scaleFactorX,130*scaleFactorY);
        } else if (i <12) {
            floatDock[i]->setGeometry(100+300*scaleFactorX,(150*(i-6)+40)*scaleFactorY,280*scaleFactorX,130*scaleFactorY);
        }else {
            floatDock[i]->setGeometry(100+600*scaleFactorX,(150*(i-12)+40)*scaleFactorY,280*scaleFactorX,130*scaleFactorY);
        }
    }
}

/////////////////////////////////////////////////// add codeedit below
