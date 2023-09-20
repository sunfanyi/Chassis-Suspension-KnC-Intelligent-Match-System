# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:37:04 2021

@author: Fanyi Sun
"""


import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import (FigureCanvas,
                 NavigationToolbar2QT as NaviToolbar)

from PyQt5.QtWidgets import  (QApplication, QWidget, QMainWindow, QHBoxLayout,
                              QVBoxLayout, QTreeWidgetItem, QStyleFactory, QSpacerItem)

from PyQt5.QtCore import  pyqtSlot, Qt

from ui_QWFormResult2 import Ui_QWFormResult2

from qss import QSS


class QmyFormResult2(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormResult2()
        self.ui.setupUi(self)
        
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.unicode_minus'] = False
        
        self.__buildUI()
        
        self.result = None
        self.drawFigure()
        
        self.ui.Rb_F.setEnabled(False)
        self.ui.Rb_R.setEnabled(False)
        
        qss = QSS()
        self.ui.tabWidget.setStyleSheet(qss.tab)
        

    def __buildUI(self):
        self.__fig1 = plt.figure(figsize=(15, 5), dpi=80)
        self.__fig2 = plt.figure(figsize=(13, 5), dpi=80)
        # self.__fig = plt.figure()
        
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
        hlayout = QHBoxLayout()
        
        hlayout.addWidget(self.ui.label)
        hlayout.addWidget(self.ui.Rb_F)
        spacer = QSpacerItem(10,10)
        hlayout.addItem(spacer)
        hlayout.addWidget(self.ui.label_2)
        hlayout.addWidget(self.ui.Rb_R)
        hlayout.setAlignment(Qt.AlignLeft)
        hwg = QWidget()
        hwg.setLayout(hlayout)
        
        vlayout.addWidget(self.ui.lineEdit)
        vlayout.addWidget(hwg)
        vlayout.addWidget(self.ui.tabWidget)
        vlayout.addWidget(figCanvas2)
        # vlayout.setVerticalSpacing(0)
        vlayout.setContentsMargins(0,0,0,0)
        vwg = QWidget()
        vwg.setLayout(vlayout)

        Hlayout.addWidget(figCanvas1)
        Hlayout.addWidget(vwg)
        widget.setLayout(Hlayout)
        
        self.setCentralWidget(widget)
        self.ui.lineEdit.setText('Select a vehicle to see more details...')
        self.__cid1 = figCanvas1.mpl_connect("button_press_event",
                                            self.do_button_press)
        
        self.ui.tree_overall.header().resizeSection(0,180)
        self.ui.tree_overall.header().resizeSection(1,150)
        self.ui.tree_overall.header().resizeSection(2,150)
        
        self.ui.tree_general.header().resizeSection(0,180)
        self.ui.tree_general.header().resizeSection(1,150)
        self.ui.tree_general.header().resizeSection(2,150)
        
        self.ui.tree_longi.header().resizeSection(0,220)
        self.ui.tree_longi.header().resizeSection(1,150)
        self.ui.tree_longi.header().resizeSection(2,150)
        
        self.ui.tree_lateral.header().resizeSection(0,350)
        self.ui.tree_lateral.header().resizeSection(1,150)
        self.ui.tree_lateral.header().resizeSection(2,150)
        
        self.ui.tree_vertical.header().resizeSection(0,340)
        self.ui.tree_vertical.header().resizeSection(1,150)
        self.ui.tree_vertical.header().resizeSection(2,150)
        
        self.ui.tree_steer.header().resizeSection(0,220)
        self.ui.tree_steer.header().resizeSection(1,150)
        self.ui.tree_steer.header().resizeSection(2,150)
        
        self.ui.tree_roll.header().resizeSection(0,340)
        self.ui.tree_roll.header().resizeSection(1,150)
        self.ui.tree_roll.header().resizeSection(2,150)
        
        
##  ====================Customised Functional Functions=======================
    def drawFigure(self):
        if self.result is not None:
            try:
                self.__ax1.clear()
                self.__ax1.set_xticks([])
                self.__ax1.set_yticks([])
            except AttributeError:
                pass
            print('result',self.result)
            # use my own axes class
            mpl.projections.register_projection(My_Axes)
            self.__ax1 = self.__fig1.add_subplot(111, projection="my_axes")
            
            # display only the top 20 vehicles for better performance
            self.__veh_identites = self.result['VEHICLES'][:20]
            self.__veh_names = [a.rpartition('#')[0] for a in self.__veh_identites]
            self.__overall_rb = self.result['OVERALL'][:20]
            
            self.__ax1.bar(self.__veh_names, self.__overall_rb, color='blue')
            
            # value over the bar
            for i, simi in enumerate(self.__overall_rb):
                self.__ax1.text(i, simi+2,'%.2f' % simi,ha='center')
                
            self.__ax1.set_xlabel('Vehicles',fontsize=18)
            self.__ax1.set_ylabel('Overall Reliability',fontsize=18)
            self.__fig1.autofmt_xdate(rotation=20)
            self.__ax1.set_xlim([-1,10])
            self.__fig1.canvas.draw()     
    
    
    def __drawSubFigure(self, testRb_F, testRb_R):
        try:
            self.__ax2.clear()
            self.__ax2.set_xticks([])
            self.__ax2.set_yticks([])
        except AttributeError:
            pass
        
        self.__ax2 = self.__fig2.add_subplot(111)
        
        x = list(testRb_F.keys())
        y1 = list(testRb_F.values())
        y2 = list(testRb_R.values())
        
        y1 = [float('%.2f' % (i*100)) for i in y1]
        y2 = [float('%.2f' % (i*100)) for i in y2]
        y2.insert(-1,np.nan) # no steering data for rear suspension
        
        p1 = self.__ax2.barh(x, y1, color='blue',label='Front')
        p2 = self.__ax2.barh(x, y2, left=y1, color='green',label='Rear')
        
        self.__ax2.set_xlabel('Similarity (%)',fontsize=18)
        # self.__ax2.set_ylabel('Tests',fontsize=18)
        self.__ax2.set_xlim([0,200])
        self.__ax2.set_ylim([-0.5,6.2])
        self.__ax2.bar_label(p1, label_type='center',color='yellow',fontsize=14)
        self.__ax2.bar_label(p2, label_type='center',color='yellow',fontsize=14)
        # self.__fig2.tight_layout()
        self.__ax2.legend(loc='upper center', ncol=4)
        self.__fig2.subplots_adjust(left=0.18, right=0.95, top=0.95, bottom=0.2)
        self.__fig2.canvas.draw()  
        
    
    def __fill_TabWidget(self, paraRb_F, paraRb_R, testRb_F, testRb_R, 
                         vehRb_F, vehRb_R):
        self.ui.tree_overall.clear()
        # write the reliability of the front and rear suspension
        self.ui.Rb_F.setText('%.1f' % vehRb_F)
        self.ui.Rb_R.setText('%.1f' % vehRb_R)
        
        # ================== overall ======================= 
        
        tests = ['general', 'longitudinal', 'lateral', 'vertical', 'steer', 
                  'roll']
        names = ['General', 'Longitudinal', 'Lateral', 'Vertical', 'Steer', 
                  'Roll']
        excludeF = []
        excludeR = ['Steer']
        for test, name in zip(tests, names):
            item = self.__get_treeWidget_item(testRb_F, testRb_R, test, name, 
                                              excludeF, excludeR)
            self.ui.tree_overall.addTopLevelItem(item)
        # connected by dashed line
        self.ui.tree_overall.setStyle(QStyleFactory.create('windows'))
        
        # ================== General ======================= 
        self.ui.tree_general.clear()
        paras = ['toe_in', 'static_camber']
        names = ['Static toe-in', 'Static Camber']
        excludeF, excludeR = [], []
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(paraRb_F, paraRb_R, para, name, 
                                              excludeF, excludeR)
            self.ui.tree_general.addTopLevelItem(item)
        self.ui.tree_general.setStyle(QStyleFactory.create('windows'))
        
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
            item = self.__get_treeWidget_item(paraRb_F, paraRb_R, para, name, 
                                              excludeF, excludeR)
            self.ui.tree_longi.addTopLevelItem(item)
        self.ui.tree_longi.setStyle(QStyleFactory.create('windows'))
        
        # ================== Lateral ======================= 
        self.ui.tree_lateral.clear()
        paras = ['camber_comp', 'lat_stif', 'lat_F', 'lat_F_delta']
        names = ['Camber Compliance', 'Lateral Stiffness CP',
                 'Lateral Forve Understeer @-30 mm offset',
                 'Lateral Forve Understeer Delta']
        excludeF, excludeR = [], []
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(paraRb_F, paraRb_R, para, name, 
                                              excludeF, excludeR)
            self.ui.tree_lateral.addTopLevelItem(item)
        self.ui.tree_lateral.setStyle(QStyleFactory.create('windows'))
        
        # ================== Vertical ======================= 
        self.ui.tree_vertical.clear()
        paras = ['bump_camber', 'bump_understeer', 'wheel_travel']
        names = ['Bump Camber', 'bump Understeer',
                 'Wheel Travel(et_ref) at 3.8g jounce']
        excludeF = []
        excludeR = ['Wheel Travel(et_ref) at 3.8g jounce']
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(paraRb_F, paraRb_R, para, name, 
                                              excludeF, excludeR)
            self.ui.tree_vertical.addTopLevelItem(item)
        self.ui.tree_vertical.setStyle(QStyleFactory.create('windows'))
        
        # ================== Steer ======================= 
        self.ui.tree_steer.clear()
        paras = ['caster', 'kpi', 'kpo', 'scrub_r', 'ackermann']
        names = ['Static Caster', 'Kingpin Inclination', 'Kongpin Offset',
                 'Scrub Radius', 'Ackermann']
        excludeF = []
        excludeR = ['Static Caster', 'Kingpin Inclination', 'Kongpin Offset',
                    'Scrub Radius', 'Ackermann']
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(paraRb_F, paraRb_R, para, name, 
                                              excludeF, excludeR)
            self.ui.tree_steer.addTopLevelItem(item)
        self.ui.tree_steer.setStyle(QStyleFactory.create('windows'))
        
        # ================== Roll ======================= 
        self.ui.tree_roll.clear()
        paras = ['static_rch', 'static_rch_diff', 'roll_bump']
        names = ['Static RCH Flexible Tire', 
                 'Static RCH Difference Rear/Front', 
                 'Added Understeer at Roll vs Bump']
        excludeF = ['Static RCH Difference Rear/Front']
        excludeR = []
        for para, name in zip(paras, names):
            item = self.__get_treeWidget_item(paraRb_F, paraRb_R, para, name, 
                                              excludeF, excludeR)
            self.ui.tree_roll.addTopLevelItem(item)
        self.ui.tree_roll.setStyle(QStyleFactory.create('windows'))
        
        
    def __get_treeWidget_item(self, paraRb_F, paraRb_R, para, name, 
                              excludeF, excludeR):
        '''
        This function create a treeWidget item, containing the information
        of the parameter and weights for front and rear suspensions.
        excledeF is a list including the parameters that are not applicable 
        for the front suspension.
        '''
        item = QTreeWidgetItem()
        item.setText(0,name)
        
        if name not in excludeF:
            Rb_F = paraRb_F[para]
            if np.isnan(Rb_F):
                item.setText(1,'None')
            else:
                item.setText(1,'%.2f'%(Rb_F*100))
        else:
            item.setText(1,'  /')
            
        if name not in excludeR:
            Rb_R = paraRb_R[para]
            if np.isnan(Rb_R):
                item.setText(2,'None')
            else:
                item.setText(2,'%.2f'%(Rb_R*100))
        else:
            item.setText(2,'  /')
        return item
    
    
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
            self.simi = self.__overall_rb[self.index+1]
            
            # mark the selected as red
            self.__ax1.bar(self.index, self.simi, color='red')
            self.__fig1.canvas.draw()
            
            self.ui.lineEdit.setText(veh_identity)
            
            # only the selected vehicle is interested
            paraRb_F = self.allRb_F['paraRb'][veh_identity]
            paraRb_R = self.allRb_R['paraRb'][veh_identity]
            testRb_F = self.allRb_F['testRb'][veh_identity]
            testRb_R = self.allRb_R['testRb'][veh_identity]
            vehRb_F = self.allRb_F['vehRb'][veh_identity]
            vehRb_R = self.allRb_R['vehRb'][veh_identity]
            self.__fill_TabWidget(paraRb_F, paraRb_R, testRb_F, testRb_R, 
                                  vehRb_F, vehRb_R)
            self.__drawSubFigure(testRb_F, testRb_R)
    
    
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
    '''
    create my own axes class with the drag_pan method to always 
    act as though the 'x' key is being pressed so that the x axis stay unmoved
    '''
    name = "my_axes"
    def drag_pan(self, button, key, x, y):
        mpl.axes.Axes.drag_pan(self, button, 'x', x, y) # x unmoved


##  =========================== UI testing ===================================      
if  __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = QmyFormResult2()
    # form.target_veh = target_veh
    form.result = df_ranking
    form.allRb_F = allRb_F
    form.allRb_R = allRb_R
    form.drawFigure()
    form.show()
    sys.exit(app.exec_())