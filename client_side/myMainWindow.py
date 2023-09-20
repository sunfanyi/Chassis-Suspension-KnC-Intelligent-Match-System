# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:27:02 2021

@author: Fanyi Sun
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd

from PyQt5.QtWidgets import (QMainWindow, QStackedWidget,
                             QListWidget, QListWidgetItem, QActionGroup)

from PyQt5.QtCore import pyqtSlot, Qt, QSize

from PyQt5.QtGui import QIcon

from ui_MainWindow import Ui_MainWindow

from myFormWelcome import QmyFormWelcome
from myFormImport import QmyFormImport

from myFormSetWeight1 import QmyFormSetWeight1
from myFormSetWeight2 import QmyFormSetWeight2
from myFormCompare1 import QmyFormCompare1
from myFormCompare2 import QmyFormCompare2
from myFormResult1 import QmyFormResult1
from myFormResult2 import QmyFormResult2
from myFormSetTarget import QmyFormSetTarget

from qss import QSS


class QmyMainWindow(QMainWindow):
    """
    The mode selector on the left can be used to switch windows, each 
    corresponds to different functions, but are all necessary for achieving
    the main functions.
    
    There are two modes in this tool - Similarity / Reliability.
    The first one is for comparing the similarity between vehicles.
    The second one is for finding how close the vehicle data is to the target data.
    
    This two modes have windows which share the same name but with different
    functions, eg, SetWeight, Compare, Result. When clicking the switch button,
    these three buttons would connect to different windows.
    
    To make distinguishment in the coding, 1 and 2 are used as the suffix for
    these two modes. For example, the function self.__formSetWeight1() and 
    self.__formSwtWeight2() would generate the SetWeight windows for 
    mode-Similarity and mode-Reliability respectively.
    """
    def __init__(self, parent=None):
        super().__init__(parent)    # create window
        self.ui = Ui_MainWindow()     # create ui
        self.ui.setupUi(self)
        # self.resize(1600,1000)
        
        self.stack = QStackedWidget(self)
        self.stack.setVisible(True)
        self.setCentralWidget(self.stack)
        self.ui.toolBar.setMinimumSize(QSize(175, 0))
        
        qss = QSS()
        self.ui.toolBar.setStyleSheet(qss.toolbar)
        # self.ui.toolBar.setStyleSheet("background:yellow")
        
        icon = QIcon(":/icons/images/icons/Volvo Car Logo CMYK_ jpg-Small.png")
        self.setWindowIcon(icon) # top left icon
        # self.setWindowTitle(' Volvo K&C Parameter Recommendation Tool')
        self.setWindowTitle(' Chassis Suspension K&C Design Intelligent Match System')
        
        actGroup = QActionGroup(self)
        actGroup.addAction(self.ui.actWelcome)
        actGroup.addAction(self.ui.actImport)
        actGroup.addAction(self.ui.actSetWeight1)
        actGroup.addAction(self.ui.actCompare1)
        actGroup.addAction(self.ui.actResult1)
        actGroup.addAction(self.ui.actSetTarget)
        actGroup.addAction(self.ui.actSetWeight2)
        actGroup.addAction(self.ui.actCompare2)
        actGroup.addAction(self.ui.actResult2)
        actGroup.setExclusive(True)
        
        self.ui.actSetTarget.setVisible(False)
        self.ui.actSetWeight2.setVisible(False)
        self.ui.actCompare2.setVisible(False)
        self.ui.actResult2.setVisible(False)

        self.__formWelcome()
        self.__formImport()
        self.__formSetWeight1()
        self.__formCompare1()
        self.__formResult1()
        self.__formSetTarget()
        self.__formSetWeight2()
        self.__formCompare2()
        self.__formResult2()
        self.on_actWelcome_triggered()
        self.ui.actWelcome.setChecked(True)
        self.__mode = 'Similarity'
        self.__buildStatusBar()     
        # self.setWindowState(Qt.WindowMaximized)
        # self.setAutoFillBackground(True)
        
        
    def __buildStatusBar(self):
        # self.ui.statusbar.showMessage('')
        if self.__mode == 'Similarity':
            self.ui.statusbar.showMessage('  Mode: Matching based on similarity.')
        else:
            self.ui.statusbar.showMessage('  Mode: Matching based on target set.')
        
        
    def __formWelcome(self):
        formWelcome = QmyFormWelcome(self)
        formWelcome.getStarted.connect(self.on_actImport_triggered)
        self.stack.addWidget(formWelcome)
        
        # palette = QPalette()
        # pix = QPixmap(":/icons/images/V60/V60_background.png")
        # pix = pix.scaled(formWelcome.width(), formWelcome.height())
        # palette.setBrush(QPalette.Background, QBrush(pix))
        # self.ui.centralwidget.setPalette(palette)

    def __formImport(self):
        formImport = QmyFormImport(self)
        formImport.listWidgetChanged.connect(self.__do_listWidgetChanged)
        formImport.storeDirChanged.connect(self.__do_storeDirChanged)
        self.stack.addWidget(formImport)
        
    def __formSetWeight1(self):
        self.__formSetWeight1 = QmyFormSetWeight1(self)
        self.stack.addWidget(self.__formSetWeight1)
        
    def __formCompare1(self):
        self.__formCompare1 = QmyFormCompare1(self)
        self.__formCompare1.seeResult.connect(self.on_actResult1_triggered)
        self.__formCompare1.resultChanged.connect(self.__do_result1Changed)
        self.stack.addWidget(self.__formCompare1)
        
    def __formResult1(self):
        self.__formResult1 = QmyFormResult1(self)
        self.stack.addWidget(self.__formResult1)
        
    def __formSetTarget(self):
        self.__formSetTarget = QmyFormSetTarget(self)
        self.stack.addWidget(self.__formSetTarget)
        
    def __formSetWeight2(self):
        self.__formSetWeight2 = QmyFormSetWeight2(self)
        self.stack.addWidget(self.__formSetWeight2)
        
    def __formCompare2(self):
        self.__formCompare2 = QmyFormCompare2(self)
        self.__formCompare2.seeResult.connect(self.on_actResult2_triggered)
        self.__formCompare2.resultChanged.connect(self.__do_result2Changed)
        self.stack.addWidget(self.__formCompare2)
        
    def __formResult2(self):
        self.__formResult2 = QmyFormResult2(self)
        self.stack.addWidget(self.__formResult2)
        
