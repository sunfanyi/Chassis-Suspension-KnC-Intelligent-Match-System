# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWFormSetTarget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QWFormSetTarget(object):
    def setupUi(self, QWFormSetTarget):
        QWFormSetTarget.setObjectName("QWFormSetTarget")
        QWFormSetTarget.resize(1600, 1000)
        self.actImport = QtWidgets.QAction(QWFormSetTarget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.actImport.setFont(font)
        self.actImport.setObjectName("actImport")
        self.actSave = QtWidgets.QAction(QWFormSetTarget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.actSave.setFont(font)
        self.actSave.setObjectName("actSave")
        self.actResetAll = QtWidgets.QAction(QWFormSetTarget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.actResetAll.setFont(font)
        self.actResetAll.setObjectName("actResetAll")
        self.actUndo = QtWidgets.QAction(QWFormSetTarget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.actUndo.setFont(font)
        self.actUndo.setObjectName("actUndo")
        self.actRedo = QtWidgets.QAction(QWFormSetTarget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.actRedo.setFont(font)
        self.actRedo.setObjectName("actRedo")
        self.actResetLoc = QtWidgets.QAction(QWFormSetTarget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.actResetLoc.setFont(font)
        self.actResetLoc.setObjectName("actResetLoc")
        self.actSeparator1 = QtWidgets.QAction(QWFormSetTarget)
        self.actSeparator1.setEnabled(False)
        self.actSeparator1.setObjectName("actSeparator1")
        self.actSeparator2 = QtWidgets.QAction(QWFormSetTarget)
        self.actSeparator2.setEnabled(False)
        self.actSeparator2.setObjectName("actSeparator2")
        self.actSeparator3 = QtWidgets.QAction(QWFormSetTarget)
        self.actSeparator3.setEnabled(False)
        self.actSeparator3.setObjectName("actSeparator3")

        self.retranslateUi(QWFormSetTarget)
        QtCore.QMetaObject.connectSlotsByName(QWFormSetTarget)

    def retranslateUi(self, QWFormSetTarget):
        _translate = QtCore.QCoreApplication.translate
        QWFormSetTarget.setWindowTitle(_translate("QWFormSetTarget", "Form"))
        self.actImport.setText(_translate("QWFormSetTarget", "Import Setting"))
        self.actSave.setText(_translate("QWFormSetTarget", "Save Setting As"))
        self.actResetAll.setText(_translate("QWFormSetTarget", "Reset All"))
        self.actUndo.setText(_translate("QWFormSetTarget", "Undo"))
        self.actRedo.setText(_translate("QWFormSetTarget", "Redo"))
        self.actResetLoc.setText(_translate("QWFormSetTarget", "Reset Current Page"))
        self.actSeparator1.setText(_translate("QWFormSetTarget", "|"))
        self.actSeparator2.setText(_translate("QWFormSetTarget", "|"))
        self.actSeparator3.setText(_translate("QWFormSetTarget", "|"))

