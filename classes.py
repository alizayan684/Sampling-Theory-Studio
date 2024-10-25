from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np

class OriginalSignalGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent )
        self.signal_y = []  # initialization of the graph's signal values
        self.signal_x = []  # x values (time domain)
        self.signalFreq = 0 # frequency of the original signal
        self.f_sampling = 0 # sampling frequency to sample the signal
        
        
    def ShowSampledSignal(self, signal, signalFreq):
        self.signal_y = signal
        self.signalFreq = signalFreq
        self.signal_x = np.arange(0, len(self.signal_y)/self.signalFreq, 1/self.signalFreq)  # adjusting the time axis for the signal to be drawn with the correct frequency.
        self.f_sampling = 2 * self.signalFreq  # adjusting it to be double the signal frequency by default
        self.plot(self.signal_x, self.signal_y, pen = 'r')
        
        
        