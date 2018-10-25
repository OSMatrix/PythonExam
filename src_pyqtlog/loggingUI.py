# -*- coding: utf-8 -*-

" PyQt UI界面输出日志程序 "

__author__ = "Pastoral"

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time
import logging
from mainui import *
from libExam import *

class LoguiHandler(logging.Handler): 
    def __init__(self, func):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Our custom argument
        self.func = func
    def emit(self, record):
        # record.message is the log message
        self.func(record.message)

class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.runButton.clicked.connect(self.run)

    def run(self):
        logger.debug('Test 1')
        logger.info('Test 2')
        logger.warning('Test 3')
        logger.error('Test 4')
        logger.critical('Test 5')    

        func01()

    def updateProgress(self, str):
        self.textBrowser.append('%s %s' % (time.strftime('%Y-%m-%d %H:%M:%S') , str) )

if __name__ == '__main__':

    logger.setLevel(logging.DEBUG)

    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.setWindowTitle("PyQt UI界面输出日志程序")

    logHandler = LoguiHandler(mywindow.updateProgress)
    logHandler.setLevel(logging.DEBUG)
    logger.addHandler(logHandler)

    mywindow.show()

    sys.exit(app.exec_())