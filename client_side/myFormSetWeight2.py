# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:55:52 2021

@author: Fanyi Sun
"""

import sys
import copy

from PyQt5.QtWidgets import (QApplication, QWidget, QTreeWidgetItem, 
                             QHBoxLayout, QVBoxLayout, QItemDelegate, 
                             QStyleFactory, QMessageBox, QMenuBar, QSpacerItem)

from PyQt5.QtCore import pyqtSlot, Qt

from ui_QWFormSetWeight2 import Ui_QWFormSetWeight2

from qss import QSS

sys.path.append('..\\target_evaluation')
from weight_setting2 import FrontWeight, RearWeight


class QmyFormSetWeight2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormSetWeight2()
        self.ui.setupUi(self)
        
        self.wt_customisedF = FrontWeight()
        self.wt_customisedR = RearWeight()
        self.wt_defaultF = FrontWeight()
        self.wt_defaultR = RearWeight()
        self.__FlagEditable = (Qt.ItemIsSelectable | Qt.ItemIsEditable
                               | Qt.ItemIsEnabled)
        self.__FlagNotEditable = (Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.__buildUI()  # build toolbar
        self.setAutoFillBackground(True)
        self.__setweight(self.wt_customisedF, self.wt_customisedR)
        self.ui.weightF.editingFinished.connect(self.onWeightFChanged)
        self.ui.weightR.editingFinished.connect(self.onWeightRChanged)
        
        qss = QSS()
        self.ui.tabWidget.setStyleSheet(qss.tab)
        self.setStyleSheet(qss.menubar)
                           
    
    def __buildUI(self):
        # Using Actions from UI to create the menubar
        locMenuBar = QMenuBar(self)
        
        locMenuBar.addAction(self.ui.actImport)
        locMenuBar.addAction(self.ui.actSave)
        locMenuBar.addAction(self.ui.actSeparator1)
        locMenuBar.addAction(self.ui.actResetAll)
        locMenuBar.addAction(self.ui.actResetLoc)
        self.ui.actResetAll.setEnabled(False)
        self.ui.actResetLoc.setEnabled(False)
        locMenuBar.addAction(self.ui.actSeparator2)
        locMenuBar.addAction(self.ui.actUndo)
        locMenuBar.addAction(self.ui.actRedo)
        locMenuBar.addAction(self.ui.actSeparator3)
        
        # Layout setting
        hlayout = QHBoxLayout()
        Vlayout = QVBoxLayout()
        
        hlayout.addWidget(self.ui.label)
        spacer = QSpacerItem(5,10)
        hlayout.addItem(spacer)
        hlayout.addWidget(self.ui.weightF)
        spacer = QSpacerItem(50,10)
        hlayout.addItem(spacer)
        hlayout.addWidget(self.ui.label_2)
        spacer = QSpacerItem(5,10)
        hlayout.addItem(spacer)
        hlayout.addWidget(self.ui.weightR)
        hlayout.setAlignment(Qt.AlignLeft)
        
        hwg = QWidget()
        hwg.setLayout(hlayout)
        Vlayout.addWidget(locMenuBar)
        Vlayout.addWidget(hwg)
        Vlayout.addWidget(self.ui.tabWidget)
        self.setLayout(Vlayout)
        
        self.ui.tree_overall.header().resizeSection(0,180)
        self.ui.tree_overall.header().resizeSection(1,130)
        self.ui.tree_overall.header().resizeSection(2,130)
        
        self.ui.tree_general.header().resizeSection(0,180)
        self.ui.tree_general.header().resizeSection(1,130)
        self.ui.tree_general.header().resizeSection(2,130)
        
        self.ui.tree_longi.header().resizeSection(0,220)
        self.ui.tree_longi.header().resizeSection(1,130)
        self.ui.tree_longi.header().resizeSection(2,130)
        
        self.ui.tree_lateral.header().resizeSection(0,400)
        self.ui.tree_lateral.header().resizeSection(1,130)
        self.ui.tree_lateral.header().resizeSection(2,130)
        
        self.ui.tree_vertical.header().resizeSection(0,340)
        self.ui.tree_vertical.header().resizeSection(1,130)
        self.ui.tree_vertical.header().resizeSection(2,130)
        
        self.ui.tree_steer.header().resizeSection(0,220)
        self.ui.tree_steer.header().resizeSection(1,130)
        self.ui.tree_steer.header().resizeSection(2,130)
        
        self.ui.tree_roll.header().resizeSection(0,340)
        self.ui.tree_roll.header().resizeSection(1,130)
        self.ui.tree_roll.header().resizeSection(2,130)
        
        
        
##  ====================Customised Functional Functions=======================
    def __setweight(self, wt_customisedF, wt_customisedR):
        self.__isPageChanged = [False] * 7
        self.__wtF = wt_customisedF.front
        self.__wtR = wt_customisedR.rear
        self.ui.weightF.setText('%.1f'%(self.__wtF*100))
        self.ui.weightR.setText('%.1f'%(self.__wtR*100))
        
        # ================== overall ======================= 
        self.ui.tree_overall.clear()
        tests = ['general', 'longitudinal', 'lateral', 'vertical', 'steer', 
                 'roll']
        names = ['General', 'Longitudinal', 'Lateral', 'Vertical', 'Steer', 
                 'Roll']
        excludeF = []
        excludeR = ['Steer']
        for test, name in zip(tests, names):
            item = self.__get_treeWidget_item(wt_customisedF, wt_customisedR, 
                                              test, name, excludeF, excludeR)
            self.ui.tree_overall.addTopLevelItem(item)
        # first column not editable
        self.ui.tree_overall.setItemDelegateForColumn(0,EmptyDelegate(self))
        # connected by dashed line
        self.ui.tree_overall.setStyle(QStyleFactory.create('windows'))
        self.ui.tree_overall.itemChanged.connect(self.onItemChanged)
        
        # ================== General ======================= 
        self.ui.tree_general.clear()
        paras = ['toe_in', 'static_camber']
        names = ['Static toe-in', 'Static Camber']
        excludeF, excludeR = [], []
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(wt_customisedF, wt_customisedR, 
                                              para, name, excludeF, excludeR)
            self.ui.tree_general.addTopLevelItem(item)
        self.ui.tree_general.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.ui.tree_general.setStyle(QStyleFactory.create('windows'))
        self.ui.tree_general.itemChanged.connect(self.onItemChanged)
        
        # ================== Longitudinal ======================= 
        self.ui.tree_longi.clear()
        paras = ['drive_toe_in', 'brake_toe_in', 'caster_comp', 'anti_lift', 
                 'anti_dive', 'anti_squat', 'anti_lift']
        names = ['Drive Force toe-in', 'Brake Force toe-in', 'Caster Compliance',
                 'Anti-Lift Front', 'Anti-Dive Front', 'Anti-Squat Rear',
                 'Anti-Lift Rear']
        excludeF = ['Anti-Squat Rear', 'Anti-Lift Rear']
        excludeR = ['Anti-Lift Front', 'Anti-Dive Front']
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(wt_customisedF, wt_customisedR, 
                                              para, name, excludeF, excludeR)
            self.ui.tree_longi.addTopLevelItem(item)
        self.ui.tree_longi.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.ui.tree_longi.setStyle(QStyleFactory.create('windows'))
        self.ui.tree_longi.itemChanged.connect(self.onItemChanged)
        
        # ================== Lateral ======================= 
        self.ui.tree_lateral.clear()
        paras = ['camber_comp', 'lat_stif', 'lat_F', 'lat_F_delta']
        names = ['Camber Compliance', 'Lateral Stiffness CP',
                 'Lateral Forve Understeer @-30 mm offset',
                 'Lateral Forve Understeer Delta']
        excludeF, excludeR = [], []
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(wt_customisedF, wt_customisedR, 
                                              para, name, excludeF, excludeR)
            self.ui.tree_lateral.addTopLevelItem(item)
        self.ui.tree_lateral.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.ui.tree_lateral.setStyle(QStyleFactory.create('windows'))
        self.ui.tree_lateral.itemChanged.connect(self.onItemChanged)
        
        # ================== Vertical ======================= 
        self.ui.tree_vertical.clear()
        paras = ['bump_camber', 'bump_understeer', 'wheel_travel']
        names = ['Bump Camber', 'Bump Understeer',
                 'Wheel Travel(et_ref) at 3.8g jounce']
        excludeF = []
        excludeR = ['Wheel Travel(et_ref) at 3.8g jounce']
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(wt_customisedF, wt_customisedR, 
                                              para, name, excludeF, excludeR)
            self.ui.tree_vertical.addTopLevelItem(item)
        self.ui.tree_vertical.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.ui.tree_vertical.setStyle(QStyleFactory.create('windows'))
        self.ui.tree_vertical.itemChanged.connect(self.onItemChanged)
        
        # ================== Steer ======================= 
        self.ui.tree_steer.clear()
        paras = ['caster', 'kpi', 'kpo', 'scrub_r', 'ackermann']
        names = ['Static Caster', 'Kingpin Inclination', 'Kingpin Offset',
                 'Scrub Radius', 'Ackermann']
        excludeF = []
        excludeR = ['Static Caster', 'Kingpin Inclination', 'Kingpin Offset',
                    'Scrub Radius', 'Ackermann']
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(wt_customisedF, wt_customisedR, 
                                              para, name, excludeF, excludeR)
            self.ui.tree_steer.addTopLevelItem(item)
        self.ui.tree_steer.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.ui.tree_steer.setStyle(QStyleFactory.create('windows'))
        self.ui.tree_steer.itemChanged.connect(self.onItemChanged)
        
        # ================== Roll ======================= 
        self.ui.tree_roll.clear()
        paras = ['static_rch', 'static_rch_diff', 'roll_bump']
        names = ['Static RCH Flexible Tire', 
                 'Static RCH Difference Rear/Front', 
                 'Added Understeer at Roll vs Bump']
        excludeF = ['Static RCH Difference Rear/Front']
        excludeR = []
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(wt_customisedF, wt_customisedR, 
                                              para, name, excludeF, excludeR)
            self.ui.tree_roll.addTopLevelItem(item)
        self.ui.tree_roll.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.ui.tree_roll.setStyle(QStyleFactory.create('windows'))
        self.ui.tree_roll.itemChanged.connect(self.onItemChanged)
        
        
    def __get_treeWidget_item(self, wt_customisedF, wt_customisedR, 
                              para, name, excludeF, excludeR):
        """
        This function create a treeWidget item, containing the information
        of the parameter and weights for front and rear suspensions.
        excledeF is a list including the parameters that are not applicable 
        for the front suspension.
        """
        item = QTreeWidgetItem()
        item.setText(0,name)
        item.setData(0,Qt.UserRole,para)
        
        if name not in excludeF:
            wt_F = eval("wt_customisedF.%s" % para)
            item.setText(1,'%.2f'%(wt_F*100))
            item.setData(1,Qt.UserRole,'%.2f'%(wt_F*100))
        else:
            item.setText(1,'  /')
            item.setData(1,Qt.UserRole,'  /')
            
        if name not in excludeR:
            wt_R = eval("wt_customisedR.%s" % para)
            item.setText(2,'%.2f'%(wt_R*100))
            item.setData(2,Qt.UserRole,'%.2f'%(wt_R*100))
        else:
            item.setText(2,'  /')
            item.setData(2,Qt.UserRole,'  /')
        item.setFlags(self.__FlagEditable)
        return item
        
    
    def __reassign_weight(self, parameters, excludeF, excludeR):
        """
        This function returns the weight settings of some specific parameters
        to the default value.
        """
        for para in parameters:
            if para not in excludeF:
                default = eval("self.wt_defaultF.%s" % para)
                key = "self.wt_customisedF.%s" % para
                exec(f"{key} = default")
            if para not in excludeR:
                default = eval("self.wt_defaultR.%s" % para)
                key = "self.wt_customisedR.%s" % para
                exec(f"{key} = default")
                
        
##  ================ Slot Functions by connectSlotsByName()===================
    @pyqtSlot()
    def on_actResetAll_triggered(self): 
        """
        initialise all the weights
        """
        dlgTitle = 'Reset All'
        strInfo = 'Confirm to reset weights for all pages?'
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes
                                      | QMessageBox.No | QMessageBox.Cancel,
                                      defaultBtn)
        if result == QMessageBox.Yes:
            self.wt_customisedF = copy.deepcopy(self.wt_defaultF)
            self.wt_customisedR = copy.deepcopy(self.wt_defaultR)
            self.__setweight(self.wt_customisedF, self.wt_customisedR)
            self.__isPageChanged = [False] * 7
            self.ui.actResetAll.setEnabled(False)
            self.ui.actResetLoc.setEnabled(False)
    
    
    @pyqtSlot()
    def on_actResetLoc_triggered(self): 
        """
        initialise weights for current page
        """
        curTabName = self.ui.tabWidget.currentWidget().objectName()
        curTabText = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())
        dlgTitle = 'Reset Current Page'
        strInfo = 'Confirm to reset weights for %s?' % curTabText
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes
                                      | QMessageBox.No | QMessageBox.Cancel,
                                      defaultBtn)
        if result == QMessageBox.Yes:
            if curTabName == 'overall':
                tests = ['general', 'longitudinal', 'lateral', 'vertical', 
                         'steer', 'roll']
                excludeF = []
                excludeR = ['steer']
                self.__reassign_weight(tests, excludeF, excludeR)
                
            elif curTabName == 'general':
                parameters =  ['toe_in', 'static_camber']
                excludeF, excludeR = [], []
                self.__reassign_weight(parameters, excludeF, excludeR)  
                
            elif curTabName == 'longi':
                ''' do the front and rear separately because they have common 
                paramter name (anti_lift) but they are actually different 
                for front and rear, with is misleading'''
                parametersF = ['drive_toe_in', 'brake_toe_in', 'caster_comp',
                              'anti_lift', 'anti_dive']
                excludeF = []
                excludeR = ['drive_toe_in', 'brake_toe_in', 'caster_comp',
                            'anti_lift', 'anti_dive']
                self.__reassign_weight(parametersF, excludeF, excludeR) 
                
                parametersR = ['drive_toe_in', 'brake_toe_in', 'caster_comp',
                               'anti_squat', 'anti_lift']
                excludeF = ['drive_toe_in', 'brake_toe_in', 'caster_comp',
                            'anti_squat', 'anti_lift']
                excludeR = []
                self.__reassign_weight(parametersR, excludeF, excludeR) 
                
            elif curTabName == 'lateral':
                parameters = ['camber_comp', 'lat_stif', 'lat_F', 'lat_F_delta']
                excludeF, excludeR = [], []
                self.__reassign_weight(parameters, excludeF, excludeR) 
                
            elif curTabName == 'vertical':
                parameters = ['bump_camber', 'bump_understeer', 'wheel_travel']
                excludeF = []
                excludeR = ['wheel_travel']
                self.__reassign_weight(parameters, excludeF, excludeR) 
                
            elif curTabName == 'steer':
                parameters = ['caster', 'kpi', 'kpo', 'scrub_r', 'ackermann']
                excludeF = []
                excludeR = ['caster', 'kpi', 'kpo', 'scrub_r', 'ackermann']
                self.__reassign_weight(parameters, excludeF, excludeR)  
                
            elif curTabName == 'roll':
                parameters = ['static_rch', 'static_rch_diff', 'roll_bump']
                excludeF = ['static_rch_diff']
                excludeR = []
                self.__reassign_weight(parameters, excludeF, excludeR)     
                
            self.__setweight(self.wt_customisedF, self.wt_customisedR)
            self.__isPageChanged[self.ui.tabWidget.currentIndex()] = False
            self.ui.actResetLoc.setEnabled(False)
            if not any(self.__isPageChanged):
                self.ui.actResetAll.setEnabled(False)
                
    
    @pyqtSlot(int)
    def on_tabWidget_currentChanged(self, index):
        """
        when the selected tab is changed
        """
        if self.__isPageChanged[index]:
            self.ui.actResetLoc.setEnabled(True)
        else:
            self.ui.actResetLoc.setEnabled(False)
     
    
        
        
        
##  ====================Customised Slot Functions=============================
    def onItemChanged(self, item, col):
        if (item.data(col,Qt.UserRole) == item.text(col) or 
            item.data(col,Qt.UserRole) == item.text(col)): # avoid repetition
            return
        if col != 1 and col != 2: # only the change in weight is interested
            return
        if item.data(col,Qt.UserRole) == '  /':
            item.setText(col,'  /')
            return
        try:
            wt_new = float(item.text(col)) / 100
        except ValueError: # if not a float
            # return to previous value
            item.setText(col,item.data(col,Qt.UserRole))
            return
        else:
            if wt_new > 1:
                item.setText(col,item.data(col,Qt.UserRole))
                return
        self.__isPageChanged[self.ui.tabWidget.currentIndex()] = True
        self.ui.actResetAll.setEnabled(True)
        self.ui.actResetLoc.setEnabled(True)
        wt_index = item.data(0,Qt.UserRole)
        item.setData(col,Qt.UserRole,item.text(col))
        if col == 1:
            key = "self.wt_customisedF.%s" % wt_index
            exec(f"{key} = wt_new")
        elif col == 2:
            key = "self.wt_customisedR.%s" % wt_index
            exec(f"{key} = wt_new")
            

    def onWeightFChanged(self):
        wt_new = self.ui.weightF.text()
        try:
            wt_new = float(wt_new) / 100
        except ValueError: # if not a float
            # return to previous value
            self.ui.weightF.setText('%.1f'%(self.__wtF*100))
            return
        else:
            if wt_new > 1:
                self.ui.weightF.setText('%.1f'%(self.__wtF*100))
                return
        self.__wtF = wt_new
        self.ui.weightF.setText('%.1f'%(self.__wtF*100))
        self.wt_customisedF.front = self.__wtF
        
        self.__wtR = 1 - self.__wtF
        self.ui.weightR.setText('%.1f'%(self.__wtR*100))
        self.wt_customisedR.rear = self.__wtR
        
        if float(self.ui.weightF.text()) / 100 != self.wt_defaultF.front:
            self.ui.actResetAll.setEnabled(True)
            

    def onWeightRChanged(self):
        wt_new = self.ui.weightR.text()
        try:
            wt_new = float(wt_new) / 100
        except ValueError: # if not a float
            # return to previous value
            self.ui.weightR.setText('%.1f'%(self.__wtR*100))
            return
        else:
            if wt_new > 1:
                self.ui.weightR.setText('%.1f'%(self.__wtR*100))
                return
        self.__wtR = wt_new
        self.ui.weightR.setText('%.1f'%(self.__wtR*100))
        self.wt_customisedR.front = self.__wtR
        
        self.__wtF = 1 - self.__wtR
        self.ui.weightF.setText('%.1f'%(self.__wtF*100))
        self.wt_customisedF.rear = self.__wtF
        
        if float(self.ui.weightR.text()) / 100 != self.wt_defaultR.rear:
            self.ui.actResetAll.setEnabled(True)
        
        
        
##  =========================== Customised Class ==============================      
class EmptyDelegate(QItemDelegate):
    def __init__(self,parent):
        super(EmptyDelegate, self).__init__(parent)
    
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


##  =========================== UI testing ===================================      
if  __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = QmyFormSetWeight2()
    form.show()
    sys.exit(app.exec_())