##  ====================Customised Functional Functions=======================
        

        
##  =====================Event Processing Functions===========================
    # def paintEvent(self,event):
    #     painter = QPainter(self)
    #     pic = QPixmap(":/icons/images/V60/V60_background.png")
    #     painter.drawPixmap(self.ui.toolBar.width(),0, self.width()-self.ui.toolBar.width(),
    #     self.height()-self.ui.statusbar.height(),
    #     pic)
    #     super().paintEvent(event)
    
    # def resizeEvent(self, event):
    #     w = self.width()
    #     h = self.height()
    #     wtb = self.ui.toolBar.width()
    #     htb = self.ui.toolBar.height()
    #     self.ui.toolBar.setGeometry(0, 0, int(165/1600*w), htb)
    
        
##  ================ Slot Functions by connectSlotsByName()===================
    @pyqtSlot()
    def on_actWelcome_triggered(self):
        self.stack.setCurrentIndex(0)
            
    @pyqtSlot()
    def on_actImport_triggered(self):
        self.ui.actImport.setChecked(True)
        self.stack.setCurrentIndex(1)
            
    @pyqtSlot()
    def on_actSetWeight1_triggered(self):
        self.ui.actSetWeight1.setChecked(True)
        self.stack.setCurrentIndex(2)
        
    @pyqtSlot()
    def on_actCompare1_triggered(self):
        self.__formCompare1.weight = self.__formSetWeight1.wt_customised
        self.stack.setCurrentIndex(3)
        
    @pyqtSlot()
    def on_actResult1_triggered(self):
        self.ui.actResult1.setChecked(True)
        self.stack.setCurrentIndex(4)
        
    @pyqtSlot()
    def on_actSetTarget_triggered(self):
        self.ui.actSetTarget.setChecked(True)
        self.stack.setCurrentIndex(5)
        
    @pyqtSlot()
    def on_actSetWeight2_triggered(self):
        self.ui.actSetWeight2.setChecked(True)
        self.stack.setCurrentIndex(6)
        
    @pyqtSlot()
    def on_actCompare2_triggered(self):
        self.__formCompare2.weightF = self.__formSetWeight2.wt_customisedF
        self.__formCompare2.weightR = self.__formSetWeight2.wt_customisedR
        self.__formCompare2.targetF = self.__formSetTarget.target_customisedF
        self.__formCompare2.targetR = self.__formSetTarget.target_customisedR
        self.stack.setCurrentIndex(7)
        
    @pyqtSlot()
    def on_actResult2_triggered(self):
        self.ui.actResult2.setChecked(True)
        self.stack.setCurrentIndex(8)
        
    @pyqtSlot()
    def on_actMode_triggered(self):
        if self.__mode == 'Similarity':
            self.__mode = 'Reliability'
            self.on_actSetTarget_triggered()
            self.ui.actSetTarget.setVisible(True)
            self.ui.actSetWeight1.setVisible(False)
            self.ui.actSetWeight2.setVisible(True)
            self.ui.actCompare1.setVisible(False)
            self.ui.actCompare2.setVisible(True)
            self.ui.actResult1.setVisible(False)
            self.ui.actResult2.setVisible(True)
            self.ui.actMode.setText('Similarity')
        else:
            self.__mode = 'Similarity'
            self.on_actSetWeight1_triggered()
            self.ui.actSetTarget.setVisible(False)
            self.ui.actSetWeight1.setVisible(True)
            self.ui.actSetWeight2.setVisible(False)
            self.ui.actCompare1.setVisible(True)
            self.ui.actCompare2.setVisible(False)
            self.ui.actResult1.setVisible(True)
            self.ui.actResult2.setVisible(False)
            self.ui.actMode.setText('Reliability')
        self.__buildStatusBar()
        
    
