# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ConnectDialog.ui'
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

class Ui_ConnectDialog(object):
    def setupUi(self, ConnectDialog):
        ConnectDialog.setObjectName(_fromUtf8("ConnectDialog"))
        ConnectDialog.resize(250, 250)
        ConnectDialog.setMinimumSize(QtCore.QSize(250, 250))
        ConnectDialog.setMaximumSize(QtCore.QSize(250, 250))
        ConnectDialog.setBaseSize(QtCore.QSize(250, 250))
        self.connect_button = QtGui.QPushButton(ConnectDialog)
        self.connect_button.setGeometry(QtCore.QRect(70, 80, 131, 61))
        self.connect_button.setObjectName(_fromUtf8("connect_button"))

        self.retranslateUi(ConnectDialog)
        QtCore.QMetaObject.connectSlotsByName(ConnectDialog)

    def retranslateUi(self, ConnectDialog):
        ConnectDialog.setWindowTitle(_translate("ConnectDialog", "Dialog", None))
        self.connect_button.setText(_translate("ConnectDialog", "CONNECT", None))

import resources_rc
