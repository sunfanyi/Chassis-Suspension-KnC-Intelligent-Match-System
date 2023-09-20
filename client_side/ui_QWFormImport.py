# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWFormImport.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QWFormImport(object):
    def setupUi(self, QWFormImport):
        QWFormImport.setObjectName("QWFormImport")
        QWFormImport.resize(660, 391)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QWFormImport.sizePolicy().hasHeightForWidth())
        QWFormImport.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(QWFormImport)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 20, 20, 15)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStore = QtWidgets.QPushButton(self.centralwidget)
        self.btnStore.setMinimumSize(QtCore.QSize(350, 50))
        self.btnStore.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnStore.setFont(font)
        self.btnStore.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnStore.setStyleSheet("QPushButton{\n"
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
        self.btnStore.setObjectName("btnStore")
        self.horizontalLayout.addWidget(self.btnStore)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border: 2px groove gray;\n"
"    border-radius: 22px;\n"
"    padding: 2px 4px;\n"
"    color: rgb(0, 0, 0);\n"
"    border-color: rgb(0, 100, 0);\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnImport = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnImport.sizePolicy().hasHeightForWidth())
        self.btnImport.setSizePolicy(sizePolicy)
        self.btnImport.setMinimumSize(QtCore.QSize(200, 50))
        self.btnImport.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnImport.setFont(font)
        self.btnImport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnImport.setStyleSheet("QPushButton{\n"
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
        self.btnImport.setObjectName("btnImport")
        self.verticalLayout.addWidget(self.btnImport)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDel.sizePolicy().hasHeightForWidth())
        self.btnDel.setSizePolicy(sizePolicy)
        self.btnDel.setMinimumSize(QtCore.QSize(200, 50))
        self.btnDel.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnDel.setFont(font)
        self.btnDel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDel.setStyleSheet("QPushButton{\n"
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
        self.btnDel.setObjectName("btnDel")
        self.verticalLayout.addWidget(self.btnDel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.btnDelAll = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelAll.sizePolicy().hasHeightForWidth())
        self.btnDelAll.setSizePolicy(sizePolicy)
        self.btnDelAll.setMinimumSize(QtCore.QSize(200, 50))
        self.btnDelAll.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnDelAll.setFont(font)
        self.btnDelAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelAll.setStyleSheet("QPushButton{\n"
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
        self.btnDelAll.setObjectName("btnDelAll")
        self.verticalLayout.addWidget(self.btnDelAll)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.btnRecovery = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRecovery.sizePolicy().hasHeightForWidth())
        self.btnRecovery.setSizePolicy(sizePolicy)
        self.btnRecovery.setMinimumSize(QtCore.QSize(200, 60))
        self.btnRecovery.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnRecovery.setFont(font)
        self.btnRecovery.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRecovery.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(250, 250, 250);\n"
"    border: 1.5px;\n"
"    border-color: rgb(100, 100, 100);\n"
"    border-radius: 30px;\n"
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
        self.btnRecovery.setObjectName("btnRecovery")
        self.verticalLayout.addWidget(self.btnRecovery)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 2, 3)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(750, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 4, 2, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(750, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 2, 1)
        QWFormImport.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(QWFormImport)
        self.statusBar.setObjectName("statusBar")
        QWFormImport.setStatusBar(self.statusBar)

        self.retranslateUi(QWFormImport)
        QtCore.QMetaObject.connectSlotsByName(QWFormImport)

    def retranslateUi(self, QWFormImport):
        _translate = QtCore.QCoreApplication.translate
        QWFormImport.setWindowTitle(_translate("QWFormImport", "MainWindow"))
        self.btnStore.setText(_translate("QWFormImport", "Choose Store Path..."))
        self.btnImport.setText(_translate("QWFormImport", "Import..."))
        self.btnDel.setText(_translate("QWFormImport", "Delete"))
        self.btnDelAll.setText(_translate("QWFormImport", "Delete All"))
        self.btnRecovery.setText(_translate("QWFormImport", "Missing Data \n"
"Recovery"))

