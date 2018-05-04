#include "memoryviewer.h"

#include <QPainter>
#include <QScrollBar>
#include <QDebug>
#include <QMouseEvent>
#include <QMenu>
#include<qinputdialog.h>
#include "mydialog.h"



MemoryViewer::MemoryViewer(QWidget *parent):QAbstractScrollArea(parent)
{
    ioDevice = new QBuffer(this);
    init();
    connect(verticalScrollBar(), &QScrollBar::valueChanged, this, &MemoryViewer::adjustContent);
    connect(horizontalScrollBar(), &QScrollBar::valueChanged, this, &MemoryViewer::adjustContent);

     queryAct = new QAction(tr("&Query"),this);
    queryAct->setStatusTip(tr("Query DM"));
    connect(queryAct,&QAction::triggered,this,&MemoryViewer::query);
}

MemoryViewer::~MemoryViewer()
{

}
void MemoryViewer::query(){
    qDebug()<<"open function";
//    QTextCursor text_cursor(SPUEdit->document()->findBlockByNumber(100));
//    SPUEdit->setTextCursor(text_cursor);
//    QCursor cursor(this->);
//    this->verticalScrollBar()->scroll(1,2);

//    int d = QInputDialog::getInt(this, QString("address"),QString("label"),1);
    MyDialog *mydialog = new MyDialog(this);
     QString addrString ;
    if(mydialog->exec() == QDialog::Accepted){
       addrString= mydialog->getNewValue();
    }
    bool ok;
    int addressInt = addrString.toUInt(&ok,16);
    if (!ok){
        qDebug()<<"convert error!";
        return;
    }
    int lineNum = addressInt /8 -1;

//    QInputDialog::getText(this,1,1,1);
    //please input  the Addr (Hex) here
    qDebug()<<addrString;
    this->verticalScrollBar()->setValue(lineNum);
}

//void MemoryViewer::mousePressEvent(QMouseEvent *e){
//    if(e->button()==Qt::RightButton){
//        qDebug()<<"press!";
//    }
//}

void MemoryViewer::contextMenuEvent(QContextMenuEvent *e){
    QMenu *menu = new QMenu();
    menu->addSeparator();
    menu->addSeparator();
    menu->addAction(queryAct);
    menu->addSeparator();
    menu->addSeparator();
//    menu->addAction(Act_Normal);
    menu->addSeparator();
    menu->addSeparator();
    menu->exec(e->globalPos());
    delete menu;
    }


void MemoryViewer::init()
{
    nBlockAddress = 2;
    mBytesPerLine = 8;

    pxWidth = fontMetrics().width(QChar('0'));
    pxHeight = fontMetrics().height();

}

int MemoryViewer::addressWidth()
{
    return  (nBlockAddress*6+ nBlockAddress -1)*pxWidth;
}

int MemoryViewer::hexWidth()
{
    return (mBytesPerLine*3+1)*pxWidth;
}

int MemoryViewer::asciiWidth()
{
    return (mBytesPerLine*2 +1)*pxWidth;
}

QByteArray MemoryViewer::data(qint64 pos, qint64 count)
{
    QByteArray buffer;

    if (pos >= size)
        return buffer;

    if (count < 0)
        count = size;
    else
        if ((pos + count) > size)
            count = size - pos;

    if(ioDevice->open(QIODevice::ReadOnly)){
        ioDevice->seek(pos);
        buffer = ioDevice->read(count);
        ioDevice->close();
    }
    return buffer;
}

void MemoryViewer::setData(const QByteArray &ba)
{
    buffer.setData(ba);
    setData(buffer);

}

bool MemoryViewer::setData(QIODevice &device)
{
    ioDevice = &device;
    bool ok = ioDevice->open(QIODevice::ReadOnly);
    if(ok){
        size = ioDevice->size();
        ioDevice->close();
        qDebug()<<size;
    }
    else{
        QBuffer *buf = new QBuffer(this);
        ioDevice = buf;
    }
    init();
    adjustContent();
    return ok;
}

