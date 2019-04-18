# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'socketSetDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 342)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 290, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 371, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_IP = QtWidgets.QLabel(self.tab)
        self.label_IP.setGeometry(QtCore.QRect(79, 61, 69, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_IP.setFont(font)
        self.label_IP.setObjectName("label_IP")
        self.OpenSocketButton = QtWidgets.QPushButton(self.tab)
        self.OpenSocketButton.setGeometry(QtCore.QRect(134, 130, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenSocketButton.sizePolicy().hasHeightForWidth())
        self.OpenSocketButton.setSizePolicy(sizePolicy)
        self.OpenSocketButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OpenSocketButton.setObjectName("OpenSocketButton")
        self.IPPortlineEdit = QtWidgets.QLineEdit(self.tab)
        self.IPPortlineEdit.setGeometry(QtCore.QRect(154, 90, 60, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IPPortlineEdit.sizePolicy().hasHeightForWidth())
        self.IPPortlineEdit.setSizePolicy(sizePolicy)
        self.IPPortlineEdit.setMaxLength(5)
        self.IPPortlineEdit.setObjectName("IPPortlineEdit")
        self.IPlineEdit = QtWidgets.QLineEdit(self.tab)
        self.IPlineEdit.setGeometry(QtCore.QRect(154, 61, 133, 20))
        self.IPlineEdit.setMaxLength(15)
        self.IPlineEdit.setObjectName("IPlineEdit")
        self.label_Port = QtWidgets.QLabel(self.tab)
        self.label_Port.setGeometry(QtCore.QRect(80, 90, 68, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_Port.setFont(font)
        self.label_Port.setObjectName("label_Port")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_IP.setText(_translate("Dialog", "  IP地址：  "))
        self.OpenSocketButton.setText(_translate("Dialog", "开始监听"))
        self.label_Port.setText(_translate("Dialog", "  端口号：  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Socket设置"))


