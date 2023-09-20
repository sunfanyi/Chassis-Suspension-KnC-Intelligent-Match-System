# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 17:13:36 2021

@author: Fanyi Sun
"""

import os
import sys

from PyQt5.QtCore import pyqtSlot, Qt, QDir, pyqtSignal
from PyQt5.QtWidgets import (QListView, QListWidget, QTreeView,
                             QAbstractItemView,
                             QListWidgetItem, QMessageBox, QLabel,
                             QProgressBar, QMainWindow, QFileDialog)

from ui_QWFormImport import Ui_QWFormImport

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append('..\\database_establishment')
from main_database import main_database


class QmyFormImport(QMainWindow):
    listWidgetChanged = pyqtSignal(QListWidget)
    storeDirChanged = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormImport()
        self.ui.setupUi(self)
        
        self.storeDir = ''
        self.imported_vehicles = []
        # self.__FlagSelectable = (Qt.ItemIsSelectable | Qt.ItemIsEnabled |
        #                          Qt.ItemIsUserCheckable)
        self.__FlagSelectable = (Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.__FlagNotEditable = (Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.__buildStatusBar()
        self.ui.listWidget.setAlternatingRowColors(Qt.Checked)
        self.ui.lineEdit.setEnabled(False)
        # self.setAutoFillBackground(True)
        
        # self.ui.btnImport.setEnabled(False)


    def __buildStatusBar(self):
        self.__LabFile = QLabel(self)
        self.__LabFile.setMinimumWidth(150)
        self.__LabFile.setText('Uploading: ')
        self.ui.statusBar.addWidget(self.__LabFile)
        
        self.__progressBar = QProgressBar(self)
        self.__progressBar.setMaximumWidth(200)
        self.__progressBar.setMinimum(0)
        self.__progressBar.setMaximum(100)
        self.__progressBar.setValue(12)
        self.ui.statusBar.addWidget(self.__progressBar)

        self.__LabInfo = QLabel(self)
        self.__LabInfo.setText("Vechcle Path: ")
        self.ui.statusBar.addPermanentWidget(self.__LabInfo)
        
        
##  ====================Customised Functional Functions=======================
    def __fill_listWidget(self, veh_identities, veh_paths):
        self.ui.listWidget.clear()
        for i in range(len(veh_identities)):
            # if veh_identities[i] in self.imported_vehicles:
            #     continue
            self.imported_vehicles.append(veh_identities[i])
            item = QListWidgetItem()
            item.setText(veh_identities[i])
            # item.setData(Qt.UserRole,veh_paths[i])
            item.setFlags(self.__FlagSelectable)
            # item.setCheckState(Qt.Checked)
            self.ui.listWidget.addItem(item)
        # self.ui.listWidget.sortItems(0)
        # self.ui.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.ui.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        
##  ================ Slot Functions by connectSlotsByName()===================
    @pyqtSlot()
    def on_btnStore_clicked(self):
        '''choose a directoty for storing data'''
        self.ui.listWidget.clear()
        curPath = QDir.currentPath()    # get current directoty
        path = '..\curPath'
        dlgTitle = "Choose a directory for storing data..."
        self.storeDir = QFileDialog.getExistingDirectory(self,
                               dlgTitle, path, QFileDialog.ShowDirsOnly)
        self.ui.lineEdit.setText(self.storeDir)
        summary_path = self.storeDir + '\\Vehicle Summary.txt'
        try:
            with open(summary_path,'r',encoding='utf-8') as f:
                lines = f.readlines()
                veh_identities = [a.split('\t')[0] for a in lines]
                veh_paths = [a.split('\t')[1] for a in lines]
                # fill with vehicles that are already stored
                self.__fill_listWidget(veh_identities, veh_paths)
        except FileNotFoundError:
            pass
        self.listWidgetChanged.emit(self.ui.listWidget)
        self.storeDirChanged.emit(self.storeDir)


    @pyqtSlot()
    def on_btnImport_clicked(self):
        '''select vehicle paths to import'''
        if self.storeDir == '':
            dlgTitle = "Warning"
            strInfo = "Please choose a store path"
            QMessageBox.warning(self, dlgTitle, strInfo)
            return

        # select multiple directories
        fileDialog = QFileDialog(caption='Choose the raw data location...')
        fileDialog.setFileMode(QFileDialog.DirectoryOnly)
        fileDialog.setOption(QFileDialog.DontUseNativeDialog, True)
        
        listView = fileDialog.findChild(QListView, 'listView')
        if listView:
            listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
            
        detailView = fileDialog.findChild(QTreeView)
        if detailView:
            detailView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        if fileDialog.exec():
            file_list = fileDialog.selectedFiles()
        else:
            return
        
        database_paths = file_list
        store_path = self.storeDir
        veh_identities, veh_paths = main_database(database_paths, store_path)
        self.__fill_listWidget(veh_identities, veh_paths)
        self.listWidgetChanged.emit(self.ui.listWidget)
            

    @pyqtSlot()
    def on_btnDel_clicked(self):
        '''delete selected vehicles but keep the files in the store path'''
        items = self.ui.listWidget.selectedItems()
        for item in items:
            self.imported_vehicles.remove(item.text())
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
        self.listWidgetChanged.emit(self.ui.listWidget)
            
        
    @pyqtSlot()
    def on_btnDelAll_clicked(self):
        '''delete all vehicles but keep the files in the store path'''
        dlgTitle = 'Reset All'
        strInfo = 'Confirm to delete all vehicles?'
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes
                                      | QMessageBox.No | QMessageBox.Cancel,
                                      defaultBtn)
        if result == QMessageBox.Yes:
            self.imported_vehicles = []
            self.ui.listWidget.clear()
            self.listWidgetChanged.emit(self.ui.listWidget)

