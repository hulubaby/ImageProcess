# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(200, 500, 81, 51))
        self.Open.setObjectName("Open")
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(460, 500, 81, 51))
        self.Close.setObjectName("Close")
        self.DispalyLabel = QtWidgets.QLabel(self.centralwidget)
        self.DispalyLabel.setGeometry(QtCore.QRect(0, 0, 781, 491))
        self.DispalyLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.DispalyLabel.setText("")
        self.DispalyLabel.setObjectName("DispalyLabel")
        self.radioButtonCam = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonCam.setGeometry(QtCore.QRect(50, 500, 89, 16))
        self.radioButtonCam.setChecked(True)
        self.radioButtonCam.setObjectName("radioButtonCam")
        self.radioButtonFile = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonFile.setGeometry(QtCore.QRect(50, 530, 89, 16))
        self.radioButtonFile.setObjectName("radioButtonFile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.Close.setText(_translate("MainWindow", "Close"))
        self.radioButtonCam.setText(_translate("MainWindow", "camera"))
        self.radioButtonFile.setText(_translate("MainWindow", "local file"))

