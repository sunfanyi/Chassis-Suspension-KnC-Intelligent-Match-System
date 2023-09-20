# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWFormCompare2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QWFormCompare2(object):
    def setupUi(self, QWFormCompare2):
        QWFormCompare2.setObjectName("QWFormCompare2")
        QWFormCompare2.resize(554, 530)
        self.gridLayout = QtWidgets.QGridLayout(QWFormCompare2)
        self.gridLayout.setObjectName("gridLayout")
        self.lw_all = QtWidgets.QListWidget(QWFormCompare2)
        self.lw_all.setMaximumSize(QtCore.QSize(750, 16777215))
        self.lw_all.setObjectName("lw_all")
        self.gridLayout.addWidget(self.lw_all, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(25)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnSelAll = QtWidgets.QPushButton(QWFormCompare2)
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
        self.verticalLayout_5.addWidget(self.btnSelAll)
        self.btnRemove = QtWidgets.QPushButton(QWFormCompare2)
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
        self.verticalLayout_5.addWidget(self.btnRemove)
        self.btnRemoveAll = QtWidgets.QPushButton(QWFormCompare2)
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
        self.verticalLayout_5.addWidget(self.btnRemoveAll)
        self.btnAdd = QtWidgets.QPushButton(QWFormCompare2)
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
        self.verticalLayout_5.addWidget(self.btnAdd)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.lw_tbCompared = QtWidgets.QListWidget(QWFormCompare2)
        self.lw_tbCompared.setMaximumSize(QtCore.QSize(750, 16777215))
        self.lw_tbCompared.setObjectName("lw_tbCompared")
        self.gridLayout.addWidget(self.lw_tbCompared, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnCompare = QtWidgets.QToolButton(QWFormCompare2)
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
        self.horizontalLayout_4.addWidget(self.btnCompare)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 2, 1, 1)

        self.retranslateUi(QWFormCompare2)
        self.btnSelAll.clicked.connect(self.lw_all.selectAll)
        QtCore.QMetaObject.connectSlotsByName(QWFormCompare2)

    def retranslateUi(self, QWFormCompare2):
        _translate = QtCore.QCoreApplication.translate
        QWFormCompare2.setWindowTitle(_translate("QWFormCompare2", "Form"))
        self.btnSelAll.setText(_translate("QWFormCompare2", "Select All"))
        self.btnRemove.setText(_translate("QWFormCompare2", "Remove"))
        self.btnRemoveAll.setText(_translate("QWFormCompare2", "Remove All"))
        self.btnAdd.setText(_translate("QWFormCompare2", "Add"))
        self.btnCompare.setText(_translate("QWFormCompare2", ">>>Compare"))


