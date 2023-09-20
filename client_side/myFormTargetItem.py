# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:26:21 2021

@author: Fanyi Sun
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, 
                             QSpacerItem, QPushButton, QLabel, QLineEdit, 
                             QTreeWidget, QTreeWidgetItem, QInputDialog,
                             QStyleFactory)

from PyQt5.QtCore import Qt, pyqtSignal

from PyQt5.QtGui import QDoubleValidator

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas

from qss import QSS


class QmyFormTargetItem(QWidget):
    targetFChanged = pyqtSignal(str, dict)
    targetRChanged = pyqtSignal(str, dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(spacing=0)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setAlignment(Qt.AlignTop)
        
        qss = QSS()
        self.setStyleSheet(qss.target_item)
        
##  ====================Customised Functional Functions=======================
    def format_widget(self, para, targetF, targetR):
        self.para = para
        self.targetF = targetF
        self.targetR = targetR
        
        if targetF is not None:
            self.__front_suspension()
        if targetR is not None:
            self.__rear_suspension()
        
        self.setLayout(self.layout)
        
        
    def __front_suspension(self):
        self.__labF = QLabel('Front Suspension')
        self.__labTypeF = QLabel('Type:')
        self.__typeF = QLineEdit()
        self.__typeF.setStyleSheet('''
                           	border: 2px groove gray;
                           	border-radius: 14px;
                           	padding: 2px 4px;
                           	color: rgb(0, 0, 0);
                           	border-color: rgb(255, 140 ,0);
                           ''')
        self.__typeF.setText(self.targetF['type'].upper())
        
        self.__labTargetFL = QLabel('Target Left:')
        self.__lineTargetFL = QLineEdit()
        self.__labTargetFR = QLabel('Target Right:')
        self.__lineTargetFR = QLineEdit()
        self.__labCriticalF = QLabel('Critical Value:')
        self.__lineCritical_valueF = QLineEdit()
        self.__labEmptyF = QLabel('          ')
        self.__lineCritical_RbF = QLineEdit()
        
        self.__labLimitFL = QLabel('Limit Left:')
        self.__lineLimitFL = QLineEdit()
        self.__labLimitFR = QLabel('Limit Right:')
        self.__lineLimitFR = QLineEdit()
        
        self.__labAdditionalF = QLabel('Additional Nodes')
        
        self.__btnAddF = QPushButton('Add Nodes')
        self.__btnAddF.clicked.connect(self.add_nodesF)
        self.__btnDelF = QPushButton('Delete')
        self.__btnDelAllF = QPushButton('Delete All')
        self.__treeWidgetF = QTreeWidget()
        self.__treeWidgetF.setHeaderLabels(['Value', 'Reliability (%)'])
        
        info_layout = QHBoxLayout()
        info_layout.setAlignment(Qt.AlignLeft)
        info_layout.addWidget(self.__labF)
        spacer = QSpacerItem(400,10)
        info_layout.addItem(spacer)
        info_layout.addWidget(self.__labTypeF)
        info_layout.addWidget(self.__typeF)
        
        hwg_info = QWidget()
        hwg_info.setLayout(info_layout)
        
        gridF_layout = QGridLayout(self, spacing=5)
        # gridF.setContentsMargins(0,0,0,0)
        str_info = self.__round_number(self.targetF['limit'][0])
        self.__lineLimitFL.setText(str_info)
        self.__lineLimitFL.setValidator(QDoubleValidator(-1e99, 1e99, 3))
        self.__lineLimitFL.editingFinished.connect(self.onLimitFLChanged)
        
        str_info = self.__round_number(self.targetF['limit'][1])
        self.__lineLimitFR.setText(str_info)
        self.__lineLimitFR.setValidator(QDoubleValidator(-1e99, 1e99, 3))
        self.__lineLimitFR.editingFinished.connect(self.onLimitFRChanged)
        if self.targetF['type'] == 'interval':
            str_info = self.__round_number(self.targetF['value'][0])
            self.__lineTargetFL.setText(str_info)
            self.__lineTargetFL.setValidator(QDoubleValidator(-1e99, 1e99, 3))
            self.__lineTargetFL.editingFinished.connect(self.onTargetFLChanged)
            
            str_info = self.__round_number(self.targetF['value'][1])
            self.__lineTargetFR.setText(str_info)
            self.__lineTargetFR.setValidator(QDoubleValidator(-1e99, 1e99, 3))
            self.__lineTargetFR.editingFinished.connect(self.onTargetFRChanged)
            items = [self.__labTargetFL, self.__lineTargetFL, 
                     self.__labTargetFR, self.__lineTargetFR,
                     self.__labLimitFL, self.__lineLimitFL,
                     self.__labLimitFR, self.__lineLimitFR]
        else:
            str_info = self.__round_number(self.targetF['value'][0])
            self.__lineCritical_valueF.setText(str_info)
            self.__lineCritical_valueF.setValidator(QDoubleValidator(-1e99, 1e99, 3))
            self.__lineCritical_valueF.editingFinished.connect(self.onCVFChanged)
            
            self.__lineCritical_RbF.setText(str(int(self.targetF['value'][1]*100))+'%')
            self.__lineCritical_RbF.setValidator(QDoubleValidator(-1e99, 1e99, 1))
            self.__lineCritical_RbF.editingFinished.connect(self.onCRbFChanged)
            items = [self.__labCriticalF, self.__lineCritical_valueF, 
                     self.__labEmptyF, self.__lineCritical_RbF,
                     self.__labLimitFL, self.__lineLimitFL,
                     self.__labLimitFR, self.__lineLimitFR]
        positions = [(i,j) for i in range(4) for j in range(2)]
        for item, pos in zip(items, positions):
            gridF_layout.addWidget(item, *pos)
        
        gridF_layout.addWidget(self.__labAdditionalF,4,0)
        
        # layout for all the widgets for below 'Additional Nodes'
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.__btnAddF)
        btn_layout.addWidget(self.__btnDelF)
        btn_layout.addWidget(self.__btnDelAllF)
        hwg_btn = QWidget()
        hwg_btn.setLayout(btn_layout)
        
        add_layout = QGridLayout()
        add_layout.addWidget(hwg_btn)
        add_layout.addWidget(self.__treeWidgetF)
        gwg_add = QWidget()
        gwg_add.setLayout(add_layout)
        
        gridF_layout.addWidget(gwg_add,5,0,5,3)
        
        gridF_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        gridwg_settingF = QWidget()
        # gridwg_front.setGeometry(130, 30, 30, 30)  
        gridwg_settingF.setLayout(gridF_layout)
        
        mainF_layout = QHBoxLayout()
        mainF_layout.addWidget(gridwg_settingF)
        # self.__fig = plt.figure(figsize=(15, 5), dpi=80)
        self.__figF = plt.figure()
        figCanvas = FigureCanvas(self.__figF)
        self.__get_nodes_front()
        self.__drawFigureF()
        mainF_layout.addWidget(figCanvas)
        hwg_mainF = QWidget()
        hwg_mainF.setLayout(mainF_layout)
        
        self.layout.addWidget(hwg_info)
        self.layout.addWidget(hwg_mainF)
        
        
    def __rear_suspension(self):
        self.__labR = QLabel('Rear Suspension')
        self.__labTypeR = QLabel('Type:')
        self.__typeR = QLineEdit()
        self.__typeR.setStyleSheet('''
                           	border: 2px groove gray;
                           	border-radius: 14px;
                           	padding: 2px 4px;
                           	color: rgb(0, 0, 0);
                           	border-color: rgb(255, 140 ,0);
                               ''')
        self.__typeR.setText(self.targetR['type'].upper())
        
        self.__labTargetRL = QLabel('Target Left:')
        self.__lineTargetRL = QLineEdit()
        self.__labTargetRR = QLabel('Target Right:')
        self.__lineTargetRR = QLineEdit()
        self.__labCriticalR = QLabel('Critical Value:')
        self.__lineCritical_valueR = QLineEdit()
        self.__labEmptyR = QLabel('          ')
        self.__lineCritical_RbR = QLineEdit()
        self.__labLimitRL = QLabel('Limit Left:')
        self.__lineLimitRL = QLineEdit()
        self.__labLimitRR = QLabel('Limit Right:')
        self.__lineLimitRR = QLineEdit()
        
        self.__labAdditionalR = QLabel('Additional Nodes')
        
        self.__btnAddR = QPushButton('Add Nodes')
        self.__btnAddR.clicked.connect(self.add_nodesR)
        self.__btnDelR = QPushButton('Delete')
        self.__btnDelAllR = QPushButton('Delete All')
        self.__treeWidgetR = QTreeWidget()
        self.__treeWidgetR.setHeaderLabels(['Value', 'Reliability (%)'])
        
        info_layout = QHBoxLayout()
        info_layout.addWidget(self.__labR)
        spacer = QSpacerItem(400,10)
        info_layout.addItem(spacer)
        info_layout.addWidget(self.__labTypeR)
        info_layout.addWidget(self.__typeR)
        info_layout.setAlignment(Qt.AlignLeft)
        
        hwg_info = QWidget()
        hwg_info.setLayout(info_layout)
        
        gridR_layout = QGridLayout(spacing=5)
        # gridF.setContentsMargins(0,0,0,0)
        str_info = self.__round_number(self.targetR['limit'][0])
        self.__lineLimitRL.setText(str_info)
        self.__lineLimitRL.setValidator(QDoubleValidator(-1e99, 1e99, 3))
        self.__lineLimitRL.editingFinished.connect(self.onLimitRLChanged)
        
        str_info = self.__round_number(self.targetR['limit'][1])
        self.__lineLimitRR.setText(str_info)
        self.__lineLimitRR.setValidator(QDoubleValidator(-1e99, 1e99, 3))
        self.__lineLimitRR.editingFinished.connect(self.onLimitRRChanged)
        if self.targetR['type'] == 'interval':
            str_info = self.__round_number(self.targetR['value'][0])
            self.__lineTargetRL.setText(str_info)
            self.__lineTargetRL.setValidator(QDoubleValidator(-1e99, 1e99, 3))
            self.__lineTargetRL.editingFinished.connect(self.onTargetRLChanged)
        
            str_info = self.__round_number(self.targetR['value'][1])
            self.__lineTargetRR.setText(str_info)
            self.__lineTargetRR.setValidator(QDoubleValidator(-1e99, 1e99, 3))
            self.__lineTargetRR.editingFinished.connect(self.onTargetRRChanged)
            items = [self.__labTargetRL, self.__lineTargetRL, 
                     self.__labTargetRR, self.__lineTargetRR,
                     self.__labLimitRL, self.__lineLimitRL,
                     self.__labLimitRR, self.__lineLimitRR]
        else:
            str_info = self.__round_number(self.targetR['value'][0])
            self.__lineCritical_valueR.setText(str_info)
            self.__lineCritical_valueR.setValidator(QDoubleValidator(-1e99, 1e99, 3))
            self.__lineCritical_valueR.editingFinished.connect(self.onCVRChanged)
            
            self.__lineCritical_RbR.setText(str(int(self.targetR['value'][1]*100))+'%')
            self.__lineCritical_RbR.setValidator(QDoubleValidator(-1e99, 1e99, 1))
            self.__lineCritical_RbR.editingFinished.connect(self.onCRbRChanged)
            items = [self.__labCriticalR, self.__lineCritical_valueR, 
                     self.__labEmptyR, self.__lineCritical_RbR,
                     self.__labLimitRL, self.__lineLimitRL,
                     self.__labLimitRR, self.__lineLimitRR]
        positions = [(i,j) for i in range(4) for j in range(2)]
        for item, pos in zip(items, positions):
            gridR_layout.addWidget(item, *pos)
            
        gridR_layout.addWidget(self.__labAdditionalR,4,0)
        
        # layout for all the widgets for below 'Additional Nodes'
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.__btnAddR)
        btn_layout.addWidget(self.__btnDelR)
        btn_layout.addWidget(self.__btnDelAllR)
        hwg_btn = QWidget()
        hwg_btn.setLayout(btn_layout)
        
        add_layout = QGridLayout()
        add_layout.addWidget(hwg_btn)
        add_layout.addWidget(self.__treeWidgetR)
        gwg_add = QWidget()
        gwg_add.setLayout(add_layout)
        
        gridR_layout.addWidget(gwg_add,5,0,5,3)
        
        gridR_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        gridwg_settingR = QWidget()
        # gridwg_front.setGeometry(130, 30, 30, 30)  
        gridwg_settingR.setLayout(gridR_layout)
        
        mainR_layout = QHBoxLayout()
        mainR_layout.addWidget(gridwg_settingR)
        # self.__fig = plt.figure(figsize=(15, 5), dpi=80)
        self.__figR = plt.figure()
        figCanvas = FigureCanvas(self.__figR)
        self.__get_nodes_rear()
        self.__drawFigureR()
        mainR_layout.addWidget(figCanvas)
        hwg_mainR = QWidget()
        hwg_mainR.setLayout(mainR_layout)
        
        self.layout.addWidget(hwg_info)
        self.layout.addWidget(hwg_mainR)
        
        
    def __get_nodes_front(self):
        if self.targetF['type'] == 'interval':
            self.__frontx = [self.targetF['limit'][0], self.targetF['value'][0],
                             self.targetF['value'][1], self.targetF['limit'][1]]
            self.__fronty = [0,1,1,0]
        elif self.targetF['type'] == 'max':
            self.__frontx = [(1.5*self.targetF['limit'][0] - 
                              0.5*self.targetF['limit'][1]),
                             self.targetF['limit'][0], self.targetF['value'][0],
                             self.targetF['limit'][1]]
            self.__fronty = [1,1,self.targetF['value'][1],0]
        else:
            self.__frontx = [self.targetF['limit'][0], self.targetF['value'][0], 
                             self.targetF['limit'][1],
                             (1.5*self.targetF['limit'][1] - 
                             0.5*self.targetF['limit'][0])]
            self.__fronty = [0,self.targetF['value'][1],1,1]
            
        
    def __get_nodes_rear(self):
        if self.targetR['type'] == 'interval':
            self.__rearx = [self.targetR['limit'][0], self.targetR['value'][0],
                            self.targetR['value'][1], self.targetR['limit'][1]]
            self.__reary = [0,1,1,0]
        elif self.targetR['type'] == 'max':
            self.__rearx = [(1.5*self.targetR['limit'][0] - 
                             0.5*self.targetR['limit'][1]),
                            self.targetR['limit'][0], self.targetR['value'][0],
                            self.targetR['limit'][1]]
            self.__reary = [1,1,self.targetR['value'][1],0]
        else:
            self.__rearx = [self.targetR['limit'][0], self.targetR['value'][0], 
                            self.targetR['limit'][1],
                            (1.5*self.targetR['limit'][1] - 
                             0.5*self.targetR['limit'][0])]
            self.__reary = [0,self.targetR['value'][1],1,1]
            
        
    def __drawFigureF(self):
        # return
        try:
            self.__axF.clear()
            self.__axF.set_xticks([])
            self.__axF.set_yticks([])
        except AttributeError:
            pass
        
        self.__axF = self.__figF.add_subplot(111)
        zipped = sorted(zip(self.__frontx,self.__fronty))
        x, y = zip(*zipped)
        self.__axF.plot(x,y)
        
        self.__figF.canvas.draw() 
        
        
    def __drawFigureR(self):
        # return
        try:
            self.__axR.clear()
            self.__axR.set_xticks([])
            self.__axR.set_yticks([])
        except AttributeError:
            pass
        
        self.__axR = self.__figR.add_subplot(111)
        zipped = sorted(zip(self.__rearx,self.__reary))
        x, y = zip(*zipped)
        self.__axR.plot(x,y)
        
        self.__figR.canvas.draw() 
        
        
    def __round_number(self, value):
        if type(value) != float:
            value = float(value)
        if abs(value) >= 1:
            str_info = "%.1f" % value
        elif 0.1 <= abs(value) < 1:
            str_info = "%.2f" % value
        elif 0.01 <= abs(value) < 0.1:
            str_info = "%.3f" % value
        elif 0.001 <= abs(value) < 0.01:
            str_info = "%.4f" % value
        elif 0.0001 <= abs(value) < 0.001:
            str_info = "%.5f" % value
        elif value == 0:
            str_info = '0'
        return str_info
            
            
    # for front suspension, type = interval
    def __updata_limitF_interval(self):
        """
        change the limit with a specific proportion when the target value changes
        """
        value = self.targetF['value']
        if self.para == 'static_camber':
            ans = [value[0] * 2, 0]
            
        elif self.para == 'bump_camber':
            ans = [value[0] * 2, 0]
            
        elif self.para == 'toe_in':
            left = value[0] - (value[1] - value[0])
            right = value[1] * 5
            ans = [left,right]
            
        elif self.para == 'bump_understeer':
            ans = [0, value[1] * 2.5]
            
        elif self.para == 'caster':
            ans = [value[0] * 2/3, value[1] * 3/2]
            
        elif self.para == 'kpi':
            ans = [value[0] * 1/3, value[1] * 3/2]
            
        elif self.para == 'scrub_r':
            left = value[0] - (value[1] - value[0])
            right = value[1] + (value[1] - value[0])
            ans = [left,right]
            
        elif self.para == 'static_rch':
            ans = self.targetF['limit']
        
        elif self.para == 'roll_bump':
            left = value[0] - 0.5 * (value[1] - value[0])
            right = value[1] + 0.5 * (value[1] - value[0])
            ans = [left,right]
        
        elif self.para == 'ackermann':
            ans = self.targetF['limit']
        
        elif self.para == 'lat_F_delta':
            ans = [0, value[1] * 3]
        
        elif self.para == 'drive_toe_in':
            left = value[0] * 3
            right = value[1] + 2 * (value[1] - value[0])
            ans = [left,right]
        
        elif self.para == 'anti_lift':
            ans = [0, value[1] * 2.5]
            
        elif self.para == 'brake_toe_in':
            ans = [value[0] * 2.5, 0]
            
        elif self.para == 'anti_dive':
            ans = [0, value[1] * 2.5]
        
        self.targetF['limit'] = ans
        self.__lineLimitFL.setText(self.__round_number(ans[0]))
        self.__lineLimitFR.setText(self.__round_number(ans[1]))
        
    
    # for front suspension, type = max or min
    def __updata_limitF_maxmin(self):
        value = self.targetF['value'][0]
        if self.para == 'kpo':
            ans = [value * 2/3, value * 1.1]
            
        elif self.para == 'wheel_travel':
            ans = [value * 0.6, value * 1.1]
            
        elif self.para == 'camber_comp':
            ans = [value * 2/3, value * 2]
            
        elif self.para == 'lat_stif':
            ans = [value * 0.8, value * 1.2]
            
        elif self.para == 'lat_F':
            ans = [value * 0.5, value * 1.25]
            
        elif self.para == 'caster_comp':
            ans = [value * 2, value * 0.8]
            
        self.targetF['limit'] = ans
        self.__lineLimitFL.setText(self.__round_number(ans[0]))
        self.__lineLimitFR.setText(self.__round_number(ans[1]))
        
        
    # for rear suspension, type = interval
    def __updata_limitR_interval(self):
        value = self.targetR['value']
        if self.para == 'static_camber':
            ans = [value[0] * 2, 0]
            
        elif self.para == 'bump_camber':
            ans = [value[0] * 2, 0]
            
        elif self.para == 'toe_in':
            left = value[0] - (value[1] - value[0])
            right = value[1] * 5
            ans = [left,right]
            
        elif self.para == 'bump_understeer':
            ans = [0, value[1] * 2.5]
            
        elif self.para == 'static_rch' or self.para == 'static_rch_diff':
            ans = self.targetR['limit']
        
        elif self.para == 'roll_bump':
            left = value[0] - 0.5 * (value[1] - value[0])
            right = value[1] + 0.5 * (value[1] - value[0])
            ans = [left,right]
        
        elif self.para == 'lat_F':
            ans = [0, value[1] * 3]
        
        elif self.para == 'lat_F_delta':
            left = 0
            right = value[1] + (value[1] - value[0])
            ans = [left,right]
        
        elif self.para == 'drive_toe_in':
            left = value[0] - 2 * (value[1] - value[0])
            right = value[1] + 2 * (value[1] - value[0])
            ans = [left,right]
        
        elif self.para == 'anti_squat':
            ans = [0, value[1] * 2.5]
            
        elif self.para == 'brake_toe_in':
            ans = [0, value[1] * 2.4]
            
        self.targetR['limit'] = ans
        self.__lineLimitRL.setText(self.__round_number(ans[0]))
        self.__lineLimitRR.setText(self.__round_number(ans[1]))
    
    
    # for rear suspension, type = max or min
    def __updata_limitR_maxmin(self):
        value = self.targetR['value'][0]
        if self.para == 'camber_comp':
            ans = [value * 2/3, value * 2]
            
        elif self.para == 'lat_stif':
            ans = [value * 0.8, value * 1.2]
            
        elif self.para == 'caster_comp':
            ans = [value * 2.5, value * 3/4]
            
        elif self.para == 'anti_lift':
            ans = [value * 0.3, value * 1.3]
            
        self.targetR['limit'] = ans
        self.__lineLimitRL.setText(self.__round_number(ans[0]))
        self.__lineLimitFR.setText(self.__round_number(ans[1]))
    
    
