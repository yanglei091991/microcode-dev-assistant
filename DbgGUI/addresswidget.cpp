/****************************************************************************
**
** Copyright (C) 2016 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the examples of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:BSD$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** BSD License Usage
** Alternatively, you may use this file under the terms of the BSD license
** as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of The Qt Company Ltd nor the names of its
**     contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/

#include "addresswidget.h"

#include <QtWidgets>
#include <QSqlTableModel>
#include <QDebug>

extern ProjectData projectdata;
//! [0]
AddressWidget::AddressWidget(QWidget *parent)
    : QTabWidget(parent)
{
//    table = new TableModel(this);
//    setTabPosition(QTabWidget::South);
    setupTabs();
}


void AddressWidget::setupTabs()
{

    for (int i = 0; i < projectdata.vectorListofPairs.size(); ++i) {
        QString str = projectdata.regviewtablelist.at(i);
        TableModel *model = new TableModel(projectdata.vectorListofPairs[i],this);
        tableView[i] = new TableView;

        tableView[i]->setModel(model);
        tableView[i]->resizeColumnsToContents();
        tableView[i]->horizontalScrollBar()->setPageStep(1);
        tableView[i]->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
        tableView[i]->setHorizontalScrollMode(QAbstractItemView::ScrollPerPixel);
        tableView[i]->setSelectionBehavior(QAbstractItemView::SelectRows);
        tableView[i]->horizontalHeader()->setStretchLastSection(true);
        tableView[i]->verticalHeader()->hide();
        tableView[i]->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tableView[i]->setSelectionMode(QAbstractItemView::SingleSelection);

        addTab(tableView[i], str);
    }

}
//! [1]

//tableView->setColumnCount(2);
//tableView->setRowCount(10);
//        tableView->setItem(2,1,&a);
//tableView->setItem(0,0,new QTableWidgetItem("Item1"));
//tableView->setItem(0,1,new QTableWidgetItem("Item2"));
//tableView->setItem(0,2,new QTableWidgetItem("Item3"));
//tableView->setItem(1,0,new QTableWidgetItem("Item1"));
//tableView->setItem(1,1,new QTableWidgetItem("Item2"));
//tableView->setItem(1,2,new QTableWidgetItem("Item3"));
//        tableView->hideColumn(0);
//tableView->setSelectionBehavior(QAbstractItemView::SelectRows);
//tableView->horizontalHeader()->setStretchLastSection(true);
//tableView->verticalHeader()->hide();
//tableView->setEditTriggers(QAbstractItemView::NoEditTriggers);
//tableView->setSelectionMode(QAbstractItemView::SingleSelection);

