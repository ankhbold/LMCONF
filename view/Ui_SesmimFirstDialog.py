# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SesmimFirstDialog.ui'
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

class Ui_SesmimFirstDialog(object):
    def setupUi(self, SesmimFirstDialog):
        SesmimFirstDialog.setObjectName(_fromUtf8("SesmimFirstDialog"))
        SesmimFirstDialog.resize(600, 600)
        SesmimFirstDialog.setMinimumSize(QtCore.QSize(600, 600))
        SesmimFirstDialog.setMaximumSize(QtCore.QSize(600, 600))
        SesmimFirstDialog.setBaseSize(QtCore.QSize(600, 600))

        self.retranslateUi(SesmimFirstDialog)
        QtCore.QMetaObject.connectSlotsByName(SesmimFirstDialog)

    def retranslateUi(self, SesmimFirstDialog):
        SesmimFirstDialog.setWindowTitle(_translate("SesmimFirstDialog", "Dialog", None))

import resources_rc
