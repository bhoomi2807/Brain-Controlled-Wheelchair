# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(783, 531)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.imageLabel = QtGui.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(120, 200, 511, 121))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(533, 50, 141, 71))
        self.lcdNumber.setAutoFillBackground(True)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 360, 191, 40))
        self.label.setObjectName(_fromUtf8("label"))
        self.currentLabel = QtGui.QLabel(self.centralwidget)
        self.currentLabel.setGeometry(QtCore.QRect(590, 410, 161, 31))
        self.currentLabel.setObjectName(_fromUtf8("currentLabel"))
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(120, 140, 511, 50))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Wheelchair Control", None))
        self.imageLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">STOP</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Currrent State</span></p></body></html>", None))
        self.currentLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#5500ff;\">STOP</span></p></body></html>", None))
        self.statusLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#5500ff;\">Status</span></p></body></html>", None))

import dimages_rc
