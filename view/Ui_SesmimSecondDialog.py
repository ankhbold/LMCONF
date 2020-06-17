# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SesmimSecondDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SesmimSecondDialog(object):
    def setupUi(self, SesmimSecondDialog):
        SesmimSecondDialog.setObjectName(_fromUtf8("SesmimSecondDialog"))
        SesmimSecondDialog.resize(850, 550)
        SesmimSecondDialog.setMinimumSize(QtCore.QSize(850, 550))
        SesmimSecondDialog.setMaximumSize(QtCore.QSize(850, 550))
        SesmimSecondDialog.setBaseSize(QtCore.QSize(860, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/lm2/user_role_management.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SesmimSecondDialog.setWindowIcon(icon)

        self.retranslateUi(SesmimSecondDialog)
        QtCore.QMetaObject.connectSlotsByName(SesmimSecondDialog)

    def retranslateUi(self, SesmimSecondDialog):
        SesmimSecondDialog.setWindowTitle(_translate("SesmimSecondDialog", "User Role Management", None))

import resources_rc
