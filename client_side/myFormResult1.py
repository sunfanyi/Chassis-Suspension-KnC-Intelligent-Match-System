# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 14:26:40 2021

@author: Fanyi Sun
"""

import sys
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import (FigureCanvas,
                 NavigationToolbar2QT as NaviToolbar)

from PyQt5.QtWidgets import  (QApplication, QWidget, QMainWindow, QHBoxLayout,
                              QVBoxLayout, QTreeWidgetItem, QStyleFactory)

from PyQt5.QtCore import  pyqtSlot, Qt

# from PyQt5.QtGui import  QIcon

from ui_QWFormResult1 import Ui_QWFormResult1

from qss import QSS

sys.path.append('..')
from match_test_name import *


class QmyFormResult1(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormResult1()
        self.ui.setupUi(self)
        
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.unicode_minus'] = False
        
        self.__buildUI()
        
        self.result = None
        self.drawFigure()
        
        qss = QSS()
        self.ui.tabWidget.setStyleSheet(qss.tab)
        

    def __buildUI(self):
        self.__fig1 = plt.figure(figsize=(15, 5), dpi=80)
        self.__fig2 = plt.figure(figsize=(13, 4.5), dpi=80)
        
        # self.__fig.suptitle(self.target_veh,fontsize=20)
        figCanvas1 = FigureCanvas(self.__fig1)
        figCanvas1.setGeometry(10,10,10,100)
        figCanvas2 = FigureCanvas(self.__fig2)
      
        self.naviToolbar = NaviToolbar(figCanvas1, self)  # build toolbar
        # self.naviToolbar.setMovable(False)
        
        # set customised action
        self.actList = self.naviToolbar.actions()
        self.ui.actSelect.setCheckable(True)
        self.naviToolbar.insertAction(self.actList[4], self.ui.actSelect)
        
        self.actList[4].triggered.connect(self.do_selectPan)
        self.actList[5].triggered.connect(self.do_selectZoom)
        
        self.naviToolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(self.naviToolbar)  # add toolbar to mainwindow
        
        # Layout setting
        widget = QWidget()
        Hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        
        vlayout.addWidget(self.ui.lineEdit)
        vlayout.addWidget(self.ui.tabWidget)
        vlayout.addWidget(figCanvas2)
        
        vwg = QWidget()
        vwg.setLayout(vlayout)
        Hlayout.addWidget(figCanvas1)
        Hlayout.addWidget(vwg)
        widget.setLayout(Hlayout)
        
        # # layout.setContentsMargins(2,2,2,2)
        # # layout.setSpacing(2)
        self.setCentralWidget(widget)
        self.ui.lineEdit.setText('Select a vehicle to see more details...')
        self.__cid1 = figCanvas1.mpl_connect("button_press_event",
                                            self.do_button_press)
        
        
##  ====================Customised Functional Functions=======================
    def drawFigure(self):
        if self.result is not None:
            try:
                self.__ax1.clear()
                self.__ax1.set_xticks([])
                self.__ax1.set_yticks([])
            except AttributeError:
                pass
            title = 'Target vehicle: %s' % self.target_veh
            self.__fig1.suptitle(title, fontsize=20)
            print('result',self.result)
            # use my own axes class
            mpl.projections.register_projection(My_Axes)
            self.__ax1 = self.__fig1.add_subplot(111, projection="my_axes")
            
            # display only the top 20 vehicles for better performance
            self.__veh_identites = self.result['VEHICLES'][:20]
            self.__veh_names = [a.rpartition('#')[0] for a in self.__veh_identites]
            print(self.__veh_identites)
            self.__overall_simi = self.result['OVERALL'][:20]
            
            self.__ax1.bar(self.__veh_names, self.__overall_simi, color='blue')
            
            # value over the bar
            for i, simi in enumerate(self.__overall_simi):
                self.__ax1.text(i, simi+2,'%.2f' % simi,ha='center')
                
            self.__ax1.set_xlabel('Vehicles',fontsize=18)
            self.__ax1.set_ylabel('Overall Similarities',fontsize=18)
            self.__fig1.autofmt_xdate(rotation=20)
            self.__ax1.set_xlim([-1,10])
            self.__fig1.canvas.draw()     
    
    
    def __drawSubFigure(self):
        try:
            self.__ax2.clear()
            self.__ax2.set_xticks([])
            self.__ax2.set_yticks([])
        except AttributeError:
            pass
        
        self.__ax2 = self.__fig2.add_subplot(111)
        p1 = self.__ax2.barh(self.__test_names[::-1], 
                             self.__formated_simis[::-1], color='blue')
        
        self.__ax2.set_xlabel('Similarity (%)',fontsize=18)
        # self.__ax2.set_ylabel('Tests',fontsize=18)
        self.__ax2.set_xlim([0,100])
        self.__ax2.bar_label(p1, label_type='center',color='yellow',fontsize=14)
        # self.__fig2.tight_layout()
        self.__fig2.subplots_adjust(left=0.18, right=0.95, top=0.95, bottom=0.2)
        self.__fig2.canvas.draw()  
        
    
    def __fill_TabWidget(self, testSimi, paraSimi, detailedSimi):
        self.__writeSimi_overall(testSimi)
        
        tests = ['test1', 'test2', 'test3', 'test4', 'test5',
                 'test6', 'test7', 'test8', 'test10', 'strapped']
        for test in tests:
            self.__writeSimi_test(test, paraSimi, detailedSimi)
    
        
    def __writeSimi_overall(self, testSimi):
        self.ui.tree_overall.clear()
        self.__test_names = []
        self.__formated_simis = []
        for test, simi in testSimi.items():
            itemTest = QTreeWidgetItem()

            test_name = get_full_test_name(test).partition('_')[-1]
            self.__test_names.append(get_simp_test_name(test))
            formated_simi = '%.2f'%(simi*100)
            self.__formated_simis.append(float(formated_simi))
            
            itemTest.setText(0,test_name)
            itemTest.setText(1,formated_simi)
            self.ui.tree_overall.addTopLevelItem(itemTest)
        
        self.ui.tree_overall.header().resizeSection(0,350)
        # connected by dashed line
        self.ui.tree_overall.setStyle(QStyleFactory.create('windows'))
        
        
    def __writeSimi_test(self, test, paraSimi, detailedSimi):
        treeWidget = "self.ui.tree_%s" % test
        eval(treeWidget).clear()
        for para, simi in paraSimi[test].items():
            itemPara = QTreeWidgetItem()
            itemPara.setText(0,para)
            if simi is not None:
                itemPara.setText(1,'%.1f' % (simi*100))
            else:
                itemPara.setText(1,'DataMissing')
            for feature, subSimi in detailedSimi[test][para].items():
                itemFeature = QTreeWidgetItem(itemPara)
                itemFeature.setText(0,feature)
                if subSimi is not None:
                    itemFeature.setText(1,'  %.1f'%(subSimi*100))
                else:
                    itemFeature.setText(1,'  Data Missing')
            eval(treeWidget).addTopLevelItem(itemPara)

        eval(treeWidget).header().resizeSection(0, 350)
        # eval(treeWidget).setColumnWidth(0,350) # same effect
        eval(treeWidget).setStyle(QStyleFactory.create('windows'))
        eval(treeWidget).expandAll()
        
    
##  =====================Event Processing Functions===========================
    def do_button_press(self, event):
        if (self.ui.actSelect.isChecked() and event.xdata is not None 
            and event.xdata > -0.5 
            and event.xdata < len(self.__veh_identites) - 0.5):

            try:
                # remove the red marking
                self.__ax1.bar(self.index, self.simi, color='blue')
            except AttributeError:
                pass
            
            self.index = int(event.xdata + 0.5)
            
            veh_identity = self.__veh_identites[self.index+1]
            self.simi = self.__overall_simi[self.index+1]
            
            # mark the selected as red
            self.__ax1.bar(self.index, self.simi, color='red')
            self.__fig1.canvas.draw()
            
            self.ui.lineEdit.setText(veh_identity)
            
            # only the selected vehicle is interested
            testSimi = self.allSimi['testSimi'][veh_identity]
            paraSimi = self.allSimi['paraSimi'][veh_identity]
            detailedSimi = self.allSimi['detailedSimi'][veh_identity]
            self.__fill_TabWidget(testSimi, paraSimi, detailedSimi)
            self.__drawSubFigure()
    
    
##  ================ Slot Functions by connectSlotsByName()===================
    @pyqtSlot()  
    def on_actSelect_triggered(self):
        if self.ui.actSelect.isChecked():
            # disable zoom and pan by emitting a trigger signal
            if self.actList[4].isChecked():
                self.actList[4].triggered.emit()
            if self.actList[5].isChecked():
                self.actList[5].triggered.emit()
                
            '''When a trigger signal is emitted, actSelect will become 
            unchecked again, so the next line make it checked again'''
            self.ui.actSelect.setChecked(True)
            
        if not self.ui.actSelect.isChecked():
            self.ui.actSelect.setChecked(False)
            
            # try:
            #     # remove the red marking
            #     self.__ax1.bar(self.index, self.simi, color='blue')
            # except AttributeError:
            #     pass
            # else:
            #     self.__fig1.canvas.draw()
            
            
            
##  ====================Customised Slot Functions=============================
    @pyqtSlot()
    def do_selectPan(self):
        self.ui.actSelect.setChecked(False) # disable select
        
        
    @pyqtSlot()
    def do_selectZoom(self):
        self.ui.actSelect.setChecked(False) # disable select
        
            




##  =========================== Customised Class ============================== 
class My_Axes(mpl.axes.Axes):
    """
    create my own axes class with the drag_pan method to always 
    act as though the 'x' key is being pressed so that the x axis stay unmoved
    """
    name = 'my_axes'
    def drag_pan(self, button, key, x, y):
        mpl.axes.Axes.drag_pan(self, button, 'x', x, y) # x unmoved


##  =========================== UI testing ===================================      
if  __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = QmyFormResult1()
    form.target_veh = target_veh
    form.result = df_ranking
    form.overallSimi = overallSimi
    form.drawFigure()
    form.show()
    sys.exit(app.exec_())