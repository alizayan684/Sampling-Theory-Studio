# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_final.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import classes as cl

class Ui_Sampler(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 782)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: #FFFFFF;\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 14px;\n"
"	background-color: rgb(2, 70, 113);\n"
"\n"
"}\n"
"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);\n"
"	background-color: rgb(0, 0, 57);\n"
"	background-color: rgb(0, 43, 63);\n"
"\n"
"\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 15px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.action2 = QAction(MainWindow)
        self.action2.setObjectName(u"action2")
        self.action3 = QAction(MainWindow)
        self.action3.setObjectName(u"action3")
        self.action4 = QAction(MainWindow)
        self.action4.setObjectName(u"action4")
        self.action5 = QAction(MainWindow)
        self.action5.setObjectName(u"action5")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000;\n"
"}\n"
"\n"
"/* Style for QPushButton */\n"
"QPushButton {\n"
"    background-color: rgb(79, 173, 255);\n"
"	color: rgb(3, 3, 3);\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"	border-color: rgb(64, 147, 255);\n"
"    padding: 5px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border-color: rgb(1, 2, 3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" background-color: #333;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"/* Style for QLabel */\n"
"QLabel {\n"
"color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 17px;\n"
"    padding: 5px;\n"
"    border: 1px solid #cccccc;\n"
"	border-color: rgb(91, 91, 91);\n"
"    border-radius: 5px;\n"
"}\n"
"/* Slider */\n"
"QSlider {\n"
"    background-color: transp"
                        "arent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #b1b1b1;\n"
"    height: 8px;\n"
"    background-color: #f1f1f1;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    border: none;\n"
"	background-color: rgb(0, 62, 120);\n"
"    height: 16px;\n"
"    width: 16px;\n"
"    margin: -4px 0;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background-color: rgb(0, 89, 255);\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    \n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.browseSignalButton = QPushButton(self.widget)
        self.browseSignalButton.setObjectName(u"browseSignalButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseSignalButton.sizePolicy().hasHeightForWidth())
        self.browseSignalButton.setSizePolicy(sizePolicy)
        self.browseSignalButton.setMinimumSize(QSize(0, 0))
        self.browseSignalButton.setMaximumSize(QSize(300, 200))

        self.horizontalLayout_12.addWidget(self.browseSignalButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(50, 0))
        self.label_13.setMaximumSize(QSize(16777215, 100))
        self.label_13.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_13)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.samplingFreqSlider = QSlider(self.widget)
        self.samplingFreqSlider.setObjectName(u"samplingFreqSlider")
        sizePolicy.setHeightForWidth(self.samplingFreqSlider.sizePolicy().hasHeightForWidth())
        self.samplingFreqSlider.setSizePolicy(sizePolicy)
        self.samplingFreqSlider.setMinimumSize(QSize(50, 0))
        self.samplingFreqSlider.setMaximumSize(QSize(16777215, 100))
        self.samplingFreqSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.samplingFreqSlider)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.normFreqLCD = QLCDNumber(self.widget)
        self.normFreqLCD.setObjectName(u"normFreqLCD")
        sizePolicy.setHeightForWidth(self.normFreqLCD.sizePolicy().hasHeightForWidth())
        self.normFreqLCD.setSizePolicy(sizePolicy)
        self.normFreqLCD.setMinimumSize(QSize(0, 0))
        self.normFreqLCD.setMaximumSize(QSize(100, 200))
        self.normFreqLCD.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")

        self.verticalLayout_7.addWidget(self.normFreqLCD)

        self.actualFreqLCD = QLCDNumber(self.widget)
        self.actualFreqLCD.setObjectName(u"actualFreqLCD")
        sizePolicy.setHeightForWidth(self.actualFreqLCD.sizePolicy().hasHeightForWidth())
        self.actualFreqLCD.setSizePolicy(sizePolicy)
        self.actualFreqLCD.setMinimumSize(QSize(0, 0))
        self.actualFreqLCD.setMaximumSize(QSize(100, 200))
        self.actualFreqLCD.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.actualFreqLCD)


        self.horizontalLayout_14.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.fmaxLabel_2 = QLabel(self.widget)
        self.fmaxLabel_2.setObjectName(u"fmaxLabel_2")
        sizePolicy.setHeightForWidth(self.fmaxLabel_2.sizePolicy().hasHeightForWidth())
        self.fmaxLabel_2.setSizePolicy(sizePolicy)
        self.fmaxLabel_2.setMinimumSize(QSize(0, 0))
        self.fmaxLabel_2.setMaximumSize(QSize(100, 200))
        self.fmaxLabel_2.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.fmaxLabel_2)

        self.freqValLabel_2 = QLabel(self.widget)
        self.freqValLabel_2.setObjectName(u"freqValLabel_2")
        sizePolicy.setHeightForWidth(self.freqValLabel_2.sizePolicy().hasHeightForWidth())
        self.freqValLabel_2.setSizePolicy(sizePolicy)
        self.freqValLabel_2.setMinimumSize(QSize(0, 0))
        self.freqValLabel_2.setMaximumSize(QSize(100, 200))
        self.freqValLabel_2.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.freqValLabel_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(50, 0))
        self.label_14.setMaximumSize(QSize(16777215, 100))
        self.label_14.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.signalToNoiseSlider = QSlider(self.widget)
        self.signalToNoiseSlider.setObjectName(u"signalToNoiseSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.signalToNoiseSlider.sizePolicy().hasHeightForWidth())
        self.signalToNoiseSlider.setSizePolicy(sizePolicy1)
        self.signalToNoiseSlider.setMinimumSize(QSize(50, 0))
        self.signalToNoiseSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.signalToNoiseSlider)

        self.signalToNoiseLCD = QLCDNumber(self.widget)
        self.signalToNoiseLCD.setObjectName(u"signalToNoiseLCD")
        sizePolicy.setHeightForWidth(self.signalToNoiseLCD.sizePolicy().hasHeightForWidth())
        self.signalToNoiseLCD.setSizePolicy(sizePolicy)
        self.signalToNoiseLCD.setMinimumSize(QSize(0, 0))
        self.signalToNoiseLCD.setMaximumSize(QSize(50, 200))
        self.signalToNoiseLCD.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_15.addWidget(self.signalToNoiseLCD)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.clearAllButton = QPushButton(self.widget)
        self.clearAllButton.setObjectName(u"clearAllButton")
        sizePolicy.setHeightForWidth(self.clearAllButton.sizePolicy().hasHeightForWidth())
        self.clearAllButton.setSizePolicy(sizePolicy)
        self.clearAllButton.setMaximumSize(QSize(300, 200))

        self.verticalLayout_4.addWidget(self.clearAllButton)

        
        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(50, 0))
        self.label_19.setMaximumSize(QSize(16777215, 100))
        self.label_19.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"border: 2px solid;\n"
