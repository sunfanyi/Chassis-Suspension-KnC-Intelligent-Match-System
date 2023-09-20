# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:47:12 2021

@author: Fanyi Sun
"""


from PyQt5.QtWidgets import QWidget, QApplication

from PyQt5.QtGui import QPixmap, QPainter

from PyQt5.QtCore import  pyqtSlot, pyqtSignal

from ui_QWFormWelcome import Ui_QWFormWelcome

from qss import QSS


class QmyFormWelcome(QWidget):
    getStarted = pyqtSignal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_QWFormWelcome()
        self.ui.setupUi(self)
        
        qss = QSS()
        self.setStyleSheet(qss.btnStart)
        
##  =====================Event Processing Functions===========================
    def paintEvent(self, event):
        painter = QPainter(self)
        pic = QPixmap(":/icons/images/V60/V60_background.png")
        painter.drawPixmap(-70, -50, self.width()+70, self.height()+50, pic)
        super().paintEvent(event)
        
    
    def resizeEvent(self, event):
        w = self.width()
        h = self.height()
        wbtn = self.ui.btnStart.width()
        hbtn = self.ui.btnStart.height()
        self.ui.btnStart.setGeometry(920/1600*w, 820/1000*h, wbtn, hbtn)


##  ================ Slot Functions by connectSlotsByName()===================
    @pyqtSlot()
    def on_btnStart_clicked(self):
        self.getStarted.emit(True)
        
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = QmyFormWelcome()    
    win.show()
    sys.exit(app.exec_())