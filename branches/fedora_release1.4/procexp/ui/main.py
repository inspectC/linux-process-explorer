# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Dec  1 12:56:25 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(518, 358)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Linux Process Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.freezeCheckBox = QtGui.QCheckBox(self.frame)
        self.freezeCheckBox.setText(QtGui.QApplication.translate("MainWindow", "freeze", None, QtGui.QApplication.UnicodeUTF8))
        self.freezeCheckBox.setObjectName(_fromUtf8("freezeCheckBox"))
        self.horizontalLayout.addWidget(self.freezeCheckBox)
        self.qwtPlotOverallCpuHist = QwtPlot(self.frame)
        self.qwtPlotOverallCpuHist.setMinimumSize(QtCore.QSize(150, 0))
        self.qwtPlotOverallCpuHist.setMaximumSize(QtCore.QSize(150, 50))
        self.qwtPlotOverallCpuHist.setObjectName(_fromUtf8("qwtPlotOverallCpuHist"))
        self.horizontalLayout.addWidget(self.qwtPlotOverallCpuHist)
        self.verticalLayout.addWidget(self.frame)
        self.processTreeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.processTreeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.processTreeWidget.setColumnCount(0)
        self.processTreeWidget.setObjectName(_fromUtf8("processTreeWidget"))
        self.processTreeWidget.header().setCascadingSectionResizes(True)
        self.processTreeWidget.header().setDefaultSectionSize(50)
        self.verticalLayout.addWidget(self.processTreeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuProcess = QtGui.QMenu(self.menubar)
        self.menuProcess.setTitle(QtGui.QApplication.translate("MainWindow", "Process", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProcess.setObjectName(_fromUtf8("menuProcess"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSet_affinity = QtGui.QAction(MainWindow)
        self.actionSet_affinity.setText(QtGui.QApplication.translate("MainWindow", "Set affinity", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_affinity.setObjectName(_fromUtf8("actionSet_affinity"))
        self.actionSet_priority = QtGui.QAction(MainWindow)
        self.actionSet_priority.setText(QtGui.QApplication.translate("MainWindow", "Set priority", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_priority.setObjectName(_fromUtf8("actionSet_priority"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setText(QtGui.QApplication.translate("MainWindow", "----", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setObjectName(_fromUtf8("action"))
        self.actionKill_process = QtGui.QAction(MainWindow)
        self.actionKill_process.setText(QtGui.QApplication.translate("MainWindow", "Kill process", None, QtGui.QApplication.UnicodeUTF8))
        self.actionKill_process.setObjectName(_fromUtf8("actionKill_process"))
        self.actionKill_process_tree = QtGui.QAction(MainWindow)
        self.actionKill_process_tree.setText(QtGui.QApplication.translate("MainWindow", "Kill process tree", None, QtGui.QApplication.UnicodeUTF8))
        self.actionKill_process_tree.setObjectName(_fromUtf8("actionKill_process_tree"))
        self.actionSuspend_process = QtGui.QAction(MainWindow)
        self.actionSuspend_process.setText(QtGui.QApplication.translate("MainWindow", "Suspend process", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSuspend_process.setObjectName(_fromUtf8("actionSuspend_process"))
        self.actionProperties = QtGui.QAction(MainWindow)
        self.actionProperties.setText(QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setObjectName(_fromUtf8("actionProperties"))
        self.actionShow_process_from_all_users = QtGui.QAction(MainWindow)
        self.actionShow_process_from_all_users.setText(QtGui.QApplication.translate("MainWindow", "Show process from all users", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_process_from_all_users.setObjectName(_fromUtf8("actionShow_process_from_all_users"))
        self.action8 = QtGui.QAction(MainWindow)
        self.action8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.action8.setObjectName(_fromUtf8("action8"))
        self.action9 = QtGui.QAction(MainWindow)
        self.action9.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.action9.setObjectName(_fromUtf8("action9"))
        self.action7 = QtGui.QAction(MainWindow)
        self.action7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.action7.setObjectName(_fromUtf8("action7"))
        self.action81 = QtGui.QAction(MainWindow)
        self.action81.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.action81.setObjectName(_fromUtf8("action81"))
        self.action10 = QtGui.QAction(MainWindow)
        self.action10.setText(QtGui.QApplication.translate("MainWindow", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.action10.setObjectName(_fromUtf8("action10"))
        self.action12 = QtGui.QAction(MainWindow)
        self.action12.setText(QtGui.QApplication.translate("MainWindow", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.action12.setObjectName(_fromUtf8("action12"))
        self.action14 = QtGui.QAction(MainWindow)
        self.action14.setText(QtGui.QApplication.translate("MainWindow", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.action14.setObjectName(_fromUtf8("action14"))
        self.actionSaveSettings = QtGui.QAction(MainWindow)
        self.actionSaveSettings.setText(QtGui.QApplication.translate("MainWindow", "Save current settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveSettings.setObjectName(_fromUtf8("actionSaveSettings"))
        self.action10_2 = QtGui.QAction(MainWindow)
        self.action10_2.setText(QtGui.QApplication.translate("MainWindow", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.action10_2.setObjectName(_fromUtf8("action10_2"))
        self.action100 = QtGui.QAction(MainWindow)
        self.action100.setText(QtGui.QApplication.translate("MainWindow", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.action100.setObjectName(_fromUtf8("action100"))
        self.action1000 = QtGui.QAction(MainWindow)
        self.action1000.setText(QtGui.QApplication.translate("MainWindow", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.action1000.setObjectName(_fromUtf8("action1000"))
        self.action10000 = QtGui.QAction(MainWindow)
        self.action10000.setText(QtGui.QApplication.translate("MainWindow", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.action10000.setObjectName(_fromUtf8("action10000"))
        self.action100000 = QtGui.QAction(MainWindow)
        self.action100000.setText(QtGui.QApplication.translate("MainWindow", "100000", None, QtGui.QApplication.UnicodeUTF8))
        self.action100000.setObjectName(_fromUtf8("action100000"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionSystem_information = QtGui.QAction(MainWindow)
        self.actionSystem_information.setText(QtGui.QApplication.translate("MainWindow", "System Information...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSystem_information.setObjectName(_fromUtf8("actionSystem_information"))
        self.actionNetwork_Information = QtGui.QAction(MainWindow)
        self.actionNetwork_Information.setText(QtGui.QApplication.translate("MainWindow", "Network Information...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNetwork_Information.setObjectName(_fromUtf8("actionNetwork_Information"))
        self.actionClose_this_window = QtGui.QAction(MainWindow)
        self.actionClose_this_window.setText(QtGui.QApplication.translate("MainWindow", "Close this window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_this_window.setObjectName(_fromUtf8("actionClose_this_window"))
        self.actionClose_all_and_exit = QtGui.QAction(MainWindow)
        self.actionClose_all_and_exit.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_all_and_exit.setObjectName(_fromUtf8("actionClose_all_and_exit"))
        self.actionColor_legend = QtGui.QAction(MainWindow)
        self.actionColor_legend.setText(QtGui.QApplication.translate("MainWindow", "Color legend", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColor_legend.setObjectName(_fromUtf8("actionColor_legend"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setText(QtGui.QApplication.translate("MainWindow", "---", None, QtGui.QApplication.UnicodeUTF8))
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionLog = QtGui.QAction(MainWindow)
        self.actionLog.setText(QtGui.QApplication.translate("MainWindow", "Log", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLog.setObjectName(_fromUtf8("actionLog"))
        self.menuFile.addAction(self.actionClose_all_and_exit)
        self.menuOptions.addAction(self.actionShow_process_from_all_users)
        self.menuView.addAction(self.actionSystem_information)
        self.menuView.addAction(self.actionNetwork_Information)
        self.menuProcess.addAction(self.actionSet_affinity)
        self.menuProcess.addAction(self.actionSet_priority)
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.actionKill_process)
        self.menuProcess.addAction(self.actionKill_process_tree)
        self.menuProcess.addAction(self.actionSuspend_process)
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.actionProperties)
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionSaveSettings)
        self.menuHelp.addAction(self.actionColor_legend)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLog)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

from PyQt4.Qwt5 import QwtPlot

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

