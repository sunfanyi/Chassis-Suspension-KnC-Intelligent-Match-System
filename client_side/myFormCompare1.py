# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:33:38 2021

@author: Fanyi Sun
"""

import pandas as pd

from PyQt5.QtWidgets import  (QWidget, QAbstractItemView,
                              QListWidgetItem, QMessageBox)

from PyQt5.QtCore import  pyqtSlot, Qt, pyqtSignal

from PyQt5.QtGui import QColor

from ui_QWFormCompare1 import Ui_QWFormCompare1

import sys
sys.path.append('..\\similarity_evaluation')
from main_similarity import main_similarity


class QmyFormCompare1(QWidget):
    # customised signal for showing the result
    seeResult = pyqtSignal(bool)
    resultChanged = pyqtSignal(pd.DataFrame, dict, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormCompare1()
        self.ui.setupUi(self)
        
        self.init_ui()
        
        self.ui.lw_all.setAlternatingRowColors(Qt.Checked)
        self.ui.lw_tbCompared.setAlternatingRowColors(Qt.Checked)
        self.ui.lw_all.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.lw_tbCompared.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.storeDir = ''
        
    def init_ui(self):
        self.ui.lw_all.clear()
        self.ui.lineTarget.clear()
        self.target_item = None
        self.sample_items = []
        
        
##  ================ Slot Functions by connectSlotsByName()===================
    @pyqtSlot()
    def on_btnSetTarget_clicked(self):
        items = self.ui.lw_all.selectedItems()
        
        if not items:
            dlgTitle = "Critical"
            strInfo = "Please choose a target vehicle"
            QMessageBox.critical(self, dlgTitle, strInfo)
            return
        if len(items) > 1:
            dlgTitle = "Critical"
            strInfo = "Please choose one target vehicle only"
            QMessageBox.critical(self, dlgTitle, strInfo)
            return
        
        if self.target_item is not None:
            # return the previous target to default
            self.target_item.setCheckState(Qt.Unchecked)
            self.target_item.setBackground(QColor(0,0,0,0))
            
        self.target_item = items[0]
        self.target_veh = self.target_item.text()
        # self.target_path = self.target_item.data(Qt.UserRole)
        self.ui.lineTarget.setText(self.target_veh)
        self.target_item.setCheckState(Qt.Checked)
        self.target_item.setBackground(QColor('yellow')) # highlight
        

    @pyqtSlot()
    def on_btnAdd_clicked(self):
        items_imported = self.ui.lw_all.selectedItems()
        if not items_imported:
            return
        
        for item_imported in items_imported:
            if item_imported != self.target_item:
                item_imported.setCheckState(Qt.Checked)
                item_comp = QListWidgetItem() # items to be compared
                item_comp.setText(item_imported.text())
                # item_comp.setData(Qt.UserRole, item_imported.data(Qt.UserRole))
                item_comp.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.ui.lw_tbCompared.addItem(item_comp)
                self.sample_items.append(item_imported.text())
        
        
    @pyqtSlot()
    def on_btnRemove_clicked(self):
        items_comp = self.ui.lw_tbCompared.selectedItems()
        for item_comp in items_comp:
            self.ui.lw_tbCompared.takeItem(self.ui.lw_tbCompared.row(item_comp))
            
            # set unchecked in listWidget_all for removed items
            text = item_comp.text()
            count = self.ui.lw_all.count()
            for i in range(count):
                if self.ui.lw_all.item(i).text() == text:
                    self.ui.lw_all.item(i).setCheckState(Qt.Unchecked)
        
        
    @pyqtSlot()
    def on_btnRemoveAll_clicked(self):
        dlgTitle = 'Remove All'
        strInfo = 'Confirm to remove all vehicles for comparison?'
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes
                                      | QMessageBox.No | QMessageBox.Cancel,
                                      defaultBtn)
        if result == QMessageBox.Yes:
            self.ui.lw_tbCompared.clear()
            self.sample_items = []
            # set unchecked for all items in listWidge_all
            count = self.ui.lw_all.count()
            for i in range(count):
                if self.ui.lw_all.item(i) != self.target_item:
                    self.ui.lw_all.item(i).setCheckState(Qt.Unchecked)


    @pyqtSlot()
    def on_btnCompare_clicked(self):
        if self.storeDir == '':
            dlgTitle = "Critical"
            strInfo = "Please import vehicle data first"
            QMessageBox.critical(self, dlgTitle, strInfo)
            return
        if self.target_item is None:
            dlgTitle = "Critical"
            strInfo = "Please select a target vehicle"
            QMessageBox.critical(self, dlgTitle, strInfo)
            return
        if self.ui.lw_tbCompared.count() == 0:
            dlgTitle = "Critical"
            strInfo = "Please select at least one vehicle for comparison"
            QMessageBox.critical(self, dlgTitle, strInfo)
            return
        veh_identities = self.sample_items
        df_ranking, allSimi = main_similarity(self.target_veh, veh_identities,
                                              self.storeDir, self.weight)
        self.resultChanged.emit(df_ranking, allSimi, self.target_veh)
        
        dlgTitle = "Question"
        strInfo = "The result is available now.\nDo you want to see the result?"
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo,
                                      QMessageBox.Yes |QMessageBox.No |
                                      QMessageBox.Cancel, defaultBtn)
        if result == QMessageBox.Yes:
            self.seeResult.emit(True)