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
        MainWindow.resize(879, 991)
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
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        font = QFont()
        font.setFamilies([u"Segoe UI,Tahoma,Geneva,Verdana,sans-serif"])
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.originalSignalPlot = cl.OriginalSignalGraph(self.centralwidget)
        self.originalSignalPlot.setObjectName(u"originalSignalPlot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.originalSignalPlot.sizePolicy().hasHeightForWidth())
        self.originalSignalPlot.setSizePolicy(sizePolicy)
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
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_9)

        self.sampledSignalPlot = cl.ReconstructedSignalGraph(self.centralwidget)
        self.sampledSignalPlot.setObjectName(u"sampledSignalPlot")
        sizePolicy.setHeightForWidth(self.sampledSignalPlot.sizePolicy().hasHeightForWidth())
        self.sampledSignalPlot.setSizePolicy(sizePolicy)
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
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_11)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.differencePlot = cl.DifferenceGraph(self.centralwidget)
        self.differencePlot.setObjectName(u"differencePlot")
        sizePolicy.setHeightForWidth(self.differencePlot.sizePolicy().hasHeightForWidth())
        self.differencePlot.setSizePolicy(sizePolicy)
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
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frequencyDomainPlot = cl.FreqSignalGraph([5], self.centralwidget)
        self.frequencyDomainPlot.setObjectName(u"frequencyDomainPlot")
        sizePolicy.setHeightForWidth(self.frequencyDomainPlot.sizePolicy().hasHeightForWidth())
        self.frequencyDomainPlot.setSizePolicy(sizePolicy)
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

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(450, 0))
        self.widget.setFont(font)
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
"QLCDNumber {\n"
"	background-color: rgb(3, 22, 53);\n"
"    color: #ffffff;\n"
"    border: 1px solid #555555;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.browseSignalButton = QPushButton(self.widget)
        self.browseSignalButton.setObjectName(u"browseSignalButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.browseSignalButton.sizePolicy().hasHeightForWidth())
        self.browseSignalButton.setSizePolicy(sizePolicy1)
        self.browseSignalButton.setMinimumSize(QSize(0, 0))
        self.browseSignalButton.setMaximumSize(QSize(700, 50))
        self.browseSignalButton.setStyleSheet(u"font-size:18px;")

        self.verticalLayout_4.addWidget(self.browseSignalButton)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMinimumSize(QSize(50, 0))
        self.label_15.setMaximumSize(QSize(16777215, 100))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 22, 53);\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 27px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setMargin(5)

        self.verticalLayout_4.addWidget(self.label_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMinimumSize(QSize(50, 0))
        self.label_16.setMaximumSize(QSize(50, 35))
        self.label_16.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 62, 108);\n"
