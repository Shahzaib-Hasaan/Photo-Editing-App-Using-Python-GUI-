# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FilterApp.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSplitter, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 637)
        # MainWIndow.openmaximized()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(231, 16777215))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)

        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)

        self.flipup = QPushButton(self.frame)
        self.flipup.setObjectName(u"flipup")
        icon = QIcon()
        icon.addFile(u":/Images/down-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.flipup.setIcon(icon)

        self.gridLayout_7.addWidget(self.flipup, 1, 0, 1, 1)

        self.fliplr = QPushButton(self.frame)
        self.fliplr.setObjectName(u"fliplr")
        icon1 = QIcon()
        icon1.addFile(u":/Images/flip1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fliplr.setIcon(icon1)

        self.gridLayout_7.addWidget(self.fliplr, 2, 0, 1, 1)

        self.rotate90 = QPushButton(self.frame)
        self.rotate90.setObjectName(u"rotate90")
        icon2 = QIcon()
        icon2.addFile(u":/Images/rotate-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rotate90.setIcon(icon2)

        self.gridLayout_7.addWidget(self.rotate90, 3, 0, 1, 1)

        self.filter1 = QPushButton(self.frame)
        self.filter1.setObjectName(u"filter1")
        icon3 = QIcon()
        icon3.addFile(u":/Images/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter1.setIcon(icon3)

        self.gridLayout_7.addWidget(self.filter1, 4, 0, 1, 1)

        self.filter2 = QPushButton(self.frame)
        self.filter2.setObjectName(u"filter2")
        icon4 = QIcon()
        icon4.addFile(u":/Images/adjust.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter2.setIcon(icon4)

        self.gridLayout_7.addWidget(self.filter2, 5, 0, 1, 1)

        self.filter3 = QPushButton(self.frame)
        self.filter3.setObjectName(u"filter3")
        icon5 = QIcon()
        icon5.addFile(u":/Images/filter1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter3.setIcon(icon5)

        self.gridLayout_7.addWidget(self.filter3, 6, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_7, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.frame_3)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setMaximumSize(QSize(174, 16777215))
        self.splitter.setOrientation(Qt.Horizontal)
        self.close = QPushButton(self.splitter)
        self.close.setObjectName(u"close")
        self.close.setMaximumSize(QSize(85, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/Images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon6)
        self.splitter.addWidget(self.close)
        self.save = QPushButton(self.splitter)
        self.save.setObjectName(u"save")
        self.save.setMaximumSize(QSize(85, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/Images/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save.setIcon(icon7)
        self.splitter.addWidget(self.save)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 2, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 70))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.path = QLineEdit(self.frame)
        self.path.setObjectName(u"path")

        self.gridLayout_6.addWidget(self.path, 0, 0, 1, 1)

        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_6.addWidget(self.toolButton, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_6)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.imageshow = QLabel(self.frame_2)
        self.imageshow.setObjectName(u"imageshow")
        self.imageshow.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.imageshow, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 847, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Photo Editor", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Apply Filters", None))
        self.flipup.setText(QCoreApplication.translate("MainWindow", u"Flip Vertical", None))
        self.fliplr.setText(QCoreApplication.translate("MainWindow", u"Flip Horizontal", None))
        self.rotate90.setText(QCoreApplication.translate("MainWindow", u"Rotate 90", None))
        self.filter1.setText(QCoreApplication.translate("MainWindow", u"Filter 1", None))
        self.filter2.setText(QCoreApplication.translate("MainWindow", u"Filter 2", None))
        self.filter3.setText(QCoreApplication.translate("MainWindow", u"Filter 3", None))
        self.close.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Photo", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Display Image", None))
        self.imageshow.setText("")
    # retranslateUi

