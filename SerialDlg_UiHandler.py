from StSerial import StSerial
from PyQt5 import QtWidgets
from socketSetDialog import Ui_Dialog
import logging

logger = logging.getLogger('main.MainWindow')


class SerialDlg_UiHandler(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)

        logger.info('Dialog Window logger start')
        self.dia = Ui_Dialog()
        self.flags = {"__isopen__": False, "__datatype__": "ascii"}
        self.dia.setupUi(self)
        self.dia_log = ""

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = SerialDlg_UiHandler()

    ports = mainWindow.serial.searchSerialPort()
    mainWindow.dia.cbbPortName.clear()
    mainWindow.dia.cbbPortName.addItems(ports)

    mainWindow.show()
    sys.exit(app.exec_())