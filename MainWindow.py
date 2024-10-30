import sys
from main_ui import Ui_Sampler
from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np
import pandas as pd
from mixing_senarios import MixingScenarios



# here, we will define the methods and vars related for all the graphs (i.e: browse, clear, ....), not defined specially for one of the four graphs 
    
    
        

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

        self.signalToNoiseSlider.setMinimum(1)
        self.signalToNoiseSlider.setMaximum(50)
        self.signalToNoiseSlider.setValue(self.signalToNoiseSlider.maximum())
        self.signalToNoiseLCD.display(self.signalToNoiseSlider.value())
        self.signalToNoiseSlider.valueChanged.connect(self.setNoise)

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

        self.originalSignalPlot.ShowSampledSignal(originalSignal= self.originalSignalPlot.originalSignal_values, noise= self.originalSignalPlot.noise, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling= self.originalSignalPlot.f_sampling, samples_values= currSampleValues, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)
    
    #############################################################################################################
    def run_testing_senarios(self):
        current = self.testComboBox.currentIndex()
        if current == 0:
            return
        
        mix = MixingScenarios()
        result = None
        if current == 1:
            result = mix.generate_mixed_signal("test1")
        elif current == 2:
            result = mix.generate_mixed_signal("test2")
        else:
            result = mix.generate_mixed_signal("test3")
        self.originalSignalPlot.ShowSampledSignal(self.browsedSignal)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)
            
        
    def setNoise(self):
        self.signalToNoiseLCD.display(self.signalToNoiseSlider.value())
        currSignalValues = self.originalSignalPlot.originalSignal_values

        signalPower = np.mean(currSignalValues ** 2) # The power of a signal is typically defined as the average of the squared values of the signal over time
        noisePower = signalPower / (10 ** (self.signalToNoiseSlider.value() / 10)) # This converts the SNR from decibels to a linear scale
        noise = np.random.normal(0, np.sqrt(noisePower), currSignalValues.shape)  # Generates Gaussian noise
        

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, noise= noise, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling = self.originalSignalPlot.f_sampling, samples_values= self.originalSignalPlot.samples_values, originalSignal_time= self.originalSignalPlot.originalSignal_time)
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
        self.removeSignalComboBox.addItem(f"Signal {self.removeSignalComboBox.count() + 1} | Amp: {self.amplitudeComposerSlider.value()}mV | Freq: {self.freqComposerSlider.value()}HZ")

        currSignalValues = self.originalSignalPlot.originalSignal_values
        currSignalValues += self.amplitudes[-1] * np.sin(2 * np.pi * self.frequencies[-1] * self.originalSignalPlot.originalSignal_time)
        currSampleValues = self.originalSignalPlot.samples_values
        currSampleValues += self.amplitudes[-1] * np.sin(2 * np.pi * self.frequencies[-1] * self.originalSignalPlot.samples_time)

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, noise= self.originalSignalPlot.noise, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling = self.originalSignalPlot.f_sampling, samples_values= currSampleValues, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)

        self.amplitudeComposerSlider.setValue(1)
        self.freqComposerSlider.setValue(1)
    
    def removeSignal(self):
        if(len(self.amplitudes) == 1):
            return
        
        idxRemoved = self.removeSignalComboBox.currentIndex()
        currSignalValues = self.originalSignalPlot.originalSignal_values
        currSignalValues -= self.amplitudes[idxRemoved] * np.sin(2 * np.pi * self.frequencies[idxRemoved] * self.originalSignalPlot.originalSignal_time)
        currSampleValues = self.originalSignalPlot.samples_values
        currSampleValues -= self.amplitudes[idxRemoved] * np.sin(2 * np.pi * self.frequencies[idxRemoved] * self.originalSignalPlot.samples_time)

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, noise= self.originalSignalPlot.noise, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling = self.originalSignalPlot.f_sampling, samples_values= currSampleValues, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)

        for i in range(idxRemoved, len(self.amplitudes) - 1):
            self.amplitudes[i] = self.amplitudes[i + 1]
            self.frequencies[i] = self.frequencies[i + 1]
            
            currItemText = self.removeSignalComboBox.itemText(i + 1)
            modifiedText = currItemText[ : 7] + f"{i + 1}" + currItemText[8 : ]
            self.removeSignalComboBox.setItemText(i, modifiedText)

        self.removeSignalComboBox.removeItem(len(self.amplitudes) - 1)
        self.amplitudes.pop()
        self.frequencies.pop()
            
if __name__ == '__main__':
    app = QtWidgets.QApplication([]);
    window = MainWindow();
    window.show();
    sys.exit(app.exec());