"    font-size: 15px;\n"
"border: 2px solid;\n"
"\n"
"}\n"
"")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_16)

        self.amplitudeComposerSlider = QSlider(self.widget)
        self.amplitudeComposerSlider.setObjectName(u"amplitudeComposerSlider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.amplitudeComposerSlider.sizePolicy().hasHeightForWidth())
        self.amplitudeComposerSlider.setSizePolicy(sizePolicy2)
        self.amplitudeComposerSlider.setMinimumSize(QSize(50, 0))
        self.amplitudeComposerSlider.setMaximumSize(QSize(16777215, 35))
        self.amplitudeComposerSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.amplitudeComposerSlider)

        self.amplitudeComposerLCD = QLCDNumber(self.widget)
        self.amplitudeComposerLCD.setObjectName(u"amplitudeComposerLCD")
        sizePolicy2.setHeightForWidth(self.amplitudeComposerLCD.sizePolicy().hasHeightForWidth())
        self.amplitudeComposerLCD.setSizePolicy(sizePolicy2)
        self.amplitudeComposerLCD.setMinimumSize(QSize(50, 0))
        self.amplitudeComposerLCD.setMaximumSize(QSize(50, 35))
        self.amplitudeComposerLCD.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_16.addWidget(self.amplitudeComposerLCD)

        self.freqValLabel_4 = QLabel(self.widget)
        self.freqValLabel_4.setObjectName(u"freqValLabel_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.freqValLabel_4.sizePolicy().hasHeightForWidth())
        self.freqValLabel_4.setSizePolicy(sizePolicy3)
        self.freqValLabel_4.setMinimumSize(QSize(0, 0))
        self.freqValLabel_4.setMaximumSize(QSize(40, 35))
        self.freqValLabel_4.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_16.addWidget(self.freqValLabel_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setMinimumSize(QSize(50, 0))
        self.label_17.setMaximumSize(QSize(50, 35))
        self.label_17.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 62, 108);\n"
"    font-size: 15px;\n"
"border: 2px solid;\n"
"\n"
"}\n"
"")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_17)

        self.freqComposerSlider = QSlider(self.widget)
        self.freqComposerSlider.setObjectName(u"freqComposerSlider")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.freqComposerSlider.sizePolicy().hasHeightForWidth())
        self.freqComposerSlider.setSizePolicy(sizePolicy4)
        self.freqComposerSlider.setMinimumSize(QSize(50, 0))
        self.freqComposerSlider.setMaximumSize(QSize(16777215, 35))
        self.freqComposerSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_17.addWidget(self.freqComposerSlider)

        self.freqComposerLCD = QLCDNumber(self.widget)
        self.freqComposerLCD.setObjectName(u"freqComposerLCD")
        sizePolicy1.setHeightForWidth(self.freqComposerLCD.sizePolicy().hasHeightForWidth())
        self.freqComposerLCD.setSizePolicy(sizePolicy1)
        self.freqComposerLCD.setMinimumSize(QSize(50, 0))
        self.freqComposerLCD.setMaximumSize(QSize(50, 35))
        self.freqComposerLCD.setFont(font)
        self.freqComposerLCD.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_17.addWidget(self.freqComposerLCD)

        self.freqValLabel_3 = QLabel(self.widget)
        self.freqValLabel_3.setObjectName(u"freqValLabel_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.freqValLabel_3.sizePolicy().hasHeightForWidth())
        self.freqValLabel_3.setSizePolicy(sizePolicy5)
        self.freqValLabel_3.setMinimumSize(QSize(0, 0))
        self.freqValLabel_3.setMaximumSize(QSize(40, 35))
        self.freqValLabel_3.setStyleSheet(u"")

        self.horizontalLayout_17.addWidget(self.freqValLabel_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setMinimumSize(QSize(50, 0))
        self.label_22.setMaximumSize(QSize(50, 35))
        self.label_22.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 62, 108);\n"
"    font-size: 15px;\n"
"border: 2px solid;\n"
"\n"
"}\n"
"")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_22)

        self.phaseComposerSlider = QSlider(self.widget)
        self.phaseComposerSlider.setObjectName(u"phaseComposerSlider")
        sizePolicy4.setHeightForWidth(self.phaseComposerSlider.sizePolicy().hasHeightForWidth())
        self.phaseComposerSlider.setSizePolicy(sizePolicy4)
        self.phaseComposerSlider.setMinimumSize(QSize(50, 0))
        self.phaseComposerSlider.setMaximumSize(QSize(16777215, 35))
        self.phaseComposerSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_19.addWidget(self.phaseComposerSlider)

        self.phaseComposerLCD = QLCDNumber(self.widget)
        self.phaseComposerLCD.setObjectName(u"phaseComposerLCD")
        sizePolicy1.setHeightForWidth(self.phaseComposerLCD.sizePolicy().hasHeightForWidth())
        self.phaseComposerLCD.setSizePolicy(sizePolicy1)
        self.phaseComposerLCD.setMinimumSize(QSize(45, 0))
        self.phaseComposerLCD.setMaximumSize(QSize(20, 35))
        self.phaseComposerLCD.setFont(font)
        self.phaseComposerLCD.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_19.addWidget(self.phaseComposerLCD)

        self.freqValLabel_5 = QLabel(self.widget)
        self.freqValLabel_5.setObjectName(u"freqValLabel_5")
        sizePolicy5.setHeightForWidth(self.freqValLabel_5.sizePolicy().hasHeightForWidth())
        self.freqValLabel_5.setSizePolicy(sizePolicy5)
        self.freqValLabel_5.setMinimumSize(QSize(45, 0))
        self.freqValLabel_5.setMaximumSize(QSize(40, 35))
        self.freqValLabel_5.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.freqValLabel_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.addSignalComposerButton = QPushButton(self.widget)
        self.addSignalComposerButton.setObjectName(u"addSignalComposerButton")
        sizePolicy2.setHeightForWidth(self.addSignalComposerButton.sizePolicy().hasHeightForWidth())
        self.addSignalComposerButton.setSizePolicy(sizePolicy2)
        self.addSignalComposerButton.setMinimumSize(QSize(0, 0))
        self.addSignalComposerButton.setMaximumSize(QSize(500, 50))

        self.horizontalLayout_20.addWidget(self.addSignalComposerButton)

        self.saveButton = QPushButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)
        self.saveButton.setMaximumSize(QSize(300, 50))

        self.horizontalLayout_20.addWidget(self.saveButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFont(font)
        self.line_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setMinimumSize(QSize(60, 10))
        self.label_23.setMaximumSize(QSize(16777215, 60))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 62, 108);\n"
