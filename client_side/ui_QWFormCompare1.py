# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWFormCompare1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QWFormCompare1(object):
    def setupUi(self, QWFormCompare1):
        QWFormCompare1.setObjectName("QWFormCompare1")
        QWFormCompare1.resize(554, 530)
        self.gridLayout = QtWidgets.QGridLayout(QWFormCompare1)
        self.gridLayout.setContentsMargins(20, 20, 20, 15)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(QWFormCompare1)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineTarget = QtWidgets.QLineEdit(QWFormCompare1)
        self.lineTarget.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineTarget.setFont(font)
        self.lineTarget.setStyleSheet("QLineEdit{\n"
"    border: 2px groove gray;\n"
"    border-radius: 22px;\n"
"    padding: 2px 4px;\n"
"    color: rgb(0, 0, 0);\n"
"    border-color: rgb(0, 100, 0);\n"
"}")
        self.lineTarget.setReadOnly(True)
        self.lineTarget.setObjectName("lineTarget")
        self.horizontalLayout_2.addWidget(self.lineTarget)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(25)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnSetTarget = QtWidgets.QPushButton(QWFormCompare1)
        self.btnSetTarget.setMinimumSize(QtCore.QSize(200, 50))
        self.btnSetTarget.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnSetTarget.setFont(font)
        self.btnSetTarget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSetTarget.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border: 1.5px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    border-radius: 25px;\n"
"    padding: 4px 4px;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: Black;\n"
"    font-size: 12pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(150, 150, 150);\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: Black;\n"
"    font-size: 11pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    background-color: rgb(195, 255, 255);\n"
"}\n"
"")
        self.btnSetTarget.setObjectName("btnSetTarget")
        self.verticalLayout_3.addWidget(self.btnSetTarget)
        self.btnSelAll = QtWidgets.QPushButton(QWFormCompare1)
        self.btnSelAll.setMinimumSize(QtCore.QSize(200, 50))
        self.btnSelAll.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnSelAll.setFont(font)
        self.btnSelAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSelAll.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border: 1.5px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    border-radius: 25px;\n"
"    padding: 4px 4px;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: Black;\n"
"    font-size: 12pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(150, 150, 150);\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: Black;\n"
"    font-size: 11pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    background-color: rgb(195, 255, 255);\n"
"}\n"
"")
        self.btnSelAll.setObjectName("btnSelAll")
        self.verticalLayout_3.addWidget(self.btnSelAll)
        self.btnRemove = QtWidgets.QPushButton(QWFormCompare1)
        self.btnRemove.setMinimumSize(QtCore.QSize(200, 50))
        self.btnRemove.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnRemove.setFont(font)
        self.btnRemove.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRemove.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border: 1.5px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    border-radius: 25px;\n"
"    padding: 4px 4px;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: Black;\n"
"    font-size: 12pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(150, 150, 150);\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: Black;\n"
"    font-size: 11pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    background-color: rgb(195, 255, 255);\n"
"}\n"
"")
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout_3.addWidget(self.btnRemove)
        self.btnRemoveAll = QtWidgets.QPushButton(QWFormCompare1)
        self.btnRemoveAll.setMinimumSize(QtCore.QSize(200, 50))
        self.btnRemoveAll.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnRemoveAll.setFont(font)
        self.btnRemoveAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRemoveAll.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border: 1.5px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    border-radius: 25px;\n"
"    padding: 4px 4px;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: Black;\n"
"    font-size: 12pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(150, 150, 150);\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: Black;\n"
"    font-size: 11pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    background-color: rgb(195, 255, 255);\n"
"}\n"
"")
        self.btnRemoveAll.setObjectName("btnRemoveAll")
        self.verticalLayout_3.addWidget(self.btnRemoveAll)
        self.btnAdd = QtWidgets.QPushButton(QWFormCompare1)
        self.btnAdd.setMinimumSize(QtCore.QSize(200, 50))
        self.btnAdd.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border: 1.5px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    border-radius: 25px;\n"
"    padding: 4px 4px;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: Black;\n"
"    font-size: 12pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(150, 150, 150);\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: Black;\n"
"    font-size: 11pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    background-color: rgb(195, 255, 255);\n"
"}\n"
"")
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout_3.addWidget(self.btnAdd)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.lw_tbCompared = QtWidgets.QListWidget(QWFormCompare1)
        self.lw_tbCompared.setMaximumSize(QtCore.QSize(750, 16777215))
        self.lw_tbCompared.setObjectName("lw_tbCompared")
        self.gridLayout.addWidget(self.lw_tbCompared, 1, 2, 1, 1)
        self.lw_all = QtWidgets.QListWidget(QWFormCompare1)
        self.lw_all.setMaximumSize(QtCore.QSize(750, 16777215))
        self.lw_all.setObjectName("lw_all")
        self.gridLayout.addWidget(self.lw_all, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnCompare = QtWidgets.QToolButton(QWFormCompare1)
        self.btnCompare.setMinimumSize(QtCore.QSize(200, 50))
        self.btnCompare.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btnCompare.setFont(font)
        self.btnCompare.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCompare.setStyleSheet("QToolButton{\n"
"    color: black;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border: 1.5px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    border-radius: 25px;\n"
"    padding: 4px 4px;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"    color: Black;\n"
"    font-size: 12pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(150, 150, 150);\n"
"    background-color: rgb(225, 255, 255);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"    color: Black;\n"
"    font-size: 11pt;\n"
"    padding: 3px 4px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    background-color: rgb(195, 255, 255);\n"
"}\n"
"")
        self.btnCompare.setIconSize(QtCore.QSize(16, 16))
        self.btnCompare.setObjectName("btnCompare")
        self.horizontalLayout_3.addWidget(self.btnCompare)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 2, 1, 1)

        self.retranslateUi(QWFormCompare1)
        self.btnSelAll.clicked.connect(self.lw_all.selectAll)
        QtCore.QMetaObject.connectSlotsByName(QWFormCompare1)

    def retranslateUi(self, QWFormCompare1):
        _translate = QtCore.QCoreApplication.translate
        QWFormCompare1.setWindowTitle(_translate("QWFormCompare1", "Form"))
        self.label.setText(_translate("QWFormCompare1", "    Target Vehicle:    "))
        self.btnSetTarget.setText(_translate("QWFormCompare1", "Set Target"))
        self.btnSelAll.setText(_translate("QWFormCompare1", "Select All"))
        self.btnRemove.setText(_translate("QWFormCompare1", "Remove"))
        self.btnRemoveAll.setText(_translate("QWFormCompare1", "Remove All"))
        self.btnAdd.setText(_translate("QWFormCompare1", "Add"))
        self.btnCompare.setText(_translate("QWFormCompare1", ">>>Compare"))


