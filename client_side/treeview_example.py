# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:19:35 2021

@author: Fanyi Sun
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTreeView,
                             QAbstractItemView, QHeaderView, QStyleFactory)
 
class DemoTreeView(QMainWindow):
    def __init__(self, parent=None):
        super(DemoTreeView, self).__init__(parent)   
        
         # 设置窗口标题
        self.setWindowTitle('实战PyQt5: QTreeView 演示')      
        # 设置窗口大小
        self.resize(520, 360)
      
        self.initUi()
        
    def initUi(self):
        
        #设置表头信息
        model = QStandardItemModel(self)
        model.setHorizontalHeaderLabels(['项目名称', '信息'])
        
        #添加条目
        itemProject = QStandardItem('项目')
        model.appendRow(itemProject)
        model.setItem(0, 1, QStandardItem('项目信息说明'))
        
        #添加子条目
        itemChild = QStandardItem('文件夹1')
        itemProject.appendRow(itemChild)
        itemProject.setChild(0, 1, QStandardItem('信息说明'))
        
        #继续添加
        itemFolder = QStandardItem('文件夹2')
        itemProject.appendRow(itemFolder)
        for group in range (5):
            itemGroup = QStandardItem('组{}'.format(group+1))
            itemFolder.appendRow(itemGroup)
            for ch in range (group+1):
                itemCh = QStandardItem('成员{}'.format(ch+1))
                #添加复选框
                itemCh.setCheckable(True)
                itemGroup.appendRow(itemCh)
                itemGroup.setChild(itemCh.index().row(), 1, QStandardItem('成员{}信息说明'.format(ch+1)))
        itemProject.setChild(itemFolder.index().row(), 1, QStandardItem('文件夹2信息说明'))
        
        treeView = QTreeView(self)
        treeView.setModel(model)
        #调整第一列的宽度
        treeView.header().resizeSection(0, 160)
        #设置成有虚线连接的方式
        treeView.setStyle(QStyleFactory.create('windows'))
        #完全展开
        treeView.expandAll()
        
        #显示选中行的信息
        treeView.selectionModel().currentChanged.connect(self.onCurrentChanged)
                
        self.model = model
        self.treeView = treeView
        self.setCentralWidget(treeView)
            
    def onCurrentChanged(self,current, previous):
        txt = '父级:[{}] '.format(str(current.parent().data()))
        txt += '当前选中:[(行{},列{})] '.format(current.row(), current.column())
        
        name=''
        info=''
        if current.column() == 0:
            name = str(current.data())
            info = str(current.sibling(current.row(), 1).data())
        else:
            name = str(current.sibling(current.row(), 0).data())
            info = str(current.data())
        
        txt += '名称:[{}]  信息:[{}]'.format(name, info)    
        
        self.statusBar().showMessage(txt)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoTreeView()
    window.show()
    sys.exit(app.exec())
