__author__ = 'ankhaa'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from sqlalchemy import exc, or_
from sqlalchemy.exc import DatabaseError, SQLAlchemyError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import func, or_, and_, desc,extract
from inspect import currentframe
from ..view.Ui_SesmimSecondDialog import *
from uuid import getnode as get_mac
import  commands
import datetime
import socket
import sys
import struct

INTERFACE_NAME = "eth0"
class SesmimSecondDialog(QDialog, Ui_SesmimSecondDialog):

    GROUP_SEPARATOR = '-----'
    PW_PLACEHOLDER = '0123456789'

    def __init__(self, has_privilege , user, parent=None):

        super(SesmimSecondDialog, self).__init__(parent)
        self.setupUi(self)
