# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWFormWelcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QWFormWelcome(object):
    def setupUi(self, QWFormWelcome):
        QWFormWelcome.setObjectName("QWFormWelcome")
        QWFormWelcome.resize(1600, 1000)
        self.btnStart = QtWidgets.QToolButton(QWFormWelcome)
        self.btnStart.setGeometry(QtCore.QRect(920, 820, 450, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        self.btnStart.setMinimumSize(QtCore.QSize(450, 70))
        self.btnStart.setMaximumSize(QtCore.QSize(450, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStart.setStyleSheet("")
        self.btnStart.setIconSize(QtCore.QSize(16, 16))
        self.btnStart.setObjectName("btnStart")

        self.retranslateUi(QWFormWelcome)
        QtCore.QMetaObject.connectSlotsByName(QWFormWelcome)

    def retranslateUi(self, QWFormWelcome):
        _translate = QtCore.QCoreApplication.translate
        QWFormWelcome.setWindowTitle(_translate("QWFormWelcome", "Form"))
        self.btnStart.setText(_translate("QWFormWelcome", ">>> GET STARTED"))

