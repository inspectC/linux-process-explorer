# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Aug 17 21:27:40 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 358)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.qwtPlotOverallCpuHist = Qwt5.QwtPlot(self.frame)
        self.qwtPlotOverallCpuHist.setMinimumSize(QtCore.QSize(150, 0))
        self.qwtPlotOverallCpuHist.setMaximumSize(QtCore.QSize(150, 50))
        self.qwtPlotOverallCpuHist.setObjectName("qwtPlotOverallCpuHist")
        self.horizontalLayout.addWidget(self.qwtPlotOverallCpuHist)
        self.verticalLayout.addWidget(self.frame)
        self.processTreeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.processTreeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.processTreeWidget.setColumnCount(0)
        self.processTreeWidget.setObjectName("processTreeWidget")
        self.processTreeWidget.header().setCascadingSectionResizes(True)
        self.processTreeWidget.header().setDefaultSectionSize(50)
        self.verticalLayout.addWidget(self.processTreeWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuProcess = QtGui.QMenu(self.menubar)
        self.menuProcess.setObjectName("menuProcess")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSet_affinity = QtGui.QAction(MainWindow)
        self.actionSet_affinity.setObjectName("actionSet_affinity")
        self.actionSet_priority = QtGui.QAction(MainWindow)
        self.actionSet_priority.setObjectName("actionSet_priority")
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionKill_process = QtGui.QAction(MainWindow)
        self.actionKill_process.setObjectName("actionKill_process")
        self.actionKill_process_tree = QtGui.QAction(MainWindow)
        self.actionKill_process_tree.setObjectName("actionKill_process_tree")
        self.actionSuspend_process = QtGui.QAction(MainWindow)
        self.actionSuspend_process.setObjectName("actionSuspend_process")
        self.actionProperties = QtGui.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.actionShow_process_from_all_users = QtGui.QAction(MainWindow)
        self.actionShow_process_from_all_users.setObjectName("actionShow_process_from_all_users")
        self.action8 = QtGui.QAction(MainWindow)
        self.action8.setObjectName("action8")
        self.action9 = QtGui.QAction(MainWindow)
        self.action9.setObjectName("action9")
        self.action7 = QtGui.QAction(MainWindow)
        self.action7.setObjectName("action7")
        self.action81 = QtGui.QAction(MainWindow)
        self.action81.setObjectName("action81")
        self.action10 = QtGui.QAction(MainWindow)
        self.action10.setObjectName("action10")
        self.action12 = QtGui.QAction(MainWindow)
        self.action12.setObjectName("action12")
        self.action14 = QtGui.QAction(MainWindow)
        self.action14.setObjectName("action14")
        self.actionSaveSettings = QtGui.QAction(MainWindow)
        self.actionSaveSettings.setObjectName("actionSaveSettings")
        self.actionSent_your_feedback = QtGui.QAction(MainWindow)
        self.actionSent_your_feedback.setObjectName("actionSent_your_feedback")
        self.action10_2 = QtGui.QAction(MainWindow)
        self.action10_2.setObjectName("action10_2")
        self.action100 = QtGui.QAction(MainWindow)
        self.action100.setObjectName("action100")
        self.action1000 = QtGui.QAction(MainWindow)
        self.action1000.setObjectName("action1000")
        self.action10000 = QtGui.QAction(MainWindow)
        self.action10000.setObjectName("action10000")
        self.action100000 = QtGui.QAction(MainWindow)
        self.action100000.setObjectName("action100000")
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSystem_information = QtGui.QAction(MainWindow)
        self.actionSystem_information.setObjectName("actionSystem_information")
        self.actionNetwork_Information = QtGui.QAction(MainWindow)
        self.actionNetwork_Information.setObjectName("actionNetwork_Information")
        self.actionClose_this_window = QtGui.QAction(MainWindow)
        self.actionClose_this_window.setObjectName("actionClose_this_window")
        self.actionClose_all_and_exit = QtGui.QAction(MainWindow)
        self.actionClose_all_and_exit.setObjectName("actionClose_all_and_exit")
        self.actionColor_legend = QtGui.QAction(MainWindow)
        self.actionColor_legend.setObjectName("actionColor_legend")
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionClose_this_window)
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
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Linux Process Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProcess.setTitle(QtGui.QApplication.translate("MainWindow", "Process", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_affinity.setText(QtGui.QApplication.translate("MainWindow", "Set affinity", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_priority.setText(QtGui.QApplication.translate("MainWindow", "Set priority", None, QtGui.QApplication.UnicodeUTF8))
        self.action.setText(QtGui.QApplication.translate("MainWindow", "----", None, QtGui.QApplication.UnicodeUTF8))
        self.actionKill_process.setText(QtGui.QApplication.translate("MainWindow", "Kill process", None, QtGui.QApplication.UnicodeUTF8))
        self.actionKill_process_tree.setText(QtGui.QApplication.translate("MainWindow", "Kill process tree", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSuspend_process.setText(QtGui.QApplication.translate("MainWindow", "Suspend process", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setText(QtGui.QApplication.translate("MainWindow", "Properies", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_process_from_all_users.setText(QtGui.QApplication.translate("MainWindow", "Show process from all users", None, QtGui.QApplication.UnicodeUTF8))
        self.action8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.action9.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.action7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.action81.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.action10.setText(QtGui.QApplication.translate("MainWindow", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.action12.setText(QtGui.QApplication.translate("MainWindow", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.action14.setText(QtGui.QApplication.translate("MainWindow", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveSettings.setText(QtGui.QApplication.translate("MainWindow", "Save current settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSent_your_feedback.setText(QtGui.QApplication.translate("MainWindow", "Send your feedback", None, QtGui.QApplication.UnicodeUTF8))
        self.action10_2.setText(QtGui.QApplication.translate("MainWindow", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.action100.setText(QtGui.QApplication.translate("MainWindow", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.action1000.setText(QtGui.QApplication.translate("MainWindow", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.action10000.setText(QtGui.QApplication.translate("MainWindow", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.action100000.setText(QtGui.QApplication.translate("MainWindow", "100000", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSystem_information.setText(QtGui.QApplication.translate("MainWindow", "System Information...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNetwork_Information.setText(QtGui.QApplication.translate("MainWindow", "Network Information...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_this_window.setText(QtGui.QApplication.translate("MainWindow", "Close this window", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_all_and_exit.setText(QtGui.QApplication.translate("MainWindow", "Close all and exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionColor_legend.setText(QtGui.QApplication.translate("MainWindow", "Color legend", None, QtGui.QApplication.UnicodeUTF8))
        self.action_2.setText(QtGui.QApplication.translate("MainWindow", "---", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import Qwt5

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