##  ====================Customised Slot Functions=============================
    @pyqtSlot(QListWidget)
    def __do_listWidgetChanged(self, listWidget):
        self.__formCompare1.init_ui()
        self.__formCompare2.init_ui()
        # copy the listWidget from formImport to formCompare
        count = listWidget.count()
        for i in range(count):
            veh = QListWidgetItem()
            veh.setText(listWidget.item(i).text())
            # veh.setData(Qt.UserRole,vehicles.item(i).data(Qt.UserRole))
            veh.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            veh.setCheckState(Qt.Unchecked)
            self.__formCompare1.ui.lw_all.addItem(veh)
            
            # repeat for Reliability mode
            veh = QListWidgetItem()
            veh.setText(listWidget.item(i).text())
            # veh.setData(Qt.UserRole,vehicles.item(i).data(Qt.UserRole))
            veh.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            veh.setCheckState(Qt.Unchecked)
            self.__formCompare2.ui.lw_all.addItem(veh)
            
            
    @pyqtSlot(str)
    def __do_storeDirChanged(self, storeDir):
        self.__formCompare1.storeDir = storeDir
        self.__formCompare2.storeDir = storeDir
        
        
    @pyqtSlot(pd.DataFrame, dict, str)
    def __do_result1Changed(self, df, allSimi, target_veh):
        self.__formResult1.result = df
        self.__formResult1.target_veh = target_veh
        self.__formResult1.allSimi = allSimi
        self.__formResult1.drawFigure()
        
    @pyqtSlot(pd.DataFrame, dict, dict)
    def __do_result2Changed(self, df, allRb_F, allRb_R):
        self.__formResult2.result = df
        self.__formResult2.allRb_F = allRb_F
        self.__formResult2.allRb_R = allRb_R
        self.__formResult2.drawFigure()
            
       
   
##  =========================== UI testing ===================================
if  __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
