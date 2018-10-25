# -*- coding: utf-8 -*-

" PyQt UI界面输出线程日志程序 "

__author__ = "Pastoral"

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time
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
        self.func.emit(record.message)

class MyThread(QThread):
    #定义信号,定义参数为两个str type
    _signal = pyqtSignal(str)

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        #global Inpath,Outpath
        inFile = Inpath
        confDir = Confpath
        outputDir = Outpath

        logHandler = LoguiHandler(self._signal)
        logHandler.setLevel(logging.DEBUG)
        logger.addHandler(logHandler)

        self._signal.emit("1. 开始处理文件：%s" % inFile)
        self._signal.emit("2. 词典文件加载：%s" % confDir)
        func01()
        self._signal.emit("====数据处理已结束，您现在可以退出程序了。====")       

class MyWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.runButton.clicked.connect(self.run)

        # 实例化一个线程
        self.work = MyThread()
        self.work._signal.connect(self.updateProgress)

    def run(self):

        global Inpath,Outpath   # 全局变量线程可以访问
        Inpath = "UI主线程run"
        Outpath = "UI主线程run"
        self.work.start()

    def updateProgress(self, str):
        self.textBrowser.append('%s %s' % (time.strftime('%Y-%m-%d %H:%M:%S') , str) )

if __name__ == '__main__':

    Inpath = ""
    Outpath = ""
    Confpath = '..\\Supplier\\Knime'

    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.setWindowTitle("PyQt UI界面输出线程日志程序")
    mywindow.show()

    sys.exit(app.exec_())