void MemoryViewer::resizeEvent(QResizeEvent *)
{
    adjustContent();
}


void MemoryViewer::paintEvent(QPaintEvent *)
{
    QPainter painter(viewport());

    int offsetX = horizontalScrollBar()->value();

    int y = pxHeight;
    QString address;

    painter.setPen(viewport()->palette().color(QPalette::WindowText));

    for(int row = 0; row <= dataVisible.size()/mBytesPerLine;  row++){
//        QString str = QString("%1").arg(startPos + mBytesPerLine*row, nBlockAddress*4, 16, QChar('0')).toUpper();
//        int i = 0;
//        address = "";
//        while(i < nBlockAddress){
//            address += str.mid(i*4, 4) + ":";
//            i++;
//        }
//        address.remove(address.size()-1, 1);


        QString str1=QString("%1").arg(startPos + mBytesPerLine*row, 6, 16, QChar('0')).toUpper();
        QString str2=QString("%1").arg(startPos + mBytesPerLine*(row+1)-1, 6, 16, QChar('0')).toUpper();
        address=str1 +":"+str2;

        painter.drawText(pxWidth/2 -offsetX , y, address);
        y+=pxHeight;
    }

    int x;
    int lx = addressWidth() +pxWidth;
    painter.drawLine(lx-offsetX, 0, lx-offsetX, height());
    lx += pxWidth/2;
    y = pxHeight;

    //hex data
    x = lx-offsetX+3*pxWidth;
    int w = 3*pxWidth;
    for(int col =0; col < mBytesPerLine; col++){
        painter.fillRect(x-pxWidth/2, 0, w, height(), viewport()->palette().color(QPalette::AlternateBase));
        x+= 6*pxWidth;
    }

    int bPos = 0;
    for(int row=0; row < nRowsVisible; row++){
        x = lx-offsetX;
        for(int col =0; (col < mBytesPerLine) && (bPos < dataHex.size()) ; col++){
            QString str = dataHex.mid(bPos*2,2).toUpper();
            painter.drawText(x, y, str);
            x += 3*pxWidth;
            bPos += 1;
        }
        y+= pxHeight;
    }

    lx = addressWidth() + hexWidth();
//    painter.drawLine(lx-offsetX, 0, lx-offsetX, height());

    lx += pxWidth/2;

    bPos = 0;
    y = pxHeight ;
    int ch;
    for(int row=0; row < nRowsVisible; row++){
        x = lx-offsetX;
        for(int col =0; (col < mBytesPerLine) && (bPos < dataVisible.size()) ; col++){
            ch  = (uchar)dataVisible.at(bPos);
            if ( ch < 0x20 )
                ch = '.';
           // painter.drawText(x, y, QChar(ch));
            x += 2*pxWidth;
            bPos += 1;
        }
        y+= pxHeight;
    }
//    this->setMaximumWidth(lx);
//    this->setMinimumWidth(lx);
}

void MemoryViewer::adjustContent()
{
    int w = addressWidth() + hexWidth();
    horizontalScrollBar()->setRange(0, w - viewport()->width());
    horizontalScrollBar()->setPageStep(viewport()->width());

    nRowsVisible = viewport()->height()/pxHeight;
    int val = verticalScrollBar()->value();
    startPos = (qint64)val*mBytesPerLine;
    endPos = startPos + nRowsVisible*mBytesPerLine -1;

    int lineCount = size/mBytesPerLine;
    verticalScrollBar()->setRange(0,  lineCount-nRowsVisible);
    verticalScrollBar()->setPageStep(nRowsVisible);

    if(endPos >= size){
        endPos = size-1;
    }
    dataVisible = data(startPos, endPos-startPos + mBytesPerLine +1);
    dataHex = dataVisible.toHex();
    viewport()->update();
}
