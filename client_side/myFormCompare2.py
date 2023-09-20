# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:52:11 2021

@author: Fanyi Sun
"""

import pandas as pd

from PyQt5.QtWidgets import  (QWidget, QAbstractItemView,
                              QListWidgetItem, QMessageBox)

from PyQt5.QtCore import  pyqtSlot, Qt, pyqtSignal

from ui_QWFormCompare2 import Ui_QWFormCompare2

import sys
sys.path.append('..\\target_evaluation')
from main_target import main_target


class QmyFormCompare2(QWidget):
    # customised signal for showing the result
    seeResult = pyqtSignal(bool)
    resultChanged = pyqtSignal(pd.DataFrame, dict, dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormCompare2()
        self.ui.setupUi(self)
        
        self.init_ui()
        
        self.ui.lw_all.setAlternatingRowColors(Qt.Checked)
        self.ui.lw_tbCompared.setAlternatingRowColors(Qt.Checked)
        self.ui.lw_all.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.lw_tbCompared.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.storeDir = ''
        
    def init_ui(self):
        self.ui.lw_all.clear()
        self.sample_items = []
        
        
##  ================ Slot Functions by connectSlotsByName()===================
    @pyqtSlot()
    def on_btnAdd_clicked(self):
        items_imported = self.ui.lw_all.selectedItems()
        if not items_imported:
            return
        
        for item_imported in items_imported:
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
                self.ui.lw_all.item(i).setCheckState(Qt.Unchecked)


    @pyqtSlot()
    def on_btnCompare_clicked(self):
        print(self.targetF)
        if self.storeDir == '':
            dlgTitle = "Critical"
            strInfo = "Please import vehicle data first"
            QMessageBox.critical(self, dlgTitle, strInfo)
            return
        if self.ui.lw_tbCompared.count() == 0:
            dlgTitle = "Critical"
            strInfo = "Please select at least one vehicle for comparison"
            QMessageBox.critical(self, dlgTitle, strInfo)
            return
        veh_identities = self.sample_items
        df_ranking, allRb_F, allRb_R = main_target(veh_identities,
                                   self.storeDir, self.weightF, self.weightR, 
                                   self.targetF, self.targetR)
        
        self.resultChanged.emit(df_ranking, allRb_F, allRb_R)
        
        dlgTitle = "Question"
        strInfo = "The result is available now.\nDo you want to see the result?"
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo,
                                      QMessageBox.Yes |QMessageBox.No |
                                      QMessageBox.Cancel, defaultBtn)
        if result == QMessageBox.Yes:
            self.seeResult.emit(True)