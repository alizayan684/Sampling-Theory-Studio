from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np
from scipy.interpolate import interp1d

class OriginalSignalGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent )
        self.signalFreq = 5 # initializing frequency of the original signal (a default signal with freq = 5 Hz before browsing any signal) (cycles per second)
        self.duration = 1  # duration of the signal
        self.f_sampling = 4 * self.signalFreq # sampling frequency to sample the signal (samples per second)
        self.continuousSignal_time =  np.linspace(0, self.duration,  1000) # initializing x values of the original signal(time domain)
        self.continuousSignal_values = np.sin(2 * np.pi * self.signalFreq * self.continuousSignal_time)  # initialization of the graph's original signal values
        self.plot(self.continuousSignal_time, self.continuousSignal_values, pen = 'r') # plotting the original signal
        self.samples_time = np.linspace(0, self.duration, int(self.duration * self.f_sampling)) # x values (time values) of the samples that will be taken from the orignial signal by sampling freq = f_sampling
        self.samples_values = np.sin(2 * np.pi * self.signalFreq * self.samples_time) # values of the samples taken
        self.plot(self.samples_time, self.samples_values, pen=None, symbol='o', symbolBrush='b', symbolSize=8, name="Samples") # plotting the samples on the original signal
        
        
        
        
    def ShowSampledSignal(self, signal, signalFreq):
        # self.continuousSignal_y = signal
        # self.signalFreq = signalFreq
        # self.continuousSignal_x = np.arange(0, len(self.signal_y)/self.signalFreq, 1/self.signalFreq)  # adjusting the time axis for the signal to be drawn with the correct frequency.
        # self.f_sampling = 2 * self.signalFreq  # adjusting it to be double the signal frequency by default
        # self.plot(self.signal_x, self.signal_y, pen = 'r')
        pass





class ReconstructedSignalGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.originalSignal_time = OriginalSignalGraph().continuousSignal_time  # getting the time axis values corresponding to the original signal
        self.signalFreq = OriginalSignalGraph().signalFreq  # initializing original signal freq to be equal to the initialized one in the original signal graph
        self.f_sampling = OriginalSignalGraph().f_sampling  # initializing sampling freq to be equal to the initialized one in the original signal graph
        self.duration = OriginalSignalGraph().duration      # initializing signal duration to be equal to the initialized one in the original signal graph
        self.reconstructedSignal_time = OriginalSignalGraph().samples_time  # initializing sampling time axis values to be equal to the initialized one in the original signal graph (needed in interpolation)
        self.reconstructedSignal_values = OriginalSignalGraph().samples_values   # initializing sampled signal values to be equal to the initialized one in the original signal graph (needed in interpolation)
        self.reconstructedSignal_interpolation_method = interp1d(self.reconstructedSignal_time, self.reconstructedSignal_values, kind = 'cubic', fill_value= 'extrapolate') # interpolating to get all the y values corresponding to any x (time) value in this range (or out due 'extrapolate), so I can plot the constructed signal values infront of the original signal time values
        self.reconstructedSignal_values_correspondOriginalTime = self.reconstructedSignal_interpolation_method(self.originalSignal_time)  # reconstruction signal values that correspond the original signal time values
        self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen = 'g') # plot the reconstructed signal from sampling (the signal itself not the samples), using the signal values corresponding to the original time values
        
        
        
        
class DifferenceGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.originalSignal_time = OriginalSignalGraph().continuousSignal_time  # time values of the original signal
        self.originalSignal_values = OriginalSignalGraph().continuousSignal_values  # original signal values corresponding to the orignal time values
        self.reconstructedSignal_values_correspondOriginalTime = ReconstructedSignalGraph().reconstructedSignal_values_correspondOriginalTime  # reconstructed signal values corresponding to the orignal time values 
        self.differenceSignal_values = self.originalSignal_values - self.reconstructedSignal_values_correspondOriginalTime  # difference between orignal and reconstructed signal values corresponding to the original time values
        print(self.differenceSignal_values) # for checking the difference between both signals in the terminal
        self.setYRange(-1, 1)
        self.plot(self.originalSignal_time, self.differenceSignal_values, pen = 'y') # plotting the difference between original and reconstructed signals at the same time values (time values of the original signal).