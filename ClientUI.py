# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClientUIDAWpOC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(659, 471)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sendbox = QTextEdit(self.centralwidget)
        self.sendbox.setObjectName(u"sendbox")
        self.sendbox.setGeometry(QRect(30, 290, 511, 131))
        self.IPbox = QLineEdit(self.centralwidget)
        self.IPbox.setObjectName(u"IPbox")
        self.IPbox.setGeometry(QRect(290, 70, 161, 21))
        self.connectbutton = QPushButton(self.centralwidget)
        self.connectbutton.setObjectName(u"connectbutton")
        self.connectbutton.setGeometry(QRect(490, 70, 91, 61))
        self.recvbox = QTextEdit(self.centralwidget)
        self.recvbox.setObjectName(u"recvbox")
        self.recvbox.setGeometry(QRect(30, 160, 611, 121))
        self.recvbox.setReadOnly(True)
        self.sendbutton = QPushButton(self.centralwidget)
        self.sendbutton.setObjectName(u"sendbutton")
        self.sendbutton.setGeometry(QRect(550, 342, 101, 61))
        self.nicklabel = QLabel(self.centralwidget)
        self.nicklabel.setObjectName(u"nicklabel")
        self.nicklabel.setGeometry(QRect(40, 100, 231, 31))
        self.nickbox = QLineEdit(self.centralwidget)
        self.nickbox.setObjectName(u"nickbox")
        self.nickbox.setGeometry(QRect(290, 110, 161, 21))
        self.heading = QLabel(self.centralwidget)
        self.heading.setObjectName(u"heading")
        self.heading.setGeometry(QRect(130, 0, 371, 61))
        self.IPlabel = QLabel(self.centralwidget)
        self.IPlabel.setObjectName(u"IPlabel")
        self.IPlabel.setGeometry(QRect(100, 60, 161, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 659, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.connectbutton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.sendbutton.setText(QCoreApplication.translate("MainWindow", u"Send Message", None))
        self.nicklabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Please Input Nickname: </span></p></body></html>", None))
        self.heading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">Neon Chat</span><span style=\" font-size:22pt; vertical-align:sub;\">CLIENT</span></p></body></html>", None))
        self.IPlabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Please Input IP: </span></p></body></html>", None))
        reg_ex = QRegExp("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
        input_validator = QRegExpValidator(reg_ex, self.IPbox)
        self.IPbox.setValidator(input_validator)
    # retranslateUi