"	border-color: rgb(0, 157, 255);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.label_19)
        self.constructMethodComboBox = QComboBox(self.widget)
        self.constructMethodComboBox.addItem("")
        self.constructMethodComboBox.addItem("")
        self.constructMethodComboBox.addItem("")
        self.constructMethodComboBox.addItem("")
        self.constructMethodComboBox.setObjectName(u"constructMethodComboBox")
        sizePolicy.setHeightForWidth(self.constructMethodComboBox.sizePolicy().hasHeightForWidth())
        self.constructMethodComboBox.setSizePolicy(sizePolicy)
        self.constructMethodComboBox.setMinimumSize(QSize(203, 30))
        self.constructMethodComboBox.setMaximumSize(QSize(51000, 200))
        self.constructMethodComboBox.setStyleSheet(u" font-size: 16px; /* Font size */\n"
"    padding: 2px; /* Padding around the text */\n"
"    border: 2px solid ; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\"")

        self.verticalLayout_4.addWidget(self.constructMethodComboBox)
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(50, 0))
        self.label_15.setMaximumSize(QSize(16777215, 100))
        self.label_15.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 22, 53);\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 17px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(50, 0))
        self.label_16.setMaximumSize(QSize(16777215, 100))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_16)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.amplitudeComposerSlider = QSlider(self.widget)
        self.amplitudeComposerSlider.setObjectName(u"amplitudeComposerSlider")
        sizePolicy1.setHeightForWidth(self.amplitudeComposerSlider.sizePolicy().hasHeightForWidth())
        self.amplitudeComposerSlider.setSizePolicy(sizePolicy1)
        self.amplitudeComposerSlider.setMinimumSize(QSize(50, 0))
        self.amplitudeComposerSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.amplitudeComposerSlider)

        self.amplitudeComposerLCD = QLCDNumber(self.widget)
        self.amplitudeComposerLCD.setObjectName(u"amplitudeComposerLCD")
        sizePolicy.setHeightForWidth(self.amplitudeComposerLCD.sizePolicy().hasHeightForWidth())
        self.amplitudeComposerLCD.setSizePolicy(sizePolicy)
        self.amplitudeComposerLCD.setMinimumSize(QSize(50, 0))
        self.amplitudeComposerLCD.setMaximumSize(QSize(50, 100))
        self.amplitudeComposerLCD.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_16.addWidget(self.amplitudeComposerLCD)

        self.freqValLabel_4 = QLabel(self.widget)
        self.freqValLabel_4.setObjectName(u"freqValLabel_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.freqValLabel_4.sizePolicy().hasHeightForWidth())
        self.freqValLabel_4.setSizePolicy(sizePolicy2)
        self.freqValLabel_4.setMinimumSize(QSize(0, 0))
        self.freqValLabel_4.setMaximumSize(QSize(40, 200))
        self.freqValLabel_4.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_16.addWidget(self.freqValLabel_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(50, 0))
        self.label_17.setMaximumSize(QSize(16777215, 100))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_17)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.freqComposerSlider = QSlider(self.widget)
        self.freqComposerSlider.setObjectName(u"freqComposerSlider")
        sizePolicy1.setHeightForWidth(self.freqComposerSlider.sizePolicy().hasHeightForWidth())
        self.freqComposerSlider.setSizePolicy(sizePolicy1)
        self.freqComposerSlider.setMinimumSize(QSize(50, 0))
        self.freqComposerSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_17.addWidget(self.freqComposerSlider)

        self.freqComposerLCD = QLCDNumber(self.widget)
        self.freqComposerLCD.setObjectName(u"freqComposerLCD")
        sizePolicy.setHeightForWidth(self.freqComposerLCD.sizePolicy().hasHeightForWidth())
        self.freqComposerLCD.setSizePolicy(sizePolicy)
        self.freqComposerLCD.setMinimumSize(QSize(50, 0))
        self.freqComposerLCD.setMaximumSize(QSize(50, 100))
        self.freqComposerLCD.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_17.addWidget(self.freqComposerLCD)

        self.freqValLabel_3 = QLabel(self.widget)
        self.freqValLabel_3.setObjectName(u"freqValLabel_3")
        sizePolicy2.setHeightForWidth(self.freqValLabel_3.sizePolicy().hasHeightForWidth())
        self.freqValLabel_3.setSizePolicy(sizePolicy2)
        self.freqValLabel_3.setMinimumSize(QSize(0, 0))
        self.freqValLabel_3.setMaximumSize(QSize(40, 200))
        self.freqValLabel_3.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.freqValLabel_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addSignalComposerButton = QPushButton(self.widget)
        self.addSignalComposerButton.setObjectName(u"addSignalComposerButton")
        sizePolicy.setHeightForWidth(self.addSignalComposerButton.sizePolicy().hasHeightForWidth())
        self.addSignalComposerButton.setSizePolicy(sizePolicy)
        self.addSignalComposerButton.setMinimumSize(QSize(0, 0))
        self.addSignalComposerButton.setMaximumSize(QSize(300, 250))

        self.horizontalLayout_2.addWidget(self.addSignalComposerButton)

        self.removeSignalButton = QPushButton(self.widget)
        self.removeSignalButton.setObjectName(u"removeSignalButton")
        sizePolicy.setHeightForWidth(self.removeSignalButton.sizePolicy().hasHeightForWidth())
        self.removeSignalButton.setSizePolicy(sizePolicy)
        self.removeSignalButton.setMinimumSize(QSize(0, 0))
        self.removeSignalButton.setMaximumSize(QSize(200, 200))

        self.horizontalLayout_2.addWidget(self.removeSignalButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.removeSignalComboBox = QComboBox(self.widget)
        self.removeSignalComboBox.addItem("")
        self.removeSignalComboBox.setObjectName(u"removeSignalComboBox")
        sizePolicy.setHeightForWidth(self.removeSignalComboBox.sizePolicy().hasHeightForWidth())
        self.removeSignalComboBox.setSizePolicy(sizePolicy)
        self.removeSignalComboBox.setMinimumSize(QSize(200, 30))
        self.removeSignalComboBox.setMaximumSize(QSize(5000, 200))
        self.removeSignalComboBox.setStyleSheet(u" font-size: 16px; /* Font size */\n"
"    padding: 2px; /* Padding around the text */\n"
"    border: 2px solid ; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\"")

        self.horizontalLayout_18.addWidget(self.removeSignalComboBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(50, 0))
        self.label_18.setMaximumSize(QSize(16777215, 100))
        self.label_18.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 22, 53);\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 17px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_18)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.testComboBox = QComboBox(self.widget)
        self.testComboBox.addItem("")
        self.testComboBox.addItem("")
        self.testComboBox.addItem("")
        self.testComboBox.addItem("")
        self.testComboBox.setObjectName(u"testComboBox")
        sizePolicy2.setHeightForWidth(self.testComboBox.sizePolicy().hasHeightForWidth())
        self.testComboBox.setSizePolicy(sizePolicy2)
        self.testComboBox.setMinimumSize(QSize(100, 30))
        self.testComboBox.setMaximumSize(QSize(120, 200))
        self.testComboBox.setStyleSheet(u" font-size: 16px; /* Font size */\n"
"    padding: 2px; /* Padding around the text */\n"
"    border: 2px solid ; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\"")

        self.horizontalLayout.addWidget(self.testComboBox)

        self.generateTestButton = QPushButton(self.widget)
        self.generateTestButton.setObjectName(u"generateTestButton")
        sizePolicy.setHeightForWidth(self.generateTestButton.sizePolicy().hasHeightForWidth())
        self.generateTestButton.setSizePolicy(sizePolicy)
        self.generateTestButton.setMinimumSize(QSize(0, 0))
        self.generateTestButton.setMaximumSize(QSize(200, 200))

        self.horizontalLayout.addWidget(self.generateTestButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.originalSignalPlot = cl.OriginalSignalGraph(self.centralwidget)  # make this an object of the originalSignalGraph class in the 'MainWindow.py'.
        self.originalSignalPlot.setObjectName(u"originalSignalPlot")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.originalSignalPlot.sizePolicy().hasHeightForWidth())
        self.originalSignalPlot.setSizePolicy(sizePolicy3)
        self.originalSignalPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    border: 2px solid; /* Border color */\n"
