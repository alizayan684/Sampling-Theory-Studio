# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_M.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_Sampler(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(576, 782)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: #333333;\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 14px;\n"
"	background-color: rgb(72, 72, 72);\n"
"}\n"
"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);\n"
"    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"\n"
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

        self.verticalLayout_7.addWidget(self.normFreqLCD)

        self.actualFreqLCD = QLCDNumber(self.widget)
        self.actualFreqLCD.setObjectName(u"actualFreqLCD")
        sizePolicy.setHeightForWidth(self.actualFreqLCD.sizePolicy().hasHeightForWidth())
        self.actualFreqLCD.setSizePolicy(sizePolicy)
        self.actualFreqLCD.setMinimumSize(QSize(0, 0))
        self.actualFreqLCD.setMaximumSize(QSize(100, 200))

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

        self.horizontalLayout_15.addWidget(self.signalToNoiseLCD)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(50, 0))
        self.label_15.setMaximumSize(QSize(16777215, 100))
        self.label_15.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 48, 48);\n"
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

        self.horizontalLayout_16.addWidget(self.amplitudeComposerLCD)


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

        self.horizontalLayout_17.addWidget(self.freqComposerLCD)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.addSignalComposerButton = QPushButton(self.widget)
        self.addSignalComposerButton.setObjectName(u"addSignalComposerButton")
        sizePolicy.setHeightForWidth(self.addSignalComposerButton.sizePolicy().hasHeightForWidth())
        self.addSignalComposerButton.setSizePolicy(sizePolicy)
        self.addSignalComposerButton.setMinimumSize(QSize(0, 0))
        self.addSignalComposerButton.setMaximumSize(QSize(250, 250))

        self.verticalLayout_4.addWidget(self.addSignalComposerButton)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.signalComposerCompoBox = QComboBox(self.widget)
        self.signalComposerCompoBox.addItem("")
        self.signalComposerCompoBox.setObjectName(u"signalComposerCompoBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.signalComposerCompoBox.sizePolicy().hasHeightForWidth())
        self.signalComposerCompoBox.setSizePolicy(sizePolicy2)
        self.signalComposerCompoBox.setMinimumSize(QSize(100, 30))
        self.signalComposerCompoBox.setMaximumSize(QSize(120, 200))
        self.signalComposerCompoBox.setStyleSheet(u" font-size: 16px; /* Font size */\n"
"    padding: 2px; /* Padding around the text */\n"
"    border: 2px solid ; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\"")

        self.horizontalLayout_18.addWidget(self.signalComposerCompoBox)

        self.removeSignalButton = QPushButton(self.widget)
        self.removeSignalButton.setObjectName(u"removeSignalButton")
        sizePolicy.setHeightForWidth(self.removeSignalButton.sizePolicy().hasHeightForWidth())
        self.removeSignalButton.setSizePolicy(sizePolicy)
        self.removeSignalButton.setMinimumSize(QSize(0, 0))
        self.removeSignalButton.setMaximumSize(QSize(200, 200))

        self.horizontalLayout_18.addWidget(self.removeSignalButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.originalSignalPlot = PlotWidget(self.centralwidget)
        self.originalSignalPlot.setObjectName(u"originalSignalPlot")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.originalSignalPlot.sizePolicy().hasHeightForWidth())
        self.originalSignalPlot.setSizePolicy(sizePolicy3)
        self.originalSignalPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    border: 2px solid #4C566A; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_3.addWidget(self.originalSignalPlot)

        self.sampledSignalPlot = PlotWidget(self.centralwidget)
        self.sampledSignalPlot.setObjectName(u"sampledSignalPlot")
        sizePolicy3.setHeightForWidth(self.sampledSignalPlot.sizePolicy().hasHeightForWidth())
        self.sampledSignalPlot.setSizePolicy(sizePolicy3)
        self.sampledSignalPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    border: 2px solid #4C566A; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_3.addWidget(self.sampledSignalPlot)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.differencePlot = PlotWidget(self.centralwidget)
        self.differencePlot.setObjectName(u"differencePlot")
        sizePolicy3.setHeightForWidth(self.differencePlot.sizePolicy().hasHeightForWidth())
        self.differencePlot.setSizePolicy(sizePolicy3)
        self.differencePlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    border: 2px solid #4C566A; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_4.addWidget(self.differencePlot)

        self.frequencyDomainPlot = PlotWidget(self.centralwidget)
        self.frequencyDomainPlot.setObjectName(u"frequencyDomainPlot")
        sizePolicy3.setHeightForWidth(self.frequencyDomainPlot.sizePolicy().hasHeightForWidth())
        self.frequencyDomainPlot.setSizePolicy(sizePolicy3)
        self.frequencyDomainPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    border: 2px solid #4C566A; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_4.addWidget(self.frequencyDomainPlot)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.browseSignalButton.setText(QCoreApplication.translate("MainWindow", u"Browse Signal", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sampling Frequency", None))
        self.fmaxLabel_2.setText(QCoreApplication.translate("MainWindow", u"fmax", None))
        self.freqValLabel_2.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Signal To Noise Ratio", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Signal Composer", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.addSignalComposerButton.setText(QCoreApplication.translate("MainWindow", u"Add Signal", None))
        self.signalComposerCompoBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL", None))

        self.removeSignalButton.setText(QCoreApplication.translate("MainWindow", u"Remove Signal", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Original Signal", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Reconstructed Signal", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Construction Error", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Frequency Domain", None))
    # retranslateUi

