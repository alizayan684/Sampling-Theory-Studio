# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_Sampler(object):
    def setupUi(self, Sampler):
        if not Sampler.objectName():
            Sampler.setObjectName(u"Sampler")
        Sampler.resize(695, 511)
        self.centralwidget = QWidget(Sampler)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.browseSignalButton = QPushButton(self.centralwidget)
        self.browseSignalButton.setObjectName(u"browseSignalButton")

        self.horizontalLayout_9.addWidget(self.browseSignalButton)

        self.clearAllButton = QPushButton(self.centralwidget)
        self.clearAllButton.setObjectName(u"clearAllButton")

        self.horizontalLayout_9.addWidget(self.clearAllButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.samplingFreqSlider = QSlider(self.centralwidget)
        self.samplingFreqSlider.setObjectName(u"samplingFreqSlider")
        self.samplingFreqSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.samplingFreqSlider)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.normFreqLCD = QLCDNumber(self.centralwidget)
        self.normFreqLCD.setObjectName(u"normFreqLCD")

        self.verticalLayout_5.addWidget(self.normFreqLCD)

        self.actualFreqLCD = QLCDNumber(self.centralwidget)
        self.actualFreqLCD.setObjectName(u"actualFreqLCD")

        self.verticalLayout_5.addWidget(self.actualFreqLCD)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.fmaxLabel = QLabel(self.centralwidget)
        self.fmaxLabel.setObjectName(u"fmaxLabel")

        self.verticalLayout_6.addWidget(self.fmaxLabel)

        self.freqValLabel = QLabel(self.centralwidget)
        self.freqValLabel.setObjectName(u"freqValLabel")

        self.verticalLayout_6.addWidget(self.freqValLabel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.signalToNoiseSlider = QSlider(self.centralwidget)
        self.signalToNoiseSlider.setObjectName(u"signalToNoiseSlider")
        self.signalToNoiseSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.signalToNoiseSlider)

        self.signalToNoiseLCD = QLCDNumber(self.centralwidget)
        self.signalToNoiseLCD.setObjectName(u"signalToNoiseLCD")

        self.horizontalLayout_8.addWidget(self.signalToNoiseLCD)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.amplitudeComposerSlider = QSlider(self.centralwidget)
        self.amplitudeComposerSlider.setObjectName(u"amplitudeComposerSlider")
        self.amplitudeComposerSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.amplitudeComposerSlider)

        self.amplitudeComposerLCD = QLCDNumber(self.centralwidget)
        self.amplitudeComposerLCD.setObjectName(u"amplitudeComposerLCD")

        self.horizontalLayout_7.addWidget(self.amplitudeComposerLCD)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSlider_3 = QSlider(self.centralwidget)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.horizontalSlider_3)

        self.freqComposerLCD = QLCDNumber(self.centralwidget)
        self.freqComposerLCD.setObjectName(u"freqComposerLCD")

        self.horizontalLayout_6.addWidget(self.freqComposerLCD)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.addSignalComposerButton = QPushButton(self.centralwidget)
        self.addSignalComposerButton.setObjectName(u"addSignalComposerButton")

        self.verticalLayout_2.addWidget(self.addSignalComposerButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.signalComboBox = QComboBox(self.centralwidget)
        self.signalComboBox.setObjectName(u"signalComboBox")
        self.signalComboBox.setStyleSheet(u" font-size: 16px; /* Font size */\n"
"    padding: 2px; /* Padding around the text */\n"
"    border: 2px solid ; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\"")

        self.horizontalLayout.addWidget(self.signalComboBox)

        self.removeSignalButton = QPushButton(self.centralwidget)
        self.removeSignalButton.setObjectName(u"removeSignalButton")

        self.horizontalLayout.addWidget(self.removeSignalButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.originalSignalPlot = PlotWidget(self.centralwidget)
        self.originalSignalPlot.setObjectName(u"originalSignalPlot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.originalSignalPlot.sizePolicy().hasHeightForWidth())
        self.originalSignalPlot.setSizePolicy(sizePolicy)
        self.originalSignalPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    padding: 5px; /* Padding around the text */\n"
"    border: 2px solid #4C566A; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_3.addWidget(self.originalSignalPlot)

        self.sampledSignalPlot = PlotWidget(self.centralwidget)
        self.sampledSignalPlot.setObjectName(u"sampledSignalPlot")
        sizePolicy.setHeightForWidth(self.sampledSignalPlot.sizePolicy().hasHeightForWidth())
        self.sampledSignalPlot.setSizePolicy(sizePolicy)
        self.sampledSignalPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    padding: 5px; /* Padding around the text */\n"
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
        sizePolicy.setHeightForWidth(self.differencePlot.sizePolicy().hasHeightForWidth())
        self.differencePlot.setSizePolicy(sizePolicy)
        self.differencePlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    padding: 5px; /* Padding around the text */\n"
"    border: 2px solid #4C566A; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_4.addWidget(self.differencePlot)

        self.frequencyDomainPlot = PlotWidget(self.centralwidget)
        self.frequencyDomainPlot.setObjectName(u"frequencyDomainPlot")
        sizePolicy.setHeightForWidth(self.frequencyDomainPlot.sizePolicy().hasHeightForWidth())
        self.frequencyDomainPlot.setSizePolicy(sizePolicy)
        self.frequencyDomainPlot.setStyleSheet(u"    background-color: #000000; /* Dark background */\n"
"    color: #D8DEE9; /* Light text color */\n"
"    font-size: 16px; /* Font size */\n"
"    padding: 5px; /* Padding around the text */\n"
"    border: 2px solid #4C566A; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    font-family: \"Segoe UI\", \"Helvetica Neue\", \"Arial\", sans-serif; /* Font family */\n"
"")

        self.horizontalLayout_4.addWidget(self.frequencyDomainPlot)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        Sampler.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Sampler)
        self.statusbar.setObjectName(u"statusbar")
        Sampler.setStatusBar(self.statusbar)

        self.retranslateUi(Sampler)

        QMetaObject.connectSlotsByName(Sampler)
    # setupUi

    def retranslateUi(self, Sampler):
        Sampler.setWindowTitle(QCoreApplication.translate("Sampler", u"MainWindow", None))
        self.browseSignalButton.setText(QCoreApplication.translate("Sampler", u"Browse Signal", None))
        self.clearAllButton.setText(QCoreApplication.translate("Sampler", u"Clear All", None))
        self.label_4.setText(QCoreApplication.translate("Sampler", u"Choose Sampling Frequency", None))
        self.fmaxLabel.setText(QCoreApplication.translate("Sampler", u"fmax", None))
        self.freqValLabel.setText(QCoreApplication.translate("Sampler", u"Hz", None))
        self.label_6.setText(QCoreApplication.translate("Sampler", u"Signal To Noise Ratio", None))
        self.label_5.setText(QCoreApplication.translate("Sampler", u"Signal Composer", None))
        self.label_7.setText(QCoreApplication.translate("Sampler", u"Amplitude", None))
        self.label_8.setText(QCoreApplication.translate("Sampler", u"Frequency", None))
        self.addSignalComposerButton.setText(QCoreApplication.translate("Sampler", u"Add Signal", None))
        self.removeSignalButton.setText(QCoreApplication.translate("Sampler", u"Remove Signal", None))
        self.label_12.setText(QCoreApplication.translate("Sampler", u"Original Signal", None))
        self.label_9.setText(QCoreApplication.translate("Sampler", u"Reconstructed Signal", None))
        self.label_11.setText(QCoreApplication.translate("Sampler", u"Construction Error", None))
        self.label_10.setText(QCoreApplication.translate("Sampler", u"Frequency Domain", None))
    # retranslateUi

