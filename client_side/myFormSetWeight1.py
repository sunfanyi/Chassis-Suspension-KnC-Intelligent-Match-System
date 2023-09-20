# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:41:18 2021

@author: Fanyi Sun
"""

import sys
import re
import copy

from PyQt5.QtWidgets import (QApplication, QWidget, QTreeWidgetItem, QVBoxLayout,
                             QItemDelegate, QStyleFactory, QMessageBox, QMenuBar)

from PyQt5.QtCore import pyqtSlot, Qt

from ui_QWFormSetWeight1 import Ui_QWFormSetWeight1

from qss import QSS

sys.path.append('..')
from match_test_name import get_full_test_name

sys.path.append('..\\similarity_evaluation')
from weight_setting import Weight


class QmyFormSetWeight1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormSetWeight1()
        self.ui.setupUi(self)
        
        self.wt_customised = Weight()
        self.wt_default = Weight()
        self.__FlagEditable = (Qt.ItemIsSelectable | Qt.ItemIsEditable
                               | Qt.ItemIsEnabled)
        self.__FlagNotEditable = (Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.__buildUI()  # build toolbar
        self.setAutoFillBackground(True)
        self.__setweight(self.wt_customised)
        
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

        Layout = QVBoxLayout()
        Layout.addWidget(locMenuBar)  # vertical layout
        Layout.addWidget(self.ui.tabWidget)
        # Layout.setContentsMargins(2,2,2,2)
        Layout.setSpacing(10)
        self.setLayout(Layout)
        
        
##  ====================Customised Functional Functions=======================
    def __setweight(self, myWeight):
        locWeight = myWeight.wt_overall
        self.__setwt_overall(locWeight)
        self.__tests = ['test1', 'test2', 'test3', 'test4', 'test5',
                        'test6', 'test7', 'test8', 'test10', 'strapped']
        self.__isPageChanged = [False] * (len(self.__tests)+1)
        for test in self.__tests:
            self.__test = test
            locWeight = eval('myWeight.wt_%s' % self.__test)
            self.__setwt_test(locWeight)
        
            
    def __setwt_overall(self, locWeight):
        self.ui.tree_overall.clear()
        for test, wt in locWeight.items():
            itemTest = QTreeWidgetItem()
            # itemTest = QTreeWidgetItem(self.ui.tree_overall) # same
            itemTest.setText(0,test)
            wt_index = ['overall',test]
            itemTest.setData(0,Qt.UserRole,wt_index)
            
            itemTest.setText(1,'%.2f'%(wt*100))
            itemTest.setData(1,Qt.UserRole,'%.2f'%(wt*100))
            self.__add_comments(test, itemTest)
            itemTest.setFlags(self.__FlagEditable)
            self.ui.tree_overall.addTopLevelItem(itemTest)
        
        # first column noneditable
        self.ui.tree_overall.setItemDelegateForColumn(0,EmptyDelegate(self))
        
        self.ui.tree_overall.header().resizeSection(0,160)
        # connected by dashed line
        self.ui.tree_overall.setStyle(QStyleFactory.create('windows'))
        
        self.ui.tree_overall.itemChanged.connect(self.onItemChanged)
        
        
    def __setwt_test(self, locWeight):
        treeWidget = "self.ui.tree_%s" % self.__test
        eval(treeWidget).clear()
        for para, para_info in locWeight.items():
            itemPara = QTreeWidgetItem()
            itemPara.setText(0,para)
            wt_index = [self.__test,para,'weight']
            itemPara.setData(0,Qt.UserRole,wt_index)
            itemPara.setText(1,'%.1f' % (para_info['weight']*100))
            # itemPara.setData(1,Qt.UserRole,'%.1f' % (para_info['weight']*100))
            itemPara.setFlags(self.__FlagEditable)
            curve_interval = {}
            for feature, wt in para_info.items():
                if feature != 'weight':
                    if 'curve' in feature and feature != 'curve':
                        # record and process later
                        curve_interval[feature] = wt
                        continue
                    itemFeature = QTreeWidgetItem(itemPara)
                    itemFeature.setText(0,feature)
                    wt_index = [self.__test,para,feature]
                    itemFeature.setData(0,Qt.UserRole,wt_index)
                    itemFeature.setText(1,'%.1f'%(wt*100))
                    itemFeature.setData(1,Qt.UserRole, '%.1f'%(wt*100))
                    self.__add_comments(feature, itemFeature)
                    if wt != 1:
                        itemFeature.setFlags(self.__FlagEditable)
                    else:
                        itemFeature.setFlags(self.__FlagNotEditable)
            if curve_interval: # add one more sub-node for curve intervals
                wt_total = sum(curve_interval.values())
                itemFeature = QTreeWidgetItem(itemPara)
                itemFeature.setText(0,'curve')
                wt_index = [self.__test,para,'curve',len(curve_interval)]
                itemFeature.setData(0,Qt.UserRole,wt_index)
                itemFeature.setText(1,'%.1f'%(wt_total*100))
                itemFeature.setData(1,Qt.UserRole,'%.1f'%(wt_total*100))
                itemFeature.setFlags(self.__FlagEditable)
                self.__add_comments('curve', itemFeature)
                for interval, wt in curve_interval.items():
                    itemInterval = QTreeWidgetItem(itemFeature)
                    itemInterval.setText(0,interval)
                    # store the weight of the overall curve
                    wt_index = [self.__test,para,'curve',interval,'interval']
                    itemInterval.setData(0,Qt.UserRole,wt_index)
                    itemInterval.setText(1,'%.1f'%(wt/wt_total*100))
                    itemInterval.setData(1,Qt.UserRole,'%.1f'%(wt/wt_total*100))
                    itemInterval.setFlags(self.__FlagEditable)
                    self.__add_comments(interval, itemInterval)
                    
            eval(treeWidget).addTopLevelItem(itemPara)

        eval(treeWidget).setItemDelegateForColumn(0, EmptyDelegate(self))
        eval(treeWidget).header().resizeSection(0, 400)
        eval(treeWidget).setStyle(QStyleFactory.create('windows'))
        eval(treeWidget).expandAll()
        eval(treeWidget).itemChanged.connect(self.onItemChanged)
        

    def __add_comments(self, info, item):
        comment = None
        if info in ['overall','test1', 'test2', 'test3', 'test4', 'test5',
                  'test6', 'test7', 'test8', 'test10', 'strapped']:
            comment = get_full_test_name(info)
            comment = comment.split('_')[-1]
        elif info == 'curve':
            comment = 'separation between curves'
        elif 'curve' in info:
            digit = re.findall('\d+',info)
            if 'above' in info:
                comment = 'curve outside x = ±%s' % digit[0]
            elif '0' in digit:
                comment = 'curve between -%s to %s' % (digit[1],digit[1])
            else:
                comment = 'curve between -%s to -%s & %s to %s' \
                                % (digit[0],digit[1],digit[0],digit[1])
        elif info == 'slope':
            comment = 'slope at x = 0'
        elif 'slope' in info:
            digit = re.findall('\d+',info)
            if 'slope_diff' in info: # slope_diff20
                comment = 'difference between the slopes at x = %s and -%s' % (digit[0],digit[0])
            elif 'diff' in info: # slope20_diff
                comment = 'difference of the slopes between x = ±%s and 0' % digit[0]
            elif 'slope_grad' in info:
                comment = 'the slope gradient (2nd derivative) at x = 0'
            else: # slope2000
                comment = 'slope at x = ±%s' % digit[0]
        elif info == 'y-intercept':
            comment = 'y value at x = 0'
        elif info == 'trend_change_left':
            comment = 'x position where the curve\'s trend starts to change on the left'
        elif info == 'trend_change_right':
            comment = 'x position where the curve\'s trend starts to change on the right'
        elif info == 'max_RCH':
            comment = 'maximum Roll Center Height'
        elif info == 'min_RCH':
            comment = 'minimum Roll Center Height'
        elif info == 'limit':
            comment = 'y value at left and right limit'
        elif 'value' in info:
            digit = re.findall('\d+',info)
            if 'value-' in info:
                comment = 'y value when x = -%s' %digit[0]
            else:
                comment = 'y value when x = %s' %digit[0]
        elif info == 'non-consistence':
            comment = '(Maximum - Minimum)/Mean'
        elif info =='deviation-70':
            comment = 'deviation at x = -70'
        elif 'ychange' in info:
            pos = info.split('_')[1]
            if pos == 'max':
                comment = 'difference of the y values at left and right limitation'
            else:
                comment = 'difference of the y values at %s and -%s of the maximum x'\
                                                        % (pos,pos)
        item.setText(2, comment)
        
        
##  ================ Slot Functions by connectSlotsByName()===================
    @pyqtSlot()
    def on_actResetAll_triggered(self): 
        '''initialise all the weights'''
        dlgTitle = 'Reset All'
        strInfo = 'Confirm to reset weights for all pages?'
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, dlgTitle, strInfo, QMessageBox.Yes
                                      | QMessageBox.No | QMessageBox.Cancel,
                                      defaultBtn)
        if result == QMessageBox.Yes:
            self.wt_customised = copy.deepcopy(self.wt_default)
            self.__setweight(self.wt_customised)
            self.__isPageChanged = [False] * (len(self.__tests)+1)
            self.ui.actResetAll.setEnabled(False)
            self.ui.actResetLoc.setEnabled(False)
    
    
    @pyqtSlot()
    def on_actResetLoc_triggered(self): 
        '''initialise weights for current page'''
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
                default = self.wt_default.wt_overall
                self.wt_customised.wt_overall = copy.deepcopy(default)
                locWeight = self.wt_customised.wt_overall
                self.__setwt_overall(locWeight)
            else:
                self.__test = curTabName
                default = eval("self.wt_default.wt_%s" % self.__test)
                key = "self.wt_customised.wt_%s" % self.__test
                exec(f"{key} = copy.deepcopy(default)")
                locWeight = eval("self.wt_customised.wt_%s" % self.__test)
                self.__setwt_test(locWeight)
            self.__isPageChanged[self.ui.tabWidget.currentIndex()] = False
            self.ui.actResetLoc.setEnabled(False)
            if not any(self.__isPageChanged):
                self.ui.actResetAll.setEnabled(False)
                
    
    @pyqtSlot(int)
    def on_tabWidget_currentChanged(self, index):
        '''when the selected tab is changed'''
        if self.__isPageChanged[index]:
            self.ui.actResetLoc.setEnabled(True)
        else:
            self.ui.actResetLoc.setEnabled(False)
            
##  ====================Customised Slot Functions=============================
    # @pyqtSlot()
    def onItemChanged(self, item, col):
        if item.data(1,Qt.UserRole) == item.text(col): # avoid repetition
            return
        if col != 1: # only the change in weight is interested
            return
        try:
            wt_new = float(item.text(col)) / 100
        except ValueError: # if not a float
            # return to previous value
            item.setText(1,item.data(1,Qt.UserRole))
            return
        else:
            if wt_new > 1:
                item.setText(1,item.data(1,Qt.UserRole))
                return
        self.__isPageChanged[self.ui.tabWidget.currentIndex()] = True
        self.ui.actResetAll.setEnabled(True)
        self.ui.actResetLoc.setEnabled(True)
        wt_index = item.data(0,Qt.UserRole)
        item.setData(1,Qt.UserRole,item.text(col))
        if len(wt_index) == 2:
            key = "self.wt_customised.wt_%s['%s']" % (wt_index[0],wt_index[1])
            exec(f"{key} = wt_new")
        elif len(wt_index) == 3:
            key = "self.wt_customised.wt_%s['%s']['%s']" % \
                                        (wt_index[0],wt_index[1],wt_index[2])
            exec(f"{key} = wt_new")
        else: # curve with interval
            if wt_index[-1] == 'interval':
                # if weight for a particular interval is changed
                key = "self.wt_customised.wt_%s['%s']['%s']" % \
                                        (wt_index[0],wt_index[1],wt_index[3])
                wt_general = float(item.parent().text(1)) / 100
                wt_new = wt_new * wt_general
                exec(f"{key} = wt_new")
            else:
                # if the general weight for the curve is changed
                child_number = wt_index[-1]
                for i in range(child_number):
                    interval = item.child(i).text(0)
                    key = "self.wt_customised.wt_%s['%s']['%s']" % \
                                        (wt_index[0],wt_index[1],interval)
                    wt_interval = float(item.child(i).text(1)) / 100
                    wt_calculated = wt_new * wt_interval
                    exec(f"{key} = wt_calculated")
        # self.statusBar().showMessage(txt)
        
        
        
        
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
    form = QmyFormSetWeight1()
    form.show()
    sys.exit(app.exec_())