##  ====================Customised Slot Functions=============================
    def onLimitFLChanged(self):
        value = float(self.__lineLimitFL.text())
        if value > float(self.__lineLimitFR.text()):
            value = self.__lineLimitFR.text()
        # if self.target['type'] == 'interval':
        #     if float(value) > float(self.__lineTargetFL.text()):
        #         value = self.__lineTargetFL.text()
        value = self.__round_number(value)
        self.__lineLimitFL.setText(value)
        
        self.targetF['limit'][0] = float(value)
        self.__get_nodes_front()
        self.__drawFigureF()
        self.targetFChanged.emit(self.para, self.targetF)
        
        
    def onLimitFRChanged(self):
        value = float(self.__lineLimitFR.text())
        if value < float(self.__lineLimitFL.text()):
            value = self.__lineLimitFL.text()
        # if self.target['type'] == 'interval':
        #     if float(value) < float(self.__lineTargetFR.text()):
        #         value = self.__lineTargetFR.text()
        value = self.__round_number(value)
        self.__lineLimitFR.setText(value)
        
        self.targetF['limit'][1] = float(value)
        self.__get_nodes_front()
        self.__drawFigureF()
        self.targetFChanged.emit(self.para, self.targetF)
        
        
    def onTargetFLChanged(self):
        value = float(self.__lineTargetFL.text())
        # if float(value) < float(self.__lineLimitFL.text()):
        #     value = self.__lineLimitFL.text()
        if value > float(self.__lineTargetFR.text()):
            value = self.__lineTargetFR.text()
        value = self.__round_number(value)
        self.__lineTargetFL.setText(value)
        
        self.targetF['value'][0] = float(value)
        # auto updata the limit
        self.__updata_limitF_interval()
        self.__get_nodes_front()
        self.__drawFigureF()
        self.targetFChanged.emit(self.para, self.targetF)
        
        
    def onTargetFRChanged(self):
        value = float(self.__lineTargetFR.text())
        # if float(value) > float(self.__lineLimitFR.text()):
        #     value = self.__lineLimitFR.text()
        if value < float(self.__lineTargetFL.text()):
            value = self.__lineTargetFL.text()
        value = self.__round_number(value)
        self.__lineTargetFR.setText(value)
        
        self.targetF['value'][1] = float(value)
        # auto updata the limit
        self.__updata_limitF_interval()
        self.__get_nodes_front()
        self.__drawFigureF()
        self.targetFChanged.emit(self.para, self.targetF)
        
        
    def onCVFChanged(self):
        value = float(self.__lineCritical_valueF.text())
        value = self.__round_number(value)
        self.__lineCritical_valueF.setText(value)
        
        self.targetF['value'][0] = float(value)
        # auto updata the limit
        self.__updata_limitF_maxmin()
        self.__get_nodes_front()
        self.__drawFigureF()
        self.targetFChanged.emit(self.para, self.targetF)
        
        
    def onCRbFChanged(self):
        value = int(self.__lineCritical_RbF.text())
        if value > 100:
            value = 100
        if value < 0:
            value = -value
        self.__lineCritical_RbF.setText(str(value)+'%')
        
        self.targetF['value'][1] = value / 100
        self.__get_nodes_front()
        self.__drawFigureF()
        self.targetFChanged.emit(self.para, self.targetF)
        
        
    def onLimitRLChanged(self):
        value = float(self.__lineLimitRL.text())
        if value > float(self.__lineLimitRR.text()):
            value = self.__lineLimitRR.text()
        # if self.target['type'] == 'interval':
        #     if float(value) > float(self.__lineTargetRL.text()):
        #         value = self.__lineTargetRL.text()
        value = self.__round_number(value)
        self.__lineLimitRL.setText(value)
        
        self.targetR['limit'][0] = float(value)
        self.__get_nodes_rear()
        self.__drawFigureR()
        self.targetRChanged.emit(self.para, self.targetR)
        
        
    def onLimitRRChanged(self):
        value = float(self.__lineLimitRR.text())
        if value > float(self.__lineLimitRR.text()):
            value = self.__lineLimitRR.text()
        # if self.target['type'] == 'interval':
        #     if float(value) < float(self.__lineTargetRL.text()):
        #         value = self.__lineTargetRL.text()
        value = self.__round_number(value)
        self.__lineLimitRR.setText(value)
        
        self.targetR['limit'][1] = float(value)
        self.__get_nodes_rear()
        self.__drawFigureR()
        self.targetRChanged.emit(self.para, self.targetR)
        
        
    def onTargetRLChanged(self):
        value = float(self.__lineTargetRL.text())
        # if float(value) < float(self.__lineLimitRL.text()):
        #     value = self.__lineLimitRL.text()
        if value > float(self.__lineTargetRR.text()):
            value = self.__lineTargetRR.text()
        value = self.__round_number(value)
        self.__lineTargetRL.setText(value)
        
        self.targetR['value'][0] = float(value)
        # auto updata the limit
        self.__updata_limitR_interval()
        self.__get_nodes_rear()
        self.__drawFigureR()
        self.targetRChanged.emit(self.para, self.targetR)
        
        
    def onTargetRRChanged(self):
        value = float(self.__lineTargetRR.text())
        # if float(value) > float(self.__lineLimitRR.text()):
        #     value = self.__lineLimitRR.text()
        if value < float(self.__lineTargetRL.text()):
            value = self.__lineTargetRL.text()
        value = self.__round_number(value)
        self.__lineTargetRR.setText(value)
        
        self.targetR['value'][1] = float(value)
        # auto updata the limit
        self.__updata_limitR_interval()
        self.__get_nodes_rear()
        self.__drawFigureR()
        self.targetRChanged.emit(self.para, self.targetR)
        
        
    def onCVRChanged(self):
        value = float(self.__lineCritical_valueR.text())
        value = self.__round_number(value)
        self.__lineLimitFR.setText(value)
        
        self.targetR['value'][0] = float(value)
        # auto updata the limit
        self.__updata_limitR_maxmin()
        self.__get_nodes_rear()
        self.__drawFigureR()
        self.targetRChanged.emit(self.para, self.targetR)
        
        
    def onCRbRChanged(self):
        value = int(self.__lineCritical_RbR.text())
        if value > 100:
            value = 100
        if value < 0:
            value = -value
        self.__lineCritical_RbR.setText(str(value)+'%')
        
        self.targetR['value'][1] = value / 100
        self.__get_nodes_rear()
        self.__drawFigureR()
        self.targetRChanged.emit(self.para, self.targetR)
        
        
    def add_nodesF(self):
        dlgTitle = 'Value Dialog'
        txtLabel = 'Please enter the value'
        defaultValue = 0
        minValue = -9e9
        maxValue = 9e9
        if abs(self.targetF['limit'][0]) >= 1:
            decimals = 1
        elif 0.1 <= abs(self.targetF['limit'][0]) < 1:
            decimals = 2
        elif 0.01 <= abs(self.targetF['limit'][0]) < 0.1:
            decimals = 3
        elif 0.001 <= abs(self.targetF['limit'][0]) < 0.01:
            decimals = 4
        elif 0.0001 <= abs(self.targetF['limit'][0]) < 0.001:
            decimals = 5
        elif self.targetF['limit'][0] == 0:
            decimals = 2
        value, OK = QInputDialog.getDouble(self, dlgTitle, txtLabel,
                                    defaultValue, minValue, maxValue, decimals)
        if OK:
            dlgTitle = 'Reliability Dialog'
            txtLabel = 'Please enter the reliability (%)'
            defaultValue = 50
            minValue = 0
            maxValue = 100
            stepValue = 1
            reliability, OK = QInputDialog.getInt(self, dlgTitle, txtLabel,
                                defaultValue, minValue, maxValue, stepValue)
            if OK:
                item = QTreeWidgetItem()
                item.setText(0,str(value))
                item.setText(1,str(reliability)+'%')
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled) # nonEditable
                self.__treeWidgetF.addTopLevelItem(item)
                self.__treeWidgetF.setStyle(QStyleFactory.create('windows'))
                self.__frontx.append(value)
                self.__fronty.append(reliability/100)
                self.__drawFigureF()
        
        
    def add_nodesR(self):
        dlgTitle = 'Value Dialog'
        txtLabel = 'Please enter the value'
        defaultValue = 0
        minValue = -9e9
        maxValue = 9e9
        if abs(self.targetR['limit'][0]) >= 1:
            decimals = 1
        elif 0.1 <= abs(self.targetR['limit'][0]) < 1:
            decimals = 2
        elif 0.01 <= abs(self.targetR['limit'][0]) < 0.1:
            decimals = 3
        elif 0.001 <= abs(self.targetR['limit'][0]) < 0.01:
            decimals = 4
        elif 0.0001 <= abs(self.targetR['limit'][0]) < 0.001:
            decimals = 5
        elif self.targetR['limit'][0] == 0:
            decimals = 2
        value, OK = QInputDialog.getDouble(self, dlgTitle, txtLabel,
                                    defaultValue, minValue, maxValue, decimals)
        if OK:
            dlgTitle = 'Reliability Dialog'
            txtLabel = 'Please enter the reliability (%)'
            defaultValue = 50
            minValue = 0
            maxValue = 100
            stepValue = 1
            reliability, OK = QInputDialog.getInt(self, dlgTitle, txtLabel,
                                defaultValue, minValue, maxValue, stepValue)
            if OK:
                item = QTreeWidgetItem()
                item.setText(0,str(value))
                item.setText(1,str(reliability)+'%')
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled) # nonEditable
                self.__treeWidgetR.addTopLevelItem(item)
                self.__treeWidgetR.setStyle(QStyleFactory.create('windows'))
                self.__rearx.append(value)
                self.__reary.append(reliability/100)
                self.__drawFigureR()
        
        
