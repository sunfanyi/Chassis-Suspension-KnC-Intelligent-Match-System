# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 09:48:50 2021

@author: Fanyi Sun
"""

import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget, QListWidgetItem,
                             QStackedWidget, QMenuBar, QHBoxLayout, QVBoxLayout)
                          
from PyQt5.QtCore import QSize, Qt, pyqtSlot

from ui_QWFormSetTarget import Ui_QWFormSetTarget
from myFormTargetItem import QmyFormTargetItem

from qss import QSS

sys.path.append('..\\target_evaluation')
from target_setting import FrontTarget, RearTarget

        
class QmyFormSetTarget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormSetTarget()
        self.ui.setupUi(self)
        # self.ui.clear()

        self.target_defaultF = FrontTarget()
        self.target_defaultR = RearTarget()
        self.target_customisedF = FrontTarget()
        self.target_customisedR = RearTarget()
        
        self.__buildUI()
        self.__setLayout()
        
        qss = QSS()
        self.setStyleSheet(qss.menubar)
        self.listWidget.setStyleSheet(qss.target_listWidget)
        
        
##  ====================Customised Functional Functions=======================
    def __buildUI(self):
        # Using Actions from UI to create the menubar
        self.locMenuBar = QMenuBar()
        
        self.locMenuBar.addAction(self.ui.actImport)
        self.locMenuBar.addAction(self.ui.actSave)
        self.locMenuBar.addAction(self.ui.actSeparator1)
        self.locMenuBar.addAction(self.ui.actResetAll)
        self.locMenuBar.addAction(self.ui.actResetLoc)
        self.ui.actResetAll.setEnabled(False)
        self.ui.actResetLoc.setEnabled(False)
        self.locMenuBar.addAction(self.ui.actSeparator2)
        self.locMenuBar.addAction(self.ui.actUndo)
        self.locMenuBar.addAction(self.ui.actRedo)
        self.locMenuBar.addAction(self.ui.actSeparator3)
        
        
    def __setLayout(self):
        self.listWidget = QListWidget()
        self.stackWidget = QStackedWidget()
        
        paras = ['toe_in', 'static_camber',
                 
                 'drive_toe_in', 'brake_toe_in', 'caster_comp', 'anti_lift', 
                 'anti_dive', 'anti_squat',
                 
                 'camber_comp', 'lat_stif', 'lat_F', 'lat_F_delta',
                 
                 'bump_camber', 'bump_understeer', 'wheel_travel',
                 
                 'caster', 'kpi', 'kpo', 'scrub_r', 'ackermann',
                 
                 'static_rch', 'static_rch_diff', 'roll_bump']
        
        
        names = [' Static toe-in', ' Static Camber',
                 
                 ' Drive Force toe-in', ' Brake Force toe-in', ' Caster Compliance',
                 ' Anti-Lift', ' Anti-Dive', ' Anti-Squat',
                 
                 ' Camber Compliance', ' Lateral Stiffness CP',
                 ' Lateral Forve Understeer @-30 mm offset',
                 ' Lateral Forve Understeer Delta',
                 
                 ' Bump Camber', ' Bump Understeer',
                 ' Wheel Travel(et_ref) at 3.8g jounce',
                 
                 ' Static Caster', ' Kingpin Inclination', ' Kingpin Offset',
                 ' Scrub Radius', ' Ackermann',
                 
                 ' Static RCH Flexible Tire', 
                 ' Static RCH Difference Rear/Front', 
                 ' Added Understeer at Roll vs Bump']

        for para, name in zip(paras, names):
            self.item = QListWidgetItem(name, self.listWidget)
            self.item.setSizeHint(QSize(10,40))
            self.item.setTextAlignment(Qt.AlignLeft)
            if para == 'toe_in':
                self.item.setSelected(True)
            
            try:
                targetF = eval("self.target_customisedF.%s" % para)
            except AttributeError:
                targetF = None
            try:
                targetR = eval("self.target_customisedR.%s" % para)
            except AttributeError:
                targetR = None
            stackwg_item = QmyFormTargetItem()
            stackwg_item.format_widget(para, targetF, targetR)
            stackwg_item.targetFChanged.connect(self.__do_targetFChanged)
            stackwg_item.targetRChanged.connect(self.__do_targetRChanged)
            self.stackWidget.addWidget(stackwg_item)
        self.stackWidget.setCurrentIndex(0)
        
        
        Layout = QVBoxLayout(spacing=10)
        Layout.setContentsMargins(0,0,0,0)
        
        main_Hlayout = QHBoxLayout(spacing=0)
        main_Hlayout.setContentsMargins(0,0,0,0)
        # self.listWidget.setFrameShape(QListWidget.NoFrame)    # remove frame
        # self.listWidget.setWidth(1000)
        # create a tab widget by adding a listWidget and a stackWidget
        main_Hlayout.addWidget(self.listWidget)
        self.stackWidget.setVisible(True)
        main_Hlayout.addWidget(self.stackWidget)
        
        main_Hwg = QWidget()
        main_Hwg.setLayout(main_Hlayout)
        
        Layout.addWidget(self.locMenuBar)
        Layout.addWidget(main_Hwg)
        
        self.setLayout(Layout)
        
        # connect the left listwidget and the right stackwidget
        self.listWidget.currentRowChanged.connect(self.stackWidget.setCurrentIndex)
        

##  ====================Customised Slot Functions=============================
    @pyqtSlot(str, dict)
    def __do_targetFChanged(self, para, targetF):
        exec(f"{'self.target_customisedF.%s' % para} = targetF")
        # print(self.target_customisedF)
        
        
    @pyqtSlot(str, dict)
    def __do_targetRChanged(self, para, targetR):
        exec(f"{'self.target_customisedR.%s' % para} = targetR")
        # print(self.target_customisedR)
        
        
        
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyFormSetTarget()
    form.show()
    sys.exit(app.exec_())