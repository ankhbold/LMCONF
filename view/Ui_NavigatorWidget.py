# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\NavigatorWidget.ui'
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

class Ui_NavigatorWidget(object):
    def setupUi(self, NavigatorWidget):
        NavigatorWidget.setObjectName(_fromUtf8("NavigatorWidget"))
        NavigatorWidget.resize(415, 712)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NavigatorWidget.sizePolicy().hasHeightForWidth())
        NavigatorWidget.setSizePolicy(sizePolicy)
        NavigatorWidget.setMinimumSize(QtCore.QSize(415, 620))
        NavigatorWidget.setMaximumSize(QtCore.QSize(415, 524287))
        NavigatorWidget.setBaseSize(QtCore.QSize(440, 665))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 418, 650))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 600))
        self.scrollArea.setMaximumSize(QtCore.QSize(435, 650))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 664))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.working_l1_cbox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.working_l1_cbox.setGeometry(QtCore.QRect(6, 4, 191, 22))
        self.working_l1_cbox.setObjectName(_fromUtf8("working_l1_cbox"))
        self.working_l2_cbox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.working_l2_cbox.setGeometry(QtCore.QRect(205, 4, 191, 22))
        self.working_l2_cbox.setObjectName(_fromUtf8("working_l2_cbox"))
        self.error_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.error_label.setGeometry(QtCore.QRect(20, 576, 374, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet(_fromUtf8("QLabel {color : red;}\n"
"font: 75 14pt \"Helvetica\";"))
        self.error_label.setText(_fromUtf8(""))
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName(_fromUtf8("error_label"))
        self.load_exc_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.load_exc_button.setGeometry(QtCore.QRect(316, 67, 75, 23))
        self.load_exc_button.setObjectName(_fromUtf8("load_exc_button"))
        self.exc_twidget = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.exc_twidget.setGeometry(QtCore.QRect(10, 180, 381, 301))
        self.exc_twidget.setObjectName(_fromUtf8("exc_twidget"))
        self.exc_twidget.setColumnCount(0)
        self.exc_twidget.setRowCount(0)
        self.exc_path_edit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.exc_path_edit.setGeometry(QtCore.QRect(170, 40, 221, 20))
        self.exc_path_edit.setObjectName(_fromUtf8("exc_path_edit"))
        self.header_row_sbox = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.header_row_sbox.setGeometry(QtCore.QRect(90, 40, 61, 22))
        self.header_row_sbox.setProperty("value", 1)
        self.header_row_sbox.setObjectName(_fromUtf8("header_row_sbox"))
        self.data_row_sbox = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.data_row_sbox.setGeometry(QtCore.QRect(90, 70, 61, 22))
        self.data_row_sbox.setProperty("value", 1)
        self.data_row_sbox.setObjectName(_fromUtf8("data_row_sbox"))
        self.data_column_sbox = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.data_column_sbox.setGeometry(QtCore.QRect(90, 100, 61, 22))
        self.data_column_sbox.setProperty("value", 0)
        self.data_column_sbox.setObjectName(_fromUtf8("data_column_sbox"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.load_data_button = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.load_data_button.setGeometry(QtCore.QRect(316, 100, 75, 23))
        self.load_data_button.setObjectName(_fromUtf8("load_data_button"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        NavigatorWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(NavigatorWidget)
        QtCore.QMetaObject.connectSlotsByName(NavigatorWidget)

    def retranslateUi(self, NavigatorWidget):
        NavigatorWidget.setWindowTitle(_translate("NavigatorWidget", "Selection / Filter", None))
        self.load_exc_button.setText(_translate("NavigatorWidget", "EXCEL", None))
        self.label.setText(_translate("NavigatorWidget", "Header row", None))
        self.label_2.setText(_translate("NavigatorWidget", "data row", None))
        self.label_3.setText(_translate("NavigatorWidget", "data column", None))
        self.load_data_button.setText(_translate("NavigatorWidget", "LOAD", None))