"    font-size: 14.5px;\n"
"border: 2px solid;\n"
"\n"
"}\n"
"")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_23)

        self.removeSignalComboBox = QComboBox(self.widget)
        self.removeSignalComboBox.addItem("")
        self.removeSignalComboBox.setObjectName(u"removeSignalComboBox")
        sizePolicy1.setHeightForWidth(self.removeSignalComboBox.sizePolicy().hasHeightForWidth())
        self.removeSignalComboBox.setSizePolicy(sizePolicy1)
        self.removeSignalComboBox.setMinimumSize(QSize(200, 30))
        self.removeSignalComboBox.setMaximumSize(QSize(5000, 50))
        self.removeSignalComboBox.setStyleSheet(u" font-size: 16px; /* Font size */\n"
"    padding: 2px; /* Padding around the text */\n"
"    border: 2px solid ; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\"")

        self.horizontalLayout_2.addWidget(self.removeSignalComboBox)

        self.removeSignalButton = QPushButton(self.widget)
        self.removeSignalButton.setObjectName(u"removeSignalButton")
        sizePolicy1.setHeightForWidth(self.removeSignalButton.sizePolicy().hasHeightForWidth())
        self.removeSignalButton.setSizePolicy(sizePolicy1)
        self.removeSignalButton.setMinimumSize(QSize(0, 0))
        self.removeSignalButton.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_2.addWidget(self.removeSignalButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMinimumSize(QSize(50, 0))
        self.label_18.setMaximumSize(QSize(16777215, 50))
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 62, 108);\n"
"    font-size: 14.5px;\n"
"border: 2px solid;\n"
"\n"
"}\n"
"")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setMargin(0)

        self.horizontalLayout_21.addWidget(self.label_18)

        self.testComboBox = QComboBox(self.widget)
        self.testComboBox.addItem("")
        self.testComboBox.addItem("")
        self.testComboBox.addItem("")
        self.testComboBox.addItem("")
        self.testComboBox.setObjectName(u"testComboBox")
        sizePolicy1.setHeightForWidth(self.testComboBox.sizePolicy().hasHeightForWidth())
        self.testComboBox.setSizePolicy(sizePolicy1)
        self.testComboBox.setMinimumSize(QSize(200, 30))
        self.testComboBox.setMaximumSize(QSize(5000, 50))
        self.testComboBox.setStyleSheet(u" font-size: 16px; /* Font size */\n"
"    padding: 2px; /* Padding around the text */\n"
"    border: 2px solid ; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\"")

        self.horizontalLayout_21.addWidget(self.testComboBox)

        self.generateTestButton = QPushButton(self.widget)
        self.generateTestButton.setObjectName(u"generateTestButton")
        sizePolicy1.setHeightForWidth(self.generateTestButton.sizePolicy().hasHeightForWidth())
        self.generateTestButton.setSizePolicy(sizePolicy1)
        self.generateTestButton.setMinimumSize(QSize(0, 0))
        self.generateTestButton.setMaximumSize(QSize(5000, 50))

        self.horizontalLayout_21.addWidget(self.generateTestButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setWindowModality(Qt.NonModal)
        self.line_5.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_5)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 40))
        self.line.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(50, 0))
        self.label_20.setMaximumSize(QSize(16777215, 100))
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 22, 53);\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 27px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setMargin(5)

        self.verticalLayout_4.addWidget(self.label_20)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setMinimumSize(QSize(50, 0))
        self.label_19.setMaximumSize(QSize(16777215, 50))
        self.label_19.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 62, 108);\n"
