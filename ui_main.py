# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
        MainWindow.resize(643, 389)
        MainWindow.setStyleSheet(u"background-color: rgb(35, 37, 46)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Cantarell Light")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"Courier 10 Pitch")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.txt_link = QLineEdit(self.frame)
        self.txt_link.setObjectName(u"txt_link")
        self.txt_link.setFont(font1)
        self.txt_link.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_link)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.rn_video = QRadioButton(self.frame)
        self.rn_video.setObjectName(u"rn_video")
        font2 = QFont()
        font2.setFamily(u"Courier 10 Pitch")
        font2.setPointSize(12)
        self.rn_video.setFont(font2)

        self.verticalLayout_2.addWidget(self.rn_video)

        self.rn_audio = QRadioButton(self.frame)
        self.rn_audio.setObjectName(u"rn_audio")
        self.rn_audio.setFont(font2)

        self.verticalLayout_2.addWidget(self.rn_audio)

        self.ch_audio = QCheckBox(self.frame)
        self.ch_audio.setObjectName(u"ch_audio")
        self.ch_audio.setFont(font2)
        self.ch_audio.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_2.addWidget(self.ch_audio)

        self.ch_video = QCheckBox(self.frame)
        self.ch_video.setObjectName(u"ch_video")
        self.ch_video.setFont(font2)
        self.ch_video.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_2.addWidget(self.ch_video)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_download = QPushButton(self.frame)
        self.btn_download.setObjectName(u"btn_download")
        font3 = QFont()
        font3.setFamily(u"Courier 10 Pitch")
        font3.setPointSize(13)
        self.btn_download.setFont(font3)

        self.horizontalLayout.addWidget(self.btn_download)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#a50000;\">YouTube Downloader</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">LINK DO VIDEO</span></p></body></html>", None))
        self.txt_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cole o link do texto aqui", None))
        self.rn_video.setText(QCoreApplication.translate("MainWindow", u"V\u00eddeo", None))
        self.rn_audio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.ch_audio.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST AUDIO", None))
        self.ch_video.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST VIDEO", None))
        self.label_2.setText("")
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_3.setText("")
    # retranslateUi

