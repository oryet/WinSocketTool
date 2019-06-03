# -*- coding: utf-8 -*-
import logging
import logging.config
import sys
from PyQt5 import QtWidgets
from MainWindow import MainWindow

__author__ = 'jerry'


def loggingConfig():
    logging.config.fileConfig('logging.conf')
    root_logger = logging.getLogger('root')
    root_logger.debug('Logging System Start')
    logger = logging.getLogger('main')
    logger.info('Logging main Start')


if __name__ == '__main__':
    loggingConfig()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

