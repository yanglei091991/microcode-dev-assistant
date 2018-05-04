#ifndef TABLEVIEW_H
#define TABLEVIEW_H

#include <QDialog>
#include <QEvent>
#include <QLabel>
#include <QMouseEvent>
#include <QTableView>
#include <QVBoxLayout>
#include <QHeaderView>

#include <QThread>

class Sleeper : public QThread
{
public:
    static void usleep(unsigned long usecs){QThread::usleep(usecs);}
    static void msleep(unsigned long msecs){QThread::msleep(msecs);}
    static void sleep(unsigned long secs){QThread::sleep(secs);}
};

class TableView: public QTableView{
    Q_OBJECT
    QDialog *popup;
    QLabel *popupLabel;

public:
    TableView(QWidget *parent = Q_NULLPTR):QTableView(parent){
        viewport()->installEventFilter(this);
        setMouseTracking(true);
        popup = new QDialog(this, Qt::Popup | Qt::ToolTip);

        QVBoxLayout *layout = new QVBoxLayout;
        popupLabel = new QLabel(popup);
        popupLabel->setWordWrap(true);
        layout->addWidget(popupLabel);
        popupLabel->setTextFormat(Qt::RichText);
        //popupLabel->setOpenExternalLinks(true);
        popup->setLayout(layout);
        popup->installEventFilter(this);
    }

    bool eventFilter(QObject *watched, QEvent *event){
        if(viewport() == watched){
            if(event->type() == QEvent::MouseMove){
                QMouseEvent *mouseEvent = static_cast<QMouseEvent*>(event);
                QModelIndex index = indexAt(mouseEvent->pos());
                if(index.isValid()){
                    showPopup(index);
                }
                else{
                    popup->hide();
                }
            }
            else if(event->type() == QEvent::Leave){
                popup->hide();
            }
        }
        else if(popup == watched){
            if(event->type() == QEvent::Leave){
                popup->hide();
            }
        }
//        return QTableView::eventFilter(watched, event);

        return 0;
    }

private:
    void showPopup (const QModelIndex &index) const {
        if(index.column() == 1){
            QRect r = visualRect(index);
            popup->move(viewport()->mapToGlobal(r.bottomLeft()));
//            popup->setFixedSize(100, popup->heightForWidth(100));
//            popupLabel->setText(index.data(Qt::DisplayRole).toString());
//              popupLabel->setText(index.data(Qt::DisplayRole).toString().replace(QChar('_') , QChar(' ')));
            QString showString = index.data(Qt::DisplayRole).toString();
            if (showString.length()>36){
                for (int i = 0; i<8; i++){
                    showString = showString.replace(17+18*i,1,QChar(' '));
                }
            }

            popupLabel->setText(showString);

            popup->adjustSize();
            popup->show();
                   Sleeper::msleep(20);
        }
        else {
            popup->hide();
        }
    }
};

#endif // TABLEVIEW_H

//#ifndef TABLEVIEW_H
//#define TABLEVIEW_H

//#include <QDialog>
//#include <QEvent>
//#include <QLabel>
//#include <QMouseEvent>
//#include <QTableView>
//#include <QVBoxLayout>
//#include <QHeaderView>

//class TableView: public QTableView{
//Q_OBJECT
//QDialog *popup;
//QLabel *popupLabel;

//public:
//TableView(QWidget *parent = Q_NULLPTR):QTableView(parent){
//viewport()->installEventFilter(this);
//setMouseTracking(true);
//popup = new QDialog(this, Qt::Popup | Qt::ToolTip);

//QVBoxLayout *layout = new QVBoxLayout;
//popupLabel = new QLabel(popup);
//popupLabel->setWordWrap(true);
//layout->addWidget(popupLabel);
//popupLabel->setTextFormat(Qt::RichText);
////popupLabel->setOpenExternalLinks(true);
//popup->setLayout(layout);
//popup->installEventFilter(this);
//}

//bool eventFilter(QObject *watched, QEvent *event){
//if(viewport() == watched){
//if(event->type() == QEvent::MouseMove){
//QMouseEvent *mouseEvent = static_cast<QMouseEvent*>(event);
//QModelIndex index = indexAt(mouseEvent->pos());
//if(index.isValid()){
//showPopup(index);
//}
//else{
//popup->hide();
//}
//}
//else if(event->type() == QEvent::Leave){
//popup->hide();
//}
//}
//else if(popup == watched){
//if(event->type() == QEvent::Leave){
//popup->hide();
//}
//}
//return QTableView::eventFilter(watched, event);
//}

//private:
//void showPopup (const QModelIndex &index) const {
//if(index.column() == 1){
//QRect r = visualRect(index);
//popup->move(viewport()->mapToGlobal(r.bottomLeft()));
//popup->setFixedSize(100, popup->heightForWidth(100));
//popupLabel->setText(index.data(Qt::DisplayRole).toString().replace(QChar('_'), QChar(' ')));
//popup->adjustSize();
//popup->show();
//}
//else {
//popup->hide();
//}
//}
//};

//#endif // TABLEVIEW_H