"border-color: rgb(0, 230, 255);\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_3.addWidget(self.originalSignalPlot)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_9)

        self.sampledSignalPlot = cl.ReconstructedSignalGraph(self.centralwidget)
        self.sampledSignalPlot.setObjectName(u"sampledSignalPlot")
        sizePolicy3.setHeightForWidth(self.sampledSignalPlot.sizePolicy().hasHeightForWidth())
        self.sampledSignalPlot.setSizePolicy(sizePolicy3)
        self.sampledSignalPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    border: 2px solid; /* Border color */\n"
"border-color: rgb(0, 230, 255);\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.verticalLayout_3.addWidget(self.sampledSignalPlot)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.differencePlot = cl.DifferenceGraph(self.centralwidget)
        self.differencePlot.setObjectName(u"differencePlot")
        sizePolicy3.setHeightForWidth(self.differencePlot.sizePolicy().hasHeightForWidth())
        self.differencePlot.setSizePolicy(sizePolicy3)
        self.differencePlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    border: 2px solid; /* Border color */\n"
"border-color: rgb(0, 230, 255);\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.verticalLayout_3.addWidget(self.differencePlot)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frequencyDomainPlot = cl.FreqSignalGraph([5], self.centralwidget)
        self.frequencyDomainPlot.setObjectName(u"frequencyDomainPlot")
        sizePolicy3.setHeightForWidth(self.frequencyDomainPlot.sizePolicy().hasHeightForWidth())
        self.frequencyDomainPlot.setSizePolicy(sizePolicy3)
        self.frequencyDomainPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    border: 2px solid; /* Border color */\n"
"border-color: rgb(0, 230, 255);\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_4.addWidget(self.frequencyDomainPlot)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.action3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.action4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.action5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.browseSignalButton.setText(QCoreApplication.translate("MainWindow", u"Browse Signal", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sampling Frequency", None))
        self.fmaxLabel_2.setText(QCoreApplication.translate("MainWindow", u"fmax", None))
        self.freqValLabel_2.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Signal To Noise Ratio", None))
        self.clearAllButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Signal Composer", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.freqValLabel_4.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.freqValLabel_3.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.addSignalComposerButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.removeSignalButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.removeSignalComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Signal 1 | Amp : 1mV | Freq : 5Hz", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Testing Senarios", None))
        self.testComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.testComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.testComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.testComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.generateTestButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Original Signal", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Reconstructed Signal", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Construction Error", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Frequency Domain", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Construction Method", None))

        self.constructMethodComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"whittaker shannon", None))
        self.constructMethodComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Fourier Series", None))
        self.constructMethodComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Akima Interpolation", None))
        self.constructMethodComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Rectangular Interpolation", None))
    # retranslateUi