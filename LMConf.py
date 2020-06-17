import os.path
# -*- encoding: utf-8 -*-
from trace import Trace

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
from qgis.core import *
from controller.SesmimFirstDialog import *
from controller.SesmimSecondDialog import *
from controller.NavigatorWidget import *

from view.resources_rc import *
import qgis.core

class LMConf:

    def __init__(self, iface):

        # Save reference to the QGIS interface
        self.iface = iface
        self.activeAction = None
        self.activeParcelAction = None
        self.parcel_no = None
        self.result_feature = None
        self.navigatorWidget = None
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

    def initGui(self):

        self.navigatorWidget = None

        # Create action that will start plugin configuration
        self.sesmim_first_action = QAction(QIcon(":/plugins/lmconf/crops.png"), QApplication.translate("Plugin", "LMCONF first dialog"), self.iface.mainWindow())
        self.sesmim_second_action = QAction(QIcon(":/plugins/lmconf/certf.png"), QApplication.translate("Plugin", "LMCONF second dialog"), self.iface.mainWindow())
        self.navigator_action = QAction(QIcon(":/plugins/lmconf/navigator.png"),
                                        QApplication.translate("Plugin", "Show/Hide Navigator"),
                                        self.iface.mainWindow())
        self.navigator_action.setCheckable(True)
        # connect the action to the run method
        self.sesmim_first_action.triggered.connect(self.__show_fist_dialog)
        self.sesmim_second_action.triggered.connect(self.__show_second_dialog)

        self.__create_navigator()
        self.navigator_action.triggered.connect(self.__show_navigator_widget)

        # self.reports_action.triggered.connect(self.__show_reports_dialog)


        # Add toolbar button and menu item
        self.lm_toolbar = self.iface.addToolBar(QApplication.translate("Plugin", "LMCONF porject"))

        self.lm_toolbar.addAction(self.sesmim_first_action)
        self.lm_toolbar.addAction(self.sesmim_second_action)
        self.lm_toolbar.addAction(self.navigator_action)

        # Retrieve main menu bar
        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()

        # Create menus
        self.lm_menu = QMenu()
        self.lm_menu.setTitle(QApplication.translate("Plugin", "&LMCONF"))
        menu_bar.addMenu(self.lm_menu)

        self.lm_menu.addAction(self.navigator_action)
        self.lm_menu.addAction(self.sesmim_first_action)
        self.lm_menu.addSeparator()
        self.lm_menu.addAction(self.sesmim_second_action)

    def unload(self):

        self.iface.removePluginMenu(QApplication.translate("Plugin", "&LMCONF"), self.sesmim_first_action)
        self.iface.removePluginMenu(QApplication.translate("Plugin", "&LMCONF"), self.sesmim_second_action)
        self.iface.removePluginMenu(QApplication.translate("Plugin", "&LMCONF"), self.navigator_action)

        del self.lm_toolbar

        if self.navigatorWidget:
            self.iface.removeDockWidget(self.navigatorWidget)
            del self.navigatorWidget

    def __show_navigator_widget(self):

        print 'ddddd'
        if self.navigatorWidget != None:
            if self.navigatorWidget.isVisible():
                if self.navigatorWidget:
                    self.navigatorWidget.hide()
            else:
                if self.navigatorWidget:
                    self.navigatorWidget.show()

    def __show_fist_dialog(self):

        print "-test sesmim plugin 1-"
        dlg = SesmimFirstDialog(self.iface, self.iface.mainWindow())
        dlg.exec_()

    def __show_second_dialog(self):

        print "-test sesmim plugin 1-"
        dlg = SesmimSecondDialog(self.iface, self.iface.mainWindow())
        dlg.exec_()

    def __create_navigator(self):

        # self.removeLayers()
        # create widget
        if self.navigatorWidget:
            self.iface.removeDockWidget(self.navigatorWidget)
            del self.navigatorWidget

        self.navigatorWidget = NavigatorWidget(self)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.navigatorWidget)
        QObject.connect(self.navigatorWidget, SIGNAL("visibilityChanged(bool)"), self.__navigatorVisibilityChanged)
        self.navigatorWidget.show()

    def __navigatorVisibilityChanged(self):

        if self.navigatorWidget.isVisible():
            self.navigator_action.setChecked(True)
        else:
            self.navigator_action.setChecked(False)