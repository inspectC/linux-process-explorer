# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processdetails.ui'
#
# Created: Mon Dec 10 09:43:38 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(684, 647)
        Dialog.setBaseSize(QtCore.QSize(0, 1000))
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(178, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonOK = QtGui.QPushButton(Dialog)
        self.pushButtonOK.setText(QtGui.QApplication.translate("Dialog", "&OK", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOK.setObjectName(_fromUtf8("pushButtonOK"))
        self.horizontalLayout.addWidget(self.pushButtonOK)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 500))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 1500))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.image = QtGui.QWidget()
        self.image.setObjectName(_fromUtf8("image"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.image)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox_7 = QtGui.QGroupBox(self.image)
        self.groupBox_7.setTitle(QtGui.QApplication.translate("Dialog", "Image file", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_2 = QtGui.QLabel(self.groupBox_7)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setMargin(5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.imagePathLabel = QtGui.QLabel(self.groupBox_7)
        self.imagePathLabel.setText(_fromUtf8(""))
        self.imagePathLabel.setObjectName(_fromUtf8("imagePathLabel"))
        self.horizontalLayout_8.addWidget(self.imagePathLabel)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_3 = QtGui.QLabel(self.groupBox_7)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Command line:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setMargin(5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_9.addWidget(self.label_3)
        self.imageCommandLineLabel = QtGui.QLabel(self.groupBox_7)
        self.imageCommandLineLabel.setText(_fromUtf8(""))
        self.imageCommandLineLabel.setObjectName(_fromUtf8("imageCommandLineLabel"))
        self.horizontalLayout_9.addWidget(self.imageCommandLineLabel)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_4 = QtGui.QLabel(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Current directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setMargin(5)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_10.addWidget(self.label_4)
        self.imagePwdLabel = QtGui.QLabel(self.groupBox_7)
        self.imagePwdLabel.setText(_fromUtf8(""))
        self.imagePwdLabel.setObjectName(_fromUtf8("imagePwdLabel"))
        self.horizontalLayout_10.addWidget(self.imagePwdLabel)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_5 = QtGui.QLabel(self.groupBox_7)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Started (UTC):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setMargin(5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        self.imageStartedLabel = QtGui.QLabel(self.groupBox_7)
        self.imageStartedLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.imageStartedLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.imageStartedLabel.setText(_fromUtf8(""))
        self.imageStartedLabel.setObjectName(_fromUtf8("imageStartedLabel"))
        self.horizontalLayout_11.addWidget(self.imageStartedLabel)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_6 = QtGui.QLabel(self.groupBox_7)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Pid:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setMargin(5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_12.addWidget(self.label_6)
        self.imagePidLabel = QtGui.QLabel(self.groupBox_7)
        self.imagePidLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.imagePidLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.imagePidLabel.setText(_fromUtf8(""))
        self.imagePidLabel.setObjectName(_fromUtf8("imagePidLabel"))
        self.horizontalLayout_12.addWidget(self.imagePidLabel)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_7 = QtGui.QLabel(self.groupBox_7)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "PPid:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setMargin(5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_13.addWidget(self.label_7)
        self.imagePPidLabel = QtGui.QLabel(self.groupBox_7)
        self.imagePPidLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.imagePPidLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.imagePPidLabel.setText(_fromUtf8(""))
        self.imagePPidLabel.setObjectName(_fromUtf8("imagePPidLabel"))
        self.horizontalLayout_13.addWidget(self.imagePPidLabel)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.verticalLayout_7.addWidget(self.groupBox_7)
        self.groupBox_8 = QtGui.QGroupBox(self.image)
        self.groupBox_8.setTitle(QtGui.QApplication.translate("Dialog", "Shared objects linked at startup (using ldd)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.libraryTextEdit = QtGui.QTextEdit(self.groupBox_8)
        self.libraryTextEdit.setEnabled(True)
        self.libraryTextEdit.setObjectName(_fromUtf8("libraryTextEdit"))
        self.horizontalLayout_14.addWidget(self.libraryTextEdit)
        self.verticalLayout_7.addWidget(self.groupBox_8)
        self.tabWidget.addTab(self.image, _fromUtf8(""))
        self.performanceGraph = QtGui.QWidget()
        self.performanceGraph.setObjectName(_fromUtf8("performanceGraph"))
        self.gridLayout_2 = QtGui.QGridLayout(self.performanceGraph)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.performanceGraph)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "CPU usage", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.actualCpu = QtGui.QProgressBar(self.groupBox_3)
        self.actualCpu.setMinimumSize(QtCore.QSize(30, 0))
        self.actualCpu.setProperty("value", 24)
        self.actualCpu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.actualCpu.setTextVisible(False)
        self.actualCpu.setOrientation(QtCore.Qt.Vertical)
        self.actualCpu.setInvertedAppearance(False)
        self.actualCpu.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.actualCpu.setObjectName(_fromUtf8("actualCpu"))
        self.verticalLayout.addWidget(self.actualCpu)
        self.labelActualCpuUsage = QtGui.QLabel(self.groupBox_3)
        self.labelActualCpuUsage.setText(QtGui.QApplication.translate("Dialog", "100%", None, QtGui.QApplication.UnicodeUTF8))
        self.labelActualCpuUsage.setObjectName(_fromUtf8("labelActualCpuUsage"))
        self.verticalLayout.addWidget(self.labelActualCpuUsage)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.performanceGraph)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "CPU Usage history", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.qwtPlotCpuHist = QwtPlot(self.groupBox_2)
        self.qwtPlotCpuHist.setObjectName(_fromUtf8("qwtPlotCpuHist"))
        self.horizontalLayout_5.addWidget(self.qwtPlotCpuHist)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.performanceGraph)
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "Private bytes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.actualRss = QtGui.QProgressBar(self.groupBox_4)
        self.actualRss.setMinimumSize(QtCore.QSize(30, 0))
        self.actualRss.setProperty("value", 24)
        self.actualRss.setTextVisible(False)
        self.actualRss.setOrientation(QtCore.Qt.Vertical)
        self.actualRss.setObjectName(_fromUtf8("actualRss"))
        self.verticalLayout_2.addWidget(self.actualRss)
        self.labelActualRss = QtGui.QLabel(self.groupBox_4)
        self.labelActualRss.setText(QtGui.QApplication.translate("Dialog", "1200Kb", None, QtGui.QApplication.UnicodeUTF8))
        self.labelActualRss.setObjectName(_fromUtf8("labelActualRss"))
        self.verticalLayout_2.addWidget(self.labelActualRss)
        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.performanceGraph)
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Private bytes history", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.qwtPlotRssHist = QwtPlot(self.groupBox)
        self.qwtPlotRssHist.setObjectName(_fromUtf8("qwtPlotRssHist"))
        self.horizontalLayout_4.addWidget(self.qwtPlotRssHist)
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.performanceGraph)
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Dialog", "IO Bytes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.actualIo = QtGui.QProgressBar(self.groupBox_5)
        self.actualIo.setMinimumSize(QtCore.QSize(30, 0))
        self.actualIo.setProperty("value", 24)
        self.actualIo.setTextVisible(False)
        self.actualIo.setOrientation(QtCore.Qt.Vertical)
        self.actualIo.setObjectName(_fromUtf8("actualIo"))
        self.verticalLayout_3.addWidget(self.actualIo)
        self.labelActualIo = QtGui.QLabel(self.groupBox_5)
        self.labelActualIo.setText(QtGui.QApplication.translate("Dialog", "1MB/s", None, QtGui.QApplication.UnicodeUTF8))
        self.labelActualIo.setObjectName(_fromUtf8("labelActualIo"))
        self.verticalLayout_3.addWidget(self.labelActualIo)
        self.gridLayout_2.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.IO = QtGui.QGroupBox(self.performanceGraph)
        self.IO.setTitle(QtGui.QApplication.translate("Dialog", "IO Bytes history", None, QtGui.QApplication.UnicodeUTF8))
        self.IO.setObjectName(_fromUtf8("IO"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.IO)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.qwtPlotIoHist = QwtPlot(self.IO)
        self.qwtPlotIoHist.setObjectName(_fromUtf8("qwtPlotIoHist"))
        self.horizontalLayout_2.addWidget(self.qwtPlotIoHist)
        self.gridLayout_2.addWidget(self.IO, 2, 1, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.performanceGraph)
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Dialog", "TCPIP Bytes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.actualTcpip = QtGui.QProgressBar(self.groupBox_6)
        self.actualTcpip.setMinimumSize(QtCore.QSize(30, 0))
        self.actualTcpip.setProperty("value", 24)
        self.actualTcpip.setTextVisible(False)
        self.actualTcpip.setOrientation(QtCore.Qt.Vertical)
        self.actualTcpip.setObjectName(_fromUtf8("actualTcpip"))
        self.verticalLayout_5.addWidget(self.actualTcpip)
        self.labelActualTcpip = QtGui.QLabel(self.groupBox_6)
        self.labelActualTcpip.setText(QtGui.QApplication.translate("Dialog", "1MB/s", None, QtGui.QApplication.UnicodeUTF8))
        self.labelActualTcpip.setObjectName(_fromUtf8("labelActualTcpip"))
        self.verticalLayout_5.addWidget(self.labelActualTcpip)
        self.gridLayout_2.addWidget(self.groupBox_6, 3, 0, 1, 1)
        self.IO_2 = QtGui.QGroupBox(self.performanceGraph)
        self.IO_2.setTitle(QtGui.QApplication.translate("Dialog", "TCPIP Bytes history", None, QtGui.QApplication.UnicodeUTF8))
        self.IO_2.setObjectName(_fromUtf8("IO_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.IO_2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.qwtPlotTcpipHist = QwtPlot(self.IO_2)
        self.qwtPlotTcpipHist.setObjectName(_fromUtf8("qwtPlotTcpipHist"))
        self.horizontalLayout_7.addWidget(self.qwtPlotTcpipHist)
        self.gridLayout_2.addWidget(self.IO_2, 3, 1, 1, 1)
        self.tabWidget.addTab(self.performanceGraph, _fromUtf8(""))
        self.tcpip = QtGui.QWidget()
        self.tcpip.setObjectName(_fromUtf8("tcpip"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tcpip)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.tcpipTableWidget = QtGui.QTableWidget(self.tcpip)
        self.tcpipTableWidget.setObjectName(_fromUtf8("tcpipTableWidget"))
        self.tcpipTableWidget.setColumnCount(8)
        self.tcpipTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Proto", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpipTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "From", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpipTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpipTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpipTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpipTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "State", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpipTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Sent/sec", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpipTableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Rec/Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpipTableWidget.setHorizontalHeaderItem(7, item)
        self.horizontalLayout_6.addWidget(self.tcpipTableWidget)
        self.tabWidget.addTab(self.tcpip, _fromUtf8(""))
        self.environment = QtGui.QWidget()
        self.environment.setObjectName(_fromUtf8("environment"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.environment)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.environment)
        self.label.setText(QtGui.QApplication.translate("Dialog", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.filterEdit = QtGui.QLineEdit(self.environment)
        self.filterEdit.setObjectName(_fromUtf8("filterEdit"))
        self.horizontalLayout_3.addWidget(self.filterEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.environmentText = QtGui.QTextEdit(self.environment)
        self.environmentText.setObjectName(_fromUtf8("environmentText"))
        self.verticalLayout_4.addWidget(self.environmentText)
        self.tabWidget.addTab(self.environment, _fromUtf8(""))
        self.strings = QtGui.QWidget()
        self.strings.setObjectName(_fromUtf8("strings"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.strings)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_11 = QtGui.QLabel(self.strings)
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Not implemented yet!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_11.addWidget(self.label_11)
        self.tabWidget.addTab(self.strings, _fromUtf8(""))
        self.security = QtGui.QWidget()
        self.security.setObjectName(_fromUtf8("security"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.security)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_10 = QtGui.QLabel(self.security)
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Not implemented yet!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_10.addWidget(self.label_10)
        self.tabWidget.addTab(self.security, _fromUtf8(""))
        self.performance = QtGui.QWidget()
        self.performance.setObjectName(_fromUtf8("performance"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.performance)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_8 = QtGui.QLabel(self.performance)
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Not implemented yet!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_8.addWidget(self.label_8)
        self.tabWidget.addTab(self.performance, _fromUtf8(""))
        self.threads = QtGui.QWidget()
        self.threads.setObjectName(_fromUtf8("threads"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.threads)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.threadsTableWidget = QtGui.QTableWidget(self.threads)
        self.threadsTableWidget.setObjectName(_fromUtf8("threadsTableWidget"))
        self.threadsTableWidget.setColumnCount(3)
        self.threadsTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "ThreadID", None, QtGui.QApplication.UnicodeUTF8))
        self.threadsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "WCHAN", None, QtGui.QApplication.UnicodeUTF8))
        self.threadsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Wakeups", None, QtGui.QApplication.UnicodeUTF8))
        self.threadsTableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_9.addWidget(self.threadsTableWidget)
        self.tabWidget.addTab(self.threads, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.image), QtGui.QApplication.translate("Dialog", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.performanceGraph), QtGui.QApplication.translate("Dialog", "Performance Graph", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tcpipTableWidget.horizontalHeaderItem(0)
        item = self.tcpipTableWidget.horizontalHeaderItem(1)
        item = self.tcpipTableWidget.horizontalHeaderItem(2)
        item = self.tcpipTableWidget.horizontalHeaderItem(3)
        item = self.tcpipTableWidget.horizontalHeaderItem(4)
        item = self.tcpipTableWidget.horizontalHeaderItem(5)
        item = self.tcpipTableWidget.horizontalHeaderItem(6)
        item = self.tcpipTableWidget.horizontalHeaderItem(7)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tcpip), QtGui.QApplication.translate("Dialog", "TCP/IP", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.environment), QtGui.QApplication.translate("Dialog", "Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.strings), QtGui.QApplication.translate("Dialog", "Strings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.security), QtGui.QApplication.translate("Dialog", "Security", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.performance), QtGui.QApplication.translate("Dialog", "Performance", None, QtGui.QApplication.UnicodeUTF8))
        item = self.threadsTableWidget.horizontalHeaderItem(0)
        item = self.threadsTableWidget.horizontalHeaderItem(1)
        item = self.threadsTableWidget.horizontalHeaderItem(2)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.threads), QtGui.QApplication.translate("Dialog", "Threads", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4.Qwt5 import QwtPlot
