# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pytesttoolMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BaseInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.BaseInfoButton.setObjectName("BaseInfoButton")
        self.horizontalLayout.addWidget(self.BaseInfoButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 10))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.planComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.planComboBox.setProperty("currentText", "")
        self.planComboBox.setObjectName("planComboBox")
        self.horizontalLayout.addWidget(self.planComboBox)
        self.planButton = QtWidgets.QPushButton(self.centralwidget)
        self.planButton.setObjectName("planButton")
        self.horizontalLayout.addWidget(self.planButton)
        self.socketComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.socketComboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.socketComboBox.setObjectName("socketComboBox")
        self.horizontalLayout.addWidget(self.socketComboBox)
        self.startTestButton = QtWidgets.QPushButton(self.centralwidget)
        self.startTestButton.setObjectName("startTestButton")
        self.horizontalLayout.addWidget(self.startTestButton)
        spacerItem1 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_log = QtWidgets.QWidget()
        self.tab_log.setObjectName("tab_log")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_log)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.RxTextEdit = QtWidgets.QTextEdit(self.tab_log)
        self.RxTextEdit.setObjectName("RxTextEdit")
        self.gridLayout.addWidget(self.RxTextEdit, 0, 0, 1, 1)
        self.PlanTextEdit = QtWidgets.QTextEdit(self.tab_log)
        self.PlanTextEdit.setObjectName("PlanTextEdit")
        self.gridLayout.addWidget(self.PlanTextEdit, 0, 1, 2, 1)
        self.SendTextEdit = QtWidgets.QTextEdit(self.tab_log)
        self.SendTextEdit.setObjectName("SendTextEdit")
        self.gridLayout.addWidget(self.SendTextEdit, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_log, "")
        self.tab_ana = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_ana.sizePolicy().hasHeightForWidth())
        self.tab_ana.setSizePolicy(sizePolicy)
        self.tab_ana.setObjectName("tab_ana")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_ana)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.AnaTableWidget = QtWidgets.QTableWidget(self.tab_ana)
        self.AnaTableWidget.setObjectName("AnaTableWidget")
        self.AnaTableWidget.setColumnCount(0)
        self.AnaTableWidget.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.AnaTableWidget)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_ana, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.planComboBox.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BaseInfoButton.setText(_translate("MainWindow", "基本信息"))
        self.label.setText(_translate("MainWindow", "打开方案："))
        self.planButton.setText(_translate("MainWindow", "确定"))
        self.startTestButton.setText(_translate("MainWindow", "开始测试(Socket)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_log), _translate("MainWindow", "报文"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ana), _translate("MainWindow", "分析"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.action.setText(_translate("MainWindow", "打开方案"))
        self.action_2.setText(_translate("MainWindow", "基本信息"))


