import re
import sys
from main_ui_finished import Ui_Sampler
from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np
import pandas as pd
from mixing_senarios import MixingScenarios
from classes import OriginalSignalGraph
from reportlab.pdfgen import canvas        
class MainWindow(Ui_Sampler, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__();
        self.setupUi(self);

        self.amplitudes = [1]
        self.frequencies = [5]
        self.phases = [np.radians(0)]
        self.browsedSignalsMap = dict()
        
        # setting up sampling slider values
        self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
        self.samplingFreqSlider.setMaximum( 20 * self.originalSignalPlot.signalFreq)   # max value
        self.samplingFreqSlider.setValue(self.originalSignalPlot.f_sampling)    # inital value
        self.samplingFreqSlider_2.setMinimum(0)
        self.samplingFreqSlider_2.setMaximum(20)   
        self.samplingFreqSlider_2.setValue(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))    
        self.normFreqLCD.display(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.actualFreqLCD.display(self.samplingFreqSlider.value())
        
        self.samplingFreqSlider.valueChanged.connect(self.setSamplingSliderValue)
        self.samplingFreqSlider_2.valueChanged.connect(self.setFmaxSamplingSliderValue)
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

        self.phaseComposerSlider.setMinimum(0)
        self.phaseComposerSlider.setMaximum(360)
        self.phaseComposerSlider.setValue(0)
        self.phaseComposerLCD.display(self.phaseComposerSlider.value())
        self.phaseComposerSlider.valueChanged.connect(self.setPhaseSliderValue)


        self.addSignalComposerButton.clicked.connect(self.addSignal)
        self.removeSignalButton.clicked.connect(self.removeSignal)
        self.saveButton.clicked.connect(self.saveTest)
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
            inputSignal = []
            inputSignal = self.df.to_numpy().flatten()

            if len(inputSignal) < 1000:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                msg.setWindowTitle("Browsing Error")
                msg.setText("Browsed Signal Should Have At Least 1000 Points")
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()  # Show the message box

            browsedSignal = inputSignal[ : 1000]

            # Extend the array to equal the length of the original signal duration by repeating the start of the array
            self.browsedSignal = np.concatenate([browsedSignal] * self.originalSignalPlot.duration)
            self.browsedSignal = np.interp(np.linspace(0, self.originalSignalPlot.duration, 100 * self.originalSignalPlot.duration), 
                                           np.linspace(0, self.originalSignalPlot.duration, 1000 * self.originalSignalPlot.duration),
                                           self.browsedSignal)
        
            yLimit = max(np.abs(browsedSignal))
            
            signalFreq = self.calculate_frequency(browsedSignal, yLimit - 0.3)
            
            self.amplitudes.append(yLimit)
            self.frequencies.append(signalFreq)
            self.phases.append(np.radians(0))
            title = f"Signal {self.removeSignalComboBox.count() + 1} | Amp: {round(yLimit, 1)}mV | Freq: {signalFreq}HZ | Phase: 0 Deg"
            self.removeSignalComboBox.addItem(title)
            self.browsedSignalsMap[title] = self.browsedSignal

            currSignalValues = self.originalSignalPlot.originalSignal_values
            currSignalValues += self.browsedSignal

            # Show the sampled signal
            self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= max(self.originalSignalPlot.signalFreq, signalFreq), f_sampling= self.originalSignalPlot.f_sampling)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies.copy(), self.originalSignalPlot)

            self.amplitudeComposerSlider.setValue(1)
            self.freqComposerSlider.setValue(1)
            self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
            self.samplingFreqSlider.setMaximum( 20 * self.originalSignalPlot.signalFreq)   # max value
            self.samplingFreqSlider_2.setMinimum(0)  # min value
            self.samplingFreqSlider_2.setMaximum(20)   # max value
            self.setSamplingSliderValue()

    def calculate_frequency(self, signal, threshold):
        peaks = []
        for i in range(len(signal)):
            if i > 0 and i < len(signal) - 1:
                if signal[i] > signal[i - 1] and signal[i] > signal[i + 1] and signal[i] > threshold:
                    peaks.append(i)

        currSignalTime = np.linspace(0, 1, 1000)
        cycleTimes = []
        for i in range(len(peaks) - 1, 0, -1):
            cycleTimes.append(currSignalTime[peaks[i]] - currSignalTime[peaks[i - 1]])
        
        periodicTime = np.average(cycleTimes)

        return round(1 / periodicTime)

    def setSamplingSliderValue(self):
        self.originalSignalPlot.f_sampling = self.samplingFreqSlider.value()
        self.samplingFreqSlider_2.setValue(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.normFreqLCD.display(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.actualFreqLCD.display(self.samplingFreqSlider.value())

        currSamplesTime = np.arange(0, self.originalSignalPlot.duration, step= 1/self.originalSignalPlot.f_sampling)
        self.originalSignalPlot.samples_time = currSamplesTime

        if self.testComboBox.currentIndex() == 0:            
            self.originalSignalPlot.ShowSampledSignal(originalSignal= self.originalSignalPlot.originalSignal_values, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= self.originalSignalPlot.signalFreq, f_sampling= self.originalSignalPlot.f_sampling)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencyDomainPlot.ShowSignalFreqDomain( self.frequencies.copy(), self.originalSignalPlot)
        else:
            self.run_testing_senarios()

    def setFmaxSamplingSliderValue(self):
        self.originalSignalPlot.f_sampling = self.samplingFreqSlider_2.value() * self.originalSignalPlot.signalFreq
        self.samplingFreqSlider.setValue(self.samplingFreqSlider_2.value() * self.originalSignalPlot.signalFreq)
        self.normFreqLCD.display(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.actualFreqLCD.display(self.samplingFreqSlider.value())

        currSamplesTime = np.arange(0, self.originalSignalPlot.duration, step= 1/self.originalSignalPlot.f_sampling)
        self.originalSignalPlot.samples_time = currSamplesTime

        if self.testComboBox.currentIndex() == 0:            
            self.originalSignalPlot.ShowSampledSignal(originalSignal= self.originalSignalPlot.originalSignal_values, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= self.originalSignalPlot.signalFreq, f_sampling= self.originalSignalPlot.f_sampling)
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
        frequencies = []
        for signal_name , values in mix.tests[test_name].items():
            if signal_name != 'fmax':
                frequencies.append(values[0])
        self.frequencies = frequencies
        
        self.originalSignalPlot.clear()

        self.originalSignalPlot.ShowSampledSignal(result, self.originalSignalPlot.signalNoise,int(mix.tests[test_name]['fmax']), self.originalSignalPlot.f_sampling)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies.copy(), self.originalSignalPlot)
        
    def setNoise(self):
        self.signalToNoiseLCD.display(self.signalToNoiseSlider.value())
        currSignalValues = self.originalSignalPlot.originalSignal_values

        signalPower = np.mean(currSignalValues ** 2) # The power of a signal is typically defined as the average of the squared values of the signal over time
        noisePower = signalPower / (10 ** (self.signalToNoiseSlider.value() / 10)) # This converts the SNR from decibels to a linear scale
        signalNoise = np.random.normal(0, np.sqrt(noisePower), currSignalValues.shape)  # Generates Gaussian noise

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, signalNoise= signalNoise, signalFreq= self.originalSignalPlot.signalFreq, f_sampling = self.originalSignalPlot.f_sampling)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies.copy(), self.originalSignalPlot)

    def setAmplitudeSliderValue(self):
        self.amplitudeComposerLCD.display(self.amplitudeComposerSlider.value())
    
    def setPhaseSliderValue(self):
        self.phaseComposerLCD.display(self.phaseComposerSlider.value())
    
    def setFrequencySliderValue(self):
        self.freqComposerLCD.display(self.freqComposerSlider.value())
    
    def addSignal(self):
        self.amplitudes.append(self.amplitudeComposerSlider.value())
        self.frequencies.append(self.freqComposerSlider.value())
        self.phases.append(np.radians(self.phaseComposerSlider.value()))
        self.removeSignalComboBox.addItem(f"Signal {self.removeSignalComboBox.count() + 1} | Amp: {self.amplitudeComposerSlider.value()}mV | Freq: {self.freqComposerSlider.value()}HZ | Phase: {self.phaseComposerSlider.value()} Deg")

        currSignalValues = self.originalSignalPlot.originalSignal_values
        currSignalValues += self.amplitudes[-1] * np.sin(2 * np.pi * self.frequencies[-1] * self.originalSignalPlot.originalSignal_time + self.phases[-1])

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= max(self.originalSignalPlot.signalFreq, self.frequencies[-1]), f_sampling = self.originalSignalPlot.f_sampling)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies.copy(), self.originalSignalPlot)

        self.amplitudeComposerSlider.setValue(1)
        self.freqComposerSlider.setValue(1)
        self.phaseComposerSlider.setValue(0)
        self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
        self.samplingFreqSlider.setMaximum( 20 * self.originalSignalPlot.signalFreq)   # max value
        self.samplingFreqSlider_2.setMinimum(0)  # min value
        self.samplingFreqSlider_2.setMaximum(20)   # max value
        self.setSamplingSliderValue()
    
    def removeSignal(self):
        if(len(self.amplitudes) == 1):
            return
        
        idxRemoved = self.removeSignalComboBox.currentIndex()
        textRemoved = self.removeSignalComboBox.currentText()
        currSignalValues = self.originalSignalPlot.originalSignal_values
        if textRemoved in self.browsedSignalsMap:
            currSignalValues -= self.browsedSignalsMap[textRemoved]
            self.browsedSignalsMap.pop(textRemoved)
        else:
            currSignalValues -= self.amplitudes[idxRemoved] * np.sin(2 * np.pi * self.frequencies[idxRemoved] * self.originalSignalPlot.originalSignal_time + self.phases[idxRemoved])
        
        for i in range(idxRemoved, len(self.amplitudes) - 1):
            self.amplitudes[i] = self.amplitudes[i + 1]
            self.frequencies[i] = self.frequencies[i + 1]
            self.phases[i] = self.phases[i + 1]
            
            currItemText = self.removeSignalComboBox.itemText(i + 1)
            modifiedText = currItemText[ : 7] + f"{i + 1}" + currItemText[8 : ]
            self.removeSignalComboBox.setItemText(i, modifiedText)
            if currItemText in self.browsedSignalsMap:
                self.browsedSignalsMap[modifiedText] = self.browsedSignalsMap[currItemText]
                self.browsedSignalsMap.pop(currItemText)

        self.removeSignalComboBox.removeItem(len(self.amplitudes) - 1)
        self.amplitudes.pop()
        self.frequencies.pop()
        self.phases.pop()

        self.originalSignalPlot.ShowSampledSignal(originalSignal= currSignalValues, signalNoise= self.originalSignalPlot.signalNoise, signalFreq= max(self.frequencies), f_sampling = self.originalSignalPlot.f_sampling)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.frequencies.copy(), self.originalSignalPlot)
        
        self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
        self.samplingFreqSlider.setMaximum( 20 * self.originalSignalPlot.signalFreq)   # max value
        self.samplingFreqSlider_2.setMinimum(0)  # min value
        self.samplingFreqSlider_2.setMaximum(20)   # max value
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
            self.originalSignalPlot.ShowSampledSignal(self.originalSignalPlot.originalSignal_values, self.originalSignalPlot.signalNoise, self.originalSignalPlot.signalFreq, self.originalSignalPlot.f_sampling)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencies = [self.originalSignalPlot.signalFreq]
            self.frequencyDomainPlot.ShowSignalFreqDomain( self.frequencies.copy(), self.originalSignalPlot)

    def saveTest(self):
        # creating a PDF file
        c = canvas.Canvas("test.pdf")
        # Setting the title of the PDF file
        c.setTitle("Test Report")
        # adding signal information to the PDF file
        c.drawString(100, 800, "Signal Information")
        c.drawString(100, 780, "Original Signal Frequency: " + str(self.originalSignalPlot.signalFreq) + "Hz")
        c.drawString(100, 760, "Original Signal Sampling Frequency: " + str(self.originalSignalPlot.f_sampling) + "Hz")
        c.drawString(100, 740, "Original Signal Amplitude: " + str(self.originalSignalPlot.yLimit) + "mV")
        c.drawString(100, 720, "Original Signal Duration: " + str(self.originalSignalPlot.duration) + "s")
        c.drawString(100, 700, "Original Signal Noise: " + str(self.signalToNoiseSlider.value()) + "dB")
        c.drawString(100, 680, "Original Signal Samples: " + str(len(self.originalSignalPlot.samples_values)))
        c.drawString(100, 660, "Original Signal Samples Time: " + str(self.originalSignalPlot.samples_time))
        c.drawString(100, 640, "Original Signal Samples Values: " + str(self.originalSignalPlot.samples_values))
        # closing the PDF file
        c.save()
        

            
if __name__ == '__main__':
    app = QtWidgets.QApplication([]);
    window = MainWindow();
    window.show();
    sys.exit(app.exec());