"    font-size: 15px;\n"
"border: 2px solid;\n"
"\n"
"}\n"
"")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_19)

        self.constructMethodComboBox = QComboBox(self.widget)
        self.constructMethodComboBox.addItem("")
        self.constructMethodComboBox.addItem("")
        self.constructMethodComboBox.addItem("")
        self.constructMethodComboBox.addItem("")
        self.constructMethodComboBox.setObjectName(u"constructMethodComboBox")
        sizePolicy1.setHeightForWidth(self.constructMethodComboBox.sizePolicy().hasHeightForWidth())
        self.constructMethodComboBox.setSizePolicy(sizePolicy1)
        self.constructMethodComboBox.setMinimumSize(QSize(203, 30))
        self.constructMethodComboBox.setMaximumSize(QSize(51000, 50))
        self.constructMethodComboBox.setStyleSheet(u" font-size: 16px; /* Font size */\n"
"    padding: 2px; /* Padding around the text */\n"
"    border: 2px solid ; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\"")

        self.horizontalLayout_7.addWidget(self.constructMethodComboBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(50, 0))
        self.label_13.setMaximumSize(QSize(50, 80))
        self.label_13.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 62, 108);\n"
"    font-size: 15px;\n"
"border: 2px solid;\n"
"\n"
"}\n"
"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.samplingFreqSlider = QSlider(self.widget)
        self.samplingFreqSlider.setObjectName(u"samplingFreqSlider")
        sizePolicy1.setHeightForWidth(self.samplingFreqSlider.sizePolicy().hasHeightForWidth())
        self.samplingFreqSlider.setSizePolicy(sizePolicy1)
        self.samplingFreqSlider.setMinimumSize(QSize(50, 0))
        self.samplingFreqSlider.setMaximumSize(QSize(500, 35))
        self.samplingFreqSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.samplingFreqSlider)

        self.samplingFreqSliderFmax = QSlider(self.widget)
        self.samplingFreqSliderFmax.setObjectName(u"samplingFreqSliderFmax")
        sizePolicy1.setHeightForWidth(self.samplingFreqSliderFmax.sizePolicy().hasHeightForWidth())
        self.samplingFreqSliderFmax.setSizePolicy(sizePolicy1)
        self.samplingFreqSliderFmax.setMinimumSize(QSize(50, 0))
        self.samplingFreqSliderFmax.setMaximumSize(QSize(16777215, 35))
        self.samplingFreqSliderFmax.setOrientation(Qt.Horizontal)

        self.verticalLayout_7.addWidget(self.samplingFreqSliderFmax)


        self.horizontalLayout_9.addLayout(self.verticalLayout_7)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.actualFreqLCD = QLCDNumber(self.widget)
        self.actualFreqLCD.setObjectName(u"actualFreqLCD")
        sizePolicy1.setHeightForWidth(self.actualFreqLCD.sizePolicy().hasHeightForWidth())
        self.actualFreqLCD.setSizePolicy(sizePolicy1)
        self.actualFreqLCD.setMinimumSize(QSize(50, 0))
        self.actualFreqLCD.setMaximumSize(QSize(50, 35))
        self.actualFreqLCD.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.actualFreqLCD)

        self.freqValLabel_2 = QLabel(self.widget)
        self.freqValLabel_2.setObjectName(u"freqValLabel_2")
        sizePolicy1.setHeightForWidth(self.freqValLabel_2.sizePolicy().hasHeightForWidth())
        self.freqValLabel_2.setSizePolicy(sizePolicy1)
        self.freqValLabel_2.setMinimumSize(QSize(0, 0))
        self.freqValLabel_2.setMaximumSize(QSize(50, 35))
        self.freqValLabel_2.setStyleSheet(u"")
        self.freqValLabel_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.freqValLabel_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.normFreqLCD = QLCDNumber(self.widget)
        self.normFreqLCD.setObjectName(u"normFreqLCD")
        sizePolicy1.setHeightForWidth(self.normFreqLCD.sizePolicy().hasHeightForWidth())
        self.normFreqLCD.setSizePolicy(sizePolicy1)
        self.normFreqLCD.setMinimumSize(QSize(50, 0))
        self.normFreqLCD.setMaximumSize(QSize(50, 35))
        self.normFreqLCD.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.normFreqLCD)

        self.fmaxLabel_2 = QLabel(self.widget)
        self.fmaxLabel_2.setObjectName(u"fmaxLabel_2")
        sizePolicy1.setHeightForWidth(self.fmaxLabel_2.sizePolicy().hasHeightForWidth())
        self.fmaxLabel_2.setSizePolicy(sizePolicy1)
        self.fmaxLabel_2.setMinimumSize(QSize(0, 0))
        self.fmaxLabel_2.setMaximumSize(QSize(50, 35))
        self.fmaxLabel_2.setStyleSheet(u"")
        self.fmaxLabel_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.fmaxLabel_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_14.addLayout(self.verticalLayout_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.line_7 = QFrame(self.widget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_7)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 45))
        self.line_3.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setMinimumSize(QSize(50, 0))
        self.label_21.setMaximumSize(QSize(16777215, 100))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(3, 22, 53);\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 27px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setMargin(5)

        self.verticalLayout_4.addWidget(self.label_21)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(50, 0))
        self.label_14.setMaximumSize(QSize(50, 35))
        self.label_14.setStyleSheet(u"QLabel {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(2, 62, 108);\n"
"    font-size: 15px;\n"
"border: 2px solid;\n"
"\n"
"}\n"
"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_14)

        self.signalToNoiseSlider = QSlider(self.widget)
        self.signalToNoiseSlider.setObjectName(u"signalToNoiseSlider")
        sizePolicy4.setHeightForWidth(self.signalToNoiseSlider.sizePolicy().hasHeightForWidth())
        self.signalToNoiseSlider.setSizePolicy(sizePolicy4)
        self.signalToNoiseSlider.setMinimumSize(QSize(50, 0))
        self.signalToNoiseSlider.setMaximumSize(QSize(16777215, 35))
        self.signalToNoiseSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.signalToNoiseSlider)

        self.signalToNoiseLCD = QLCDNumber(self.widget)
        self.signalToNoiseLCD.setObjectName(u"signalToNoiseLCD")
        sizePolicy1.setHeightForWidth(self.signalToNoiseLCD.sizePolicy().hasHeightForWidth())
        self.signalToNoiseLCD.setSizePolicy(sizePolicy1)
        self.signalToNoiseLCD.setMinimumSize(QSize(0, 0))
        self.signalToNoiseLCD.setMaximumSize(QSize(70, 35))
        self.signalToNoiseLCD.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_15.addWidget(self.signalToNoiseLCD)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")

        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

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
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Original Signal", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Reconstructed Signal", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Construction Error", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Frequency Domain", None))
        self.browseSignalButton.setText(QCoreApplication.translate("MainWindow", u"Browse Signal", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Signal Composer", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Amp.", None))
        self.freqValLabel_4.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
        self.freqValLabel_3.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Phase", None))
        self.freqValLabel_5.setText(QCoreApplication.translate("MainWindow", u"deg", None))
        self.addSignalComposerButton.setText(QCoreApplication.translate("MainWindow", u"Add Component", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save to PC", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Components", None))
        self.removeSignalComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL", None))

        self.removeSignalButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Scenarios", None))
        self.testComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.testComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.testComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.testComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.generateTestButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Sampling", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Reconstruction Method", None))
        self.constructMethodComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Whittaker Shannon", None))
        self.constructMethodComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Rectangular Interpolation", None))
        self.constructMethodComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Akima Interpolation", None))
        self.constructMethodComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Fourier Series", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Freq", None))
        self.freqValLabel_2.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.fmaxLabel_2.setText(QCoreApplication.translate("MainWindow", u"fmax", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"SNR", None))
    # retranslateUi

