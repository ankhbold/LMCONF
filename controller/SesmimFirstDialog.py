__author__ = 'anna'
# coding=utf8
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
from qgis.core import *
from inspect import currentframe
from ..view.Ui_SesmimFirstDialog import *
from sqlalchemy.exc import DatabaseError, SQLAlchemyError

from datetime import timedelta, datetime
import win32netcon,win32wnet
import os
import os.path
import shutil
import sys
import win32wnet
import qgis.core

class SesmimFirstDialog(QDialog, Ui_SesmimFirstDialog):

    def __init__(self, iface, parent=None):

        super(SesmimFirstDialog,  self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.setWindowTitle(self.tr("Sesmim first dialog"))
