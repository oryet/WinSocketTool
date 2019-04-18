from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from MainWnd_UiHandler import MainWnd_UiHandler
from SerialDlg_UiHandler import SerialDlg_UiHandler
import logging
import json
from OpenExcelTestPlan import ExcelPlan
from DownLink import DownLinkThread
import socketServer
import threading
import queue

logger = logging.getLogger('main.MainWindow')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)

        self.qRecv = queue.Queue()
        self.qSocRecv = None
        logger.info('Main Window logger start')
        self.uim = MainWnd_UiHandler(self.qRecv)
        self.uid = SerialDlg_UiHandler()
        self.uim.setupUi(self)
        self.createActions()
        self.test = {"State":"stop", "Num":0, "Index":0, "timeout":0,
                     "SendFrame":None, "Answer":None, "SocketThread":"stop"}
        self.uim.startTestButton.setEnabled(False)

        config = self.loadTestPlanDefaultSettings()
        logger.info(config)
        self.uim.planComboBox.clear()
        planList = []
        for i in range(config['planNum']):
            print(config['plan' + str(i + 1)])
            planList += [config['plan' + str(i + 1)]]
        self.uim.planComboBox.addItems(planList)
        DownLinkThread(self)

    def loggingConfig(self):
        logging.config.fileConfig('logging.conf')
        root_logger = logging.getLogger('root')
        root_logger.debug('Logging System Start')

        logger = logging.getLogger('main')
        logger.info('Logging main Start')

    def loadTestPlanDefaultSettings(self):
        try:
            planConfigFile = open("configplan.json")
            defaultPlanConfig = json.load(planConfigFile)
            print(defaultPlanConfig)
        finally:
            if planConfigFile:
                planConfigFile.close()
                return defaultPlanConfig

    def loadSerialDefaultSettings(self):
        try:
            configFile = open("config.json")
            defaultConfig = json.load(configFile)
            print(defaultConfig)
        finally:
            if configFile:
                configFile.close()
                return defaultConfig

    def closeDlgReEvent(self):
        # self.uid.dia.hide()  # 隐藏此窗口
        # self.mainWindow = Ui_MainWindow()
        # self.uim.show()  # 显示登录窗口
        logger.info('SerialDlgWindow closeEvent')

    def closeDlgAcEvent(self):
        ip = self.uid.dia.IPlineEdit.text()
        ipport = int(self.uid.dia.IPPortlineEdit.text())
        config = {"ip":ip, "ipport":ipport}
        configFile = json.dumps(config)
        try:
            f = open("config.json", 'w')
            f.write(configFile)
        finally:
            f.close()

    def closeEvent(self, e):
        """
        This will called when user close the window. save the configurations here.
        :param e:
        :return: Nothing
        TODO: Can this be placed in a better place?
        """
        reply = QtWidgets.QMessageBox.question(self, '警告', '退出后测试将停止,\n你确认要退出吗？', \
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            if self.uid.flags["__isopen__"] is True:
                self.uid.flags = {"__isopen__": False, "__datatype__": "ascii"}
            socketServer.ServerClose()
            e.accept()
        else:
            e.ignore()

    def createActions(self):
        # 串口设置窗口事件
        self.uid.dia.buttonBox.accepted.connect(self.closeDlgAcEvent)
        self.uid.dia.buttonBox.rejected.connect(self.closeDlgReEvent)
        self.uid.dia.OpenSocketButton.clicked.connect(self._btnSocketEvent)

        # 主窗口事件
        self.uim.BaseInfoButton.clicked.connect(self._btnSetEvent)
        self.uim.planButton.clicked.connect(self._btnTestPlanEvent)
        self.uim.startTestButton.clicked.connect(self._btnStartTest)

    # socket功能
    def _btnSocketEvent(self):
        if self.test["SocketThread"] is "stop":
            self.test["SocketThread"] = "run"
            self.uid.dia.OpenSocketButton.setText("监听中")
            # ADDRESS = ('192.168.127.16', 8888)  # 绑定地址
            ip = self.uid.dia.IPlineEdit.text()
            ipport = self.uid.dia.IPPortlineEdit.text()
            print(ip, ipport)
            ADDRESS = (ip, int(ipport))  # 绑定地址
            tser = threading.Thread(target=socketServer.ServerStart, args=(ADDRESS,))
            tser.start()
            tmonitor = threading.Thread(target=socketServer.ServerMonitor, args=(self.qRecv,))
            tmonitor.start()
        else:
            self.test["SocketThread"] = "stop"
            self.uid.dia.OpenSocketButton.setText("启动监听")
            # 关闭监听服务器
            socketServer.ServerClose()
            # 关闭监听报文处理线程
            # TODO


    # 串口设置功能
    def _btnSetEvent(self):
        config = self.loadSerialDefaultSettings()
        self.uid.dia.IPlineEdit.setText(config['ip'])
        self.uid.dia.IPPortlineEdit.setText(str(config['ipport']))
        self.uid.show()

    # 测试方案载入
    def _btnTestPlanEvent(self):
        planText = self.uim.planComboBox.currentText()
        logger.info(planText)
        self.uim.PlanTextEdit.clear()
        self.plan = ExcelPlan(planText)
        if self.plan.row_count == 0:
            print(planText+" is not exist!")
            logger.info('ExcelPlan ' +planText+" is not exist!")
            return

        showinfo = planText
        num = self.plan.Num()
        self.test["Num"] = num

        self.uim.AnaTableWidget.setColumnCount(6)  # 0：名称，1：命令，2：DI，3：下行数据，4：上行数据，5：结果
        self.uim.AnaTableWidget.setRowCount(num)
        self.uim.AnaTableWidget.setColumnWidth(0, 280)  # 设置j列的宽度

        for i in range(0, num):
            showinfo += self.plan.Name(i) + ':\n' + self.plan.Data(i) + '\n\n'
            self.uim.AnaTableWidget.setItem(i, 0, QTableWidgetItem(self.plan.Name(i)))
            self.uim.AnaTableWidget.setItem(i, 1, QTableWidgetItem(self.plan.Cmd(i)))
            self.uim.AnaTableWidget.setItem(i, 2, QTableWidgetItem(self.plan.Data(i)))
            self.uim.AnaTableWidget.setItem(i, 3, QTableWidgetItem(self.plan.Value(i)))
        self.uim.PlanTextEdit.append(showinfo)
        self.test["State"] = "stop"
        # self.state["__planOK__"] = True
        self.setButtonEnable()

    def _btnStartTest(self):
        text = self.uim.startTestButton.text()
        if text == "测试结束(Socket)":
            self.uim.startTestButton.setText("开始测试(Socket)")
        elif text == "开始测试(Socket)":
            self.test["State"] = "start"
            self.uim.startTestButton.setText("测试中(Socket)")
        elif text == "测试中(Socket)":
            self.test["State"] = "stop"
            self.uim.startTestButton.setText("测试结束(Socket)")
        return


    def setButtonEnable(self):
        if socketServer.GetLinkNum() > 0 and self.test["SocketThread"] is "run" and self.test["Num"] > 0:
            self.uim.startTestButton.setEnabled(True)
        elif socketServer.GetLinkNum() == 0 or self.test["SocketThread"] is "stop":
            self.uim.startTestButton.setEnabled(False)