import sys
from main_ui import Ui_Sampler
from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np
import pandas as pd

class MainWindow(Ui_Sampler, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__();
        self.setupUi(self);

        self.amplitudes = [1]
        self.frequencies = [5]
        
        # setting up sampling slider values
        self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
        self.samplingFreqSlider.setMaximum( 7 * self.originalSignalPlot.signalFreq)   # max value
        self.samplingFreqSlider.setValue( self.originalSignalPlot.f_sampling)    # inital value
        self.normFreqLCD.display(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.actualFreqLCD.display(self.samplingFreqSlider.value())
        
        self.samplingFreqSlider.valueChanged.connect(self.setSamplingSliderValue)
        self.browseSignalButton.clicked.connect(self.browseSignal)

        self.amplitudeComposerSlider.setMinimum(1)
        self.amplitudeComposerSlider.setMaximum(20)
        self.amplitudeComposerSlider.setValue(self.amplitudeComposerSlider.minimum())
        self.amplitudeComposerLCD.display(self.amplitudeComposerSlider.value())
        self.amplitudeComposerSlider.valueChanged.connect(self.setAmplitudeSliderValue)

        self.freqComposerSlider.setMinimum(1)
        self.freqComposerSlider.setMaximum(10)
        self.freqComposerSlider.setValue(self.freqComposerSlider.minimum())
        self.freqComposerLCD.display(self.freqComposerSlider.value())
        self.freqComposerSlider.valueChanged.connect(self.setFrequencySliderValue)

        self.addSignalComposerButton.clicked.connect(self.addSignal)
        self.removeSignalButton.clicked.connect(self.removeSignal)
        
    def browseSignal(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self, caption="Select a CSV file", dir="/D", filter="(*.csv)"
        )
        if filePath:
            self.df = pd.read_csv(filePath, header=None)
            self.browsedSignal = []
            self.browsedSignal = self.df.to_numpy().flatten()
            self.originalSignalPlot.ShowSampledSignal(self.browsedSignal)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)    
    
    def setSamplingSliderValue(self):
        self.originalSignalPlot.f_sampling = self.samplingFreqSlider.value()
        self.normFreqLCD.display(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.actualFreqLCD.display(self.samplingFreqSlider.value())

        currSamplesTime = np.arange(0, self.originalSignalPlot.duration, step= 1/self.originalSignalPlot.f_sampling)
        currSampleValues = 0
        for i in range(len(self.amplitudes)):
            currSampleValues += self.amplitudes[i] * np.sin(2 * np.pi * self.frequencies[i] * currSamplesTime)

        self.originalSignalPlot.ShowSampledSignal(originalSignal= self.originalSignalPlot.originalSignal_values, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling= self.originalSignalPlot.f_sampling, samples_values= currSampleValues, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)

    def setAmplitudeSliderValue(self):
        self.amplitudeComposerLCD.display(self.amplitudeComposerSlider.value())
    
    def setFrequencySliderValue(self):
        self.freqComposerLCD.display(self.freqComposerSlider.value())
    
    def addSignal(self):
        self.amplitudes.append(self.amplitudeComposerSlider.value())
        self.frequencies.append(self.freqComposerSlider.value())
        self.signalComposerCompoBox.addItem(f"Signal {self.signalComposerCompoBox.count() + 1} | Amp: {self.amplitudeComposerSlider.value()} | Freq: {self.freqComposerSlider.value()}HZ")

        currValues = self.originalSignalPlot.originalSignal_values
        currValues += self.amplitudes[-1] * np.sin(2 * np.pi * self.frequencies[-1] * self.originalSignalPlot.originalSignal_time)
        currSampleValues = self.originalSignalPlot.samples_values
        currSampleValues += self.amplitudes[-1] * np.sin(2 * np.pi * self.frequencies[-1] * self.originalSignalPlot.samples_time)

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currValues, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling = self.originalSignalPlot.f_sampling, samples_values= currSampleValues, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)

        self.amplitudeComposerSlider.setValue(1)
        self.freqComposerSlider.setValue(1)
    
    def removeSignal(self):
        self.amplitudeComposerSlider.setValue(1)
        self.freqComposerSlider.setValue(1)
            
if __name__ == '__main__':
    app = QtWidgets.QApplication([]);
    window = MainWindow();
    window.show();
    sys.exit(app.exec());