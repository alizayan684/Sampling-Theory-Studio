import sys
from main_ui_final import Ui_Sampler
from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np
import pandas as pd
from mixing_senarios import MixingScenarios
from classes import OriginalSignalGraph
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

        self.generateTestButton.clicked.connect(self.run_testing_senarios)
        self.testComboBox.currentIndexChanged.connect(self.updateOriginalSignal)
        self.constructMethodComboBox.currentIndexChanged.connect(self.changeConstruction)
        
    def changeConstruction(self):
        currMethod = self.constructMethodComboBox.currentText()
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = currMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        
        
    def browseSignal(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self, caption="Select a CSV file", dir="/D", filter="(*.csv)"
        )
        if filePath:
            self.df = pd.read_csv(filePath, header=None)
            self.browsedSignal = []
            self.browsedSignal = self.df.to_numpy().flatten()
            self.browsedSignal = self.browsedSignal[:1000]
        
            currSignalTime = np.linspace(0, 1,  1000)
            yLimit = max(np.abs(self.browsedSignal))
            
            # Calculate frequency using the zero-crossing method
            signalFreq = self.calculate_frequency(self.browsedSignal)
            
            self.amplitudes.append(max(np.abs(self.browsedSignal)))
            self.frequencies.append(signalFreq)
            self.removeSignalComboBox.addItem(f"Signal {self.removeSignalComboBox.count() + 1} | Amp: {self.amplitudeComposerSlider.value()}mV | Freq: {self.freqComposerSlider.value()}HZ")
            originalSignalTime = np.linspace(0, len(self.browsedSignal) / self.originalSignalPlot.f_sampling, len(self.browsedSignal))
            samplesTime = np.arange(0, originalSignalTime[-1], step=1/self.originalSignalPlot.f_sampling)
            samplesValues = np.interp(samplesTime, originalSignalTime, self.browsedSignal)

            currSignalValues = self.originalSignalPlot.originalSignal_values
            currSignalValues += self.browsedSignal
            currSampleValues = self.originalSignalPlot.samples_values
            currSampleValues += samplesValues[:20]
            

            # Show the sampled signal
            self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= max(self.originalSignalPlot.signalFreq, signalFreq), yLimit= yLimit, f_sampling= self.originalSignalPlot.f_sampling, samples_values= currSampleValues, sampleNoise= self.originalSignalPlot.sampleNoise, originalSignal_time= self.originalSignalPlot.originalSignal_time)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies, self.originalSignalPlot)

            self.amplitudeComposerSlider.setValue(1)
            self.freqComposerSlider.setValue(1)
            self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
            self.samplingFreqSlider.setMaximum( 7 * self.originalSignalPlot.signalFreq)   # max value
            self.setSamplingSliderValue()

    def calculate_frequency(self, signal):
        """Estimate frequency using the zero-crossing method."""
        zero_crossings = np.where(np.diff(np.sign(signal)))[0]
        num_crossings = len(zero_crossings)
        duration = len(signal) / self.originalSignalPlot.f_sampling  # total duration in seconds
        frequency = num_crossings / (2 * duration)  # divide by 2 for actual frequency
        return frequency

    def ShowSampledSignal(self, originalSignal, signalNoise, signalFreq, yLimit, f_sampling, samples_values, sampleNoise, originalSignal_time=None):
        self.clear()
        self.originalSignal_values = originalSignal
        self.signalNoise = signalNoise
        self.signalFreq = signalFreq
        self.yLimit = yLimit
        self.f_sampling = f_sampling
        self.samples_values = samples_values
        self.sampleNoise = sampleNoise
        self.originalSignal_time = originalSignal_time

        self.plotItem.getViewBox().setLimits(xMin=0, xMax=self.duration, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
        self.plot(self.originalSignal_time, self.originalSignal_values + self.signalNoise, pen='r')
        self.plot(self.samples_time, self.samples_values, pen=None, symbol='o', symbolBrush='b', symbolSize=8, name="Samples")

    def browse_signal(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self, caption="Select a CSV file", dir="/D", filter="(*.csv)"
        )
        if filePath:
            self.load_signal_from_csv(filePath)

            self.originalSignalPlot.ShowSampledSignal(self.browsedSignal)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies, self.originalSignalPlot)    
    
    def setSamplingSliderValue(self):
        self.originalSignalPlot.f_sampling = self.samplingFreqSlider.value()
        self.normFreqLCD.display(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.actualFreqLCD.display(self.samplingFreqSlider.value())

        currSamplesTime = np.arange(0, self.originalSignalPlot.duration, step= 1/self.originalSignalPlot.f_sampling)
        self.originalSignalPlot.samples_time = currSamplesTime
        currSampleValues = 0
        if self.testComboBox.currentIndex() == 0:
            for i in range(len(self.amplitudes)):
                currSampleValues += self.amplitudes[i] * np.sin(2 * np.pi * self.frequencies[i] * currSamplesTime)
            
            self.originalSignalPlot.ShowSampledSignal(originalSignal= self.originalSignalPlot.originalSignal_values, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling= self.originalSignalPlot.f_sampling, samples_values= currSampleValues, sampleNoise= self.originalSignalPlot.sampleNoise , originalSignal_time= self.originalSignalPlot.originalSignal_time)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencyDomainPlot.ShowSignalFreqDomain( self.frequencies.copy(), self.originalSignalPlot)
        else:
            self.run_testing_senarios()
    #############################################################################################################
    def run_testing_senarios(self):
        current = self.testComboBox.currentIndex()
        if current == 0:
            return
        
        mix = MixingScenarios()
        result = None
        if current == 1:
            result = mix.generate_mixed_signal("test1")
            test_name = 'test1'
        elif current == 2:
            result = mix.generate_mixed_signal("test2")
            test_name = 'test2'
        else:
            result = mix.generate_mixed_signal("test3")
            test_name = 'test3'
        mixed_sample_values  =  self.generate_samples_from_signals(mix.tests, test_name, mix)
        
        self.originalSignalPlot.clear()

        self.originalSignalPlot.ShowSampledSignal(result, self.originalSignalPlot.signalNoise,int(mix.tests[test_name]['fmax']), self.originalSignalPlot.yLimit, self.originalSignalPlot.f_sampling, mixed_sample_values, self.originalSignalPlot.sampleNoise, self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies, self.originalSignalPlot)
        
    def setNoise(self):
        self.signalToNoiseLCD.display(self.signalToNoiseSlider.value())
        currSignalValues = self.originalSignalPlot.originalSignal_values
        currSampleValues = self.originalSignalPlot.samples_values

        signalPower = np.mean(currSignalValues ** 2) # The power of a signal is typically defined as the average of the squared values of the signal over time
        noisePower = signalPower / (10 ** (self.signalToNoiseSlider.value() / 10)) # This converts the SNR from decibels to a linear scale
        signalNoise = np.random.normal(0, np.sqrt(noisePower), currSignalValues.shape)  # Generates Gaussian noise
        sampleNoise = np.random.normal(0, np.sqrt(noisePower), currSampleValues.shape)

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, signalNoise= signalNoise, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling = self.originalSignalPlot.f_sampling, samples_values= self.originalSignalPlot.samples_values, sampleNoise= sampleNoise, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies, self.originalSignalPlot)

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

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= max(self.originalSignalPlot.signalFreq, self.frequencies[-1]), yLimit= self.originalSignalPlot.yLimit, f_sampling = self.originalSignalPlot.f_sampling, samples_values= currSampleValues, sampleNoise= self.originalSignalPlot.sampleNoise, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies, self.originalSignalPlot)

        self.amplitudeComposerSlider.setValue(1)
        self.freqComposerSlider.setValue(1)
        self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
        self.samplingFreqSlider.setMaximum( 7 * self.originalSignalPlot.signalFreq)   # max value
        self.setSamplingSliderValue()
    
    def removeSignal(self):
        if(len(self.amplitudes) == 1):
            return
        
        idxRemoved = self.removeSignalComboBox.currentIndex()
        currSignalValues = self.originalSignalPlot.originalSignal_values
        currSignalValues -= self.amplitudes[idxRemoved] * np.sin(2 * np.pi * self.frequencies[idxRemoved] * self.originalSignalPlot.originalSignal_time)
        currSampleValues = self.originalSignalPlot.samples_values
        currSampleValues -= self.amplitudes[idxRemoved] * np.sin(2 * np.pi * self.frequencies[idxRemoved] * self.originalSignalPlot.samples_time)
        
        for i in range(idxRemoved, len(self.amplitudes) - 1):
            self.amplitudes[i] = self.amplitudes[i + 1]
            self.frequencies[i] = self.frequencies[i + 1]
            
            currItemText = self.removeSignalComboBox.itemText(i + 1)
            modifiedText = currItemText[ : 7] + f"{i + 1}" + currItemText[8 : ]
            self.removeSignalComboBox.setItemText(i, modifiedText)

        self.removeSignalComboBox.removeItem(len(self.amplitudes) - 1)
        self.amplitudes.pop()
        self.frequencies.pop()

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= max(self.frequencies), yLimit= self.originalSignalPlot.yLimit, f_sampling = self.originalSignalPlot.f_sampling, samples_values= currSampleValues, sampleNoise= self.originalSignalPlot.sampleNoise, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies, self.originalSignalPlot)
        
        self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
        self.samplingFreqSlider.setMaximum( 7 * self.originalSignalPlot.signalFreq)   # max value
        self.setSamplingSliderValue()

    def generate_samples_from_signals(self, tests,  test_name , mix: MixingScenarios):
        
        test = tests[test_name]
        for signal_name, signal_params in test.items():
            if signal_name != 'fmax':
               mix.generate_sample(signal_name, signal_params ,  self.originalSignalPlot.samples_time )
        return mix.mix_samples(self.originalSignalPlot.samples_time)
    
    def updateOriginalSignal(self):
        if self.testComboBox.currentIndex() == 0:
            self.originalSignalPlot.signalFreq = 5
            self.originalSignalPlot.f_sampling = 4 * self.originalSignalPlot.signalFreq
            self.originalSignalPlot.duration = 1 
            self.originalSignalPlot.originalSignal_time =  np.linspace(0, self.originalSignalPlot.duration,  1000)
            self.originalSignalPlot.originalSignal_values = np.sin(2 * np.pi * self.originalSignalPlot.signalFreq * self.originalSignalPlot.originalSignal_time)
            self.originalSignalPlot.yLimit = max(self.originalSignalPlot.originalSignal_values)
            self.originalSignalPlot.samples_time = np.arange(0, self.originalSignalPlot.duration, step= 1/self.originalSignalPlot.f_sampling) 
            self.originalSignalPlot.samples_values = np.sin(2 * np.pi * self.originalSignalPlot.signalFreq * self.originalSignalPlot.samples_time)
            self.originalSignalPlot.signalNoise = 0
            self.originalSignalPlot.sampleNoise = 0
            self.originalSignalPlot.ShowSampledSignal(self.originalSignalPlot.originalSignal_values, self.originalSignalPlot.signalNoise, self.originalSignalPlot.signalFreq, self.originalSignalPlot.yLimit, self.originalSignalPlot.f_sampling, self.originalSignalPlot.samples_values, self.originalSignalPlot.sampleNoise, self.originalSignalPlot.originalSignal_time) # showing default signal when openning the application)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencyDomainPlot.ShowSignalFreqDomain( self.frequencies.copy(), self.originalSignalPlot)

        
        
        
        
        
            
if __name__ == '__main__':
    app = QtWidgets.QApplication([]);
    window = MainWindow();
    window.show();
    sys.exit(app.exec());