from PySide6 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
from scipy.interpolate import Akima1DInterpolator

class OriginalSignalGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent )
        self.signalFreq = 5 # initializing frequency of the original signal (a default signal with freq = 5 Hz before browsing any signal) (cycles per second)
        self.f_sampling = int(2.2 * self.signalFreq) # initializing sampling frequency to sample the signal (samples per second)
        self.duration = 30  # duration of the signal
        self.phaseShift = np.radians(0)
        self.originalSignal_time =  np.linspace(0, self.duration, 100 * self.duration) # initializing x values of the original signal(time domain)
        self.originalSignal_values = np.sin(2 * np.pi * self.signalFreq * self.originalSignal_time + self.phaseShift)  # initialization of the graph's original signal values
        self.yLimit = max(self.originalSignal_values)
        self.signalNoise = 0
        self.samples_time = np.arange(0, self.duration, step= 1/self.f_sampling) 
        self.samples_values = np.interp(self.samples_time, self.originalSignal_time, self.originalSignal_values + self.signalNoise)
        self.ShowSampledSignal(self.originalSignal_values, self.signalNoise, self.signalFreq, self.f_sampling) # showing default signal when openning the application
        
        self.plotItem.getViewBox().sigRangeChanged.connect(self.resetRange)
        
    # showing sampled signal in the graph    
    def ShowSampledSignal(self, originalSignal, signalNoise, signalFreq, f_sampling): 
        # I pass the "originalSignal_time" as it will be needed for the default signal that occurs when starting the application and also to keep  the same signal time when changing the slider
        self.clear()
        self.originalSignal_values = originalSignal
        self.signalNoise = signalNoise
        self.signalFreq = signalFreq
        self.f_sampling = f_sampling
        self.samples_time = np.arange(0, self.duration, step= 1/self.f_sampling)
        self.samples_values = np.interp(self.samples_time, self.originalSignal_time, self.originalSignal_values + self.signalNoise)
        self.yLimit = max(self.originalSignal_values)
        self.setXRange(0, 5)
        self.plotItem.getViewBox().setLimits(xMin=0, xMax=self.duration, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
        self.plot(self.originalSignal_time, self.originalSignal_values + self.signalNoise, pen = 'r')
        self.plot(self.samples_time, self.samples_values, pen=None, symbol='o', symbolBrush='b', symbolSize=8, name="Samples")
    
    def resetRange(self):
        currXRange = self.plotItem.getViewBox().viewRange()[0]
        if ((currXRange[1] - currXRange[0]) > 7):
            self.setXRange(0, 5)
            self.setYRange(-self.yLimit - 0.3, self.yLimit + 0.3)

class ReconstructedSignalGraph(pg.PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize necessary values for Whittaker-Shannon reconstruction
        self.originalSignal_time = OriginalSignalGraph().originalSignal_time
        self.signalFreq = OriginalSignalGraph().signalFreq
        self.yLimit = OriginalSignalGraph().yLimit
        self.f_sampling = OriginalSignalGraph().f_sampling
        self.duration = OriginalSignalGraph().duration
        self.reconstructedSignal_time = OriginalSignalGraph().samples_time
        self.reconstructedSignal_values = OriginalSignalGraph().samples_values
        self.reconstructionMethod = 'whittaker shannon' # initializing the reconstruction method to be whittaker shannon method.
        # self.reconstructionMethod = ['whittaker shannon','Fourier Series' , 'Akima Interpolation','Rectangular Interpolation']
        self.ReconstructSampledSignal(OriginalSignalGraph(), self.reconstructionMethod)

        self.plotItem.getViewBox().sigRangeChanged.connect(self.resetRange)
    
    def resetRange(self):
        currXRange = self.plotItem.getViewBox().viewRange()[0]
        if ((currXRange[1] - currXRange[0]) > 7):
            self.setXRange(0, 5)
            self.setYRange(-self.yLimit - 0.3, self.yLimit + 0.3)

    # reconstruction signal method  
    def ReconstructSampledSignal(self, originalGraph_instance, reconstructionMethod = 'whittaker shannon' ):  
        """
        Params:
        originalGraph_instance (_instance_): instance of the 'OriginalSignalGraph' that is already made(needed to get some data for reconstructing the original signal)
        recosntructionMethod (_method_): method used for the signal recosntruction
        
        """
        self.clear()
        self.reconstructionMethod = reconstructionMethod
        if self.reconstructionMethod == 'whittaker shannon':
            # taking data needed for the whittaker shannon construction from the OriginalGraph instance.
            self.originalSignal_time = originalGraph_instance.originalSignal_time
            self.originalSignal_duration = originalGraph_instance.duration
            self.reconstructedSignal_time = originalGraph_instance.samples_time
            self.reconstructedSignal_values = originalGraph_instance.samples_values
            
            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the whittaker shannon formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.whittaker_shannon(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            self.yLimit = max(self.reconstructedSignal_values_correspondOriginalTime)
            self.setXRange(0, 5)
            self.plotItem.getViewBox().setLimits(xMin=0, xMax=self.originalSignal_duration, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen='g')        
        
        elif self.reconstructionMethod == 'Fourier Series':
            # taking data needed for the Fourier Series construction from the OriginalGraph instance.
            self.originalSignal_time = originalGraph_instance.originalSignal_time
            self.originalSignal_duration = originalGraph_instance.duration
            self.reconstructedSignal_time = originalGraph_instance.samples_time
            self.reconstructedSignal_values = originalGraph_instance.samples_values

            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the Fourier Series formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.fourier_series(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            self.yLimit = max(self.reconstructedSignal_values_correspondOriginalTime)
            self.setXRange(0, 5)
            self.plotItem.getViewBox().setLimits(xMin=0, xMax=self.originalSignal_duration, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen='g')
        
        elif self.reconstructionMethod == 'Akima Interpolation':
            # taking data needed for the Polynomial Interpolation construction from the OriginalGraph instance.
            self.originalSignal_time = originalGraph_instance.originalSignal_time
            self.originalSignal_duration = originalGraph_instance.duration  
            self.reconstructedSignal_time = originalGraph_instance.samples_time
            self.reconstructedSignal_values = originalGraph_instance.samples_values

            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the Polynomial Interpolation formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.akima_interpolation(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            self.yLimit = max(self.reconstructedSignal_values_correspondOriginalTime)
            self.setXRange(0, 5)
            self.plotItem.getViewBox().setLimits(xMin=0, xMax=self.originalSignal_duration, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen='g')

        elif self.reconstructionMethod == 'Rectangular Interpolation':
            # taking data needed for the Spline Interpolation construction from the OriginalGraph instance.
            self.originalSignal_time = originalGraph_instance.originalSignal_time
            self.originalSignal_duration = originalGraph_instance.duration
            self.reconstructedSignal_time = originalGraph_instance.samples_time
            self.reconstructedSignal_values = originalGraph_instance.samples_values

            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the Spline Interpolation formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.rectangular_interpolation(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            self.yLimit = max(self.reconstructedSignal_values_correspondOriginalTime)
            self.setXRange(0, 5)
            self.plotItem.getViewBox().setLimits(xMin=0, xMax=self.originalSignal_duration, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen='g')
    
    # reconstructing using Whittaker Shannon formula
    def whittaker_shannon(self,t, t_samples, samples):
        """
        Reconstructs a signal using the Whittaker-Shannon interpolation formula.

        Parameters:
        - t : array-like
            Points in time where the reconstructed signal will be evaluated.
        - t_samples : array-like
            Sample times of the original signal.
        - samples : array-like
            Amplitude values of the original signal at each sample time.

        Returns:
        - reconstructed_signal : array-like
            The reconstructed signal evaluated at points t.
        """
        # Calculate the sampling period
        T = t_samples[1] - t_samples[0]  # Assuming uniform spacing

        # Initialize the output array
        reconstructed_signal = np.zeros_like(t, dtype=float)

        # Perform the Whittaker-Shannon interpolation for each point in t
        for i, t_val in enumerate(t):
            # Calculate the sinc terms for each sample
            sinc_terms = samples * np.sinc((t_val - t_samples) / T)
            # Sum the terms to get the reconstructed value
            reconstructed_signal[i] = np.sum(sinc_terms)

        return reconstructed_signal
    # reconstructing using Akima Interpolation formula
    def akima_interpolation(self, t, t_samples, samples):
        """
        Akima interpolation for signal reconstruction.
        
        Params:
        t : array-like
            The time points at which to reconstruct the signal.
        t_samples : array-like
            The sample time points.
        samples : array-like
            The signal values at the sample points.
            
        Returns:
        np.array : The reconstructed signal values at the specified time points t.
        """
        # Use scipy's Akima1DInterpolator for Akima interpolation
        akima_interp = Akima1DInterpolator(t_samples, samples)
        reconstructed_signal = akima_interp(t)
        
        return reconstructed_signal
    # reconstructing using Fourier Series formula
    def fourier_series(self, t, t_samples, samples):
        """
        Fourier Series interpolation for signal reconstruction.
        
        Params:
        t : array-like
            The time points at which to reconstruct the signal.
        t_samples : array-like
            The sample time points.
        samples : array-like
            The signal values at the sample points.
            
        Returns:
        np.array : The reconstructed signal values at the specified time points t.
        """
        T = 1 / self.f_sampling
        reconstructed_signal = np.zeros_like(t)
        for i in range(len(t_samples)):
            reconstructed_signal += samples[i] * np.sinc((t - t_samples[i]) / T)
        return reconstructed_signal

    # reconstructing using Rectangular Interpolation formula
    def rectangular_interpolation(self, t, t_samples, samples):
        # def rectangular_interpolation(self, t, t_samples, samples):
        # spline_interpolation
        """
        Reconstructs a signal using rectangular interpolation.

        Parameters:
        - t : array-like
            Points in time where the reconstructed signal will be evaluated.
        - t_samples : array-like
            Sample times of the original signal.
        - samples : array-like
            Amplitude values of the original signal at each sample time.

        Returns:
        - reconstructed_signal : array-like
            The reconstructed signal evaluated at points t.
        """
        reconstructed_signal = np.zeros_like(t, dtype=float)
        for i, t_val in enumerate(t):
            # Find the closest sample time
            closest_sample_index = np.argmin(np.abs(t_samples - t_val))
            reconstructed_signal[i] = samples[closest_sample_index]
        return reconstructed_signal

###################################################################################################################################  
    
    
class DifferenceGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ShowDifferenceSignal(OriginalSignalGraph(), ReconstructedSignalGraph()) # many variabales of the instance made of this class are intialized in this method when we have just created the instance.
        self.plotItem.getViewBox().sigRangeChanged.connect(self.resetRange)
    
    def resetRange(self):
        currXRange = self.plotItem.getViewBox().viewRange()[0]
        if ((currXRange[1] - currXRange[0]) > 7):
            self.setXRange(0, 5)
            self.setYRange(-self.yLimit - 0.3, self.yLimit + 0.3)
        
        
    def ShowDifferenceSignal(self, originalGraph_instance, reconstructedGraph_instance):
        """
        Params:
        originalGraph_instance (_instance_): already made instance of the OriginalSingalGraph
        reconstructedGraph_instance (_instance_): already made instance of the ReconstructedSignalGraph
            
        """
        self.clear()
        
        # setting up needed some instance variables needed for calculating and plotting the difference signal.
        self.originalSignal_time = originalGraph_instance.originalSignal_time
        self.originalSignal_duration = originalGraph_instance.duration  
        self.originalSignal_values = originalGraph_instance.originalSignal_values
        self.originalSignal_noise = originalGraph_instance.signalNoise
        self.reconstructedSignal_values_correspondOriginalTime = reconstructedGraph_instance.reconstructedSignal_values_correspondOriginalTime  
        self.differenceSignal_values = self.originalSignal_values + self.originalSignal_noise - self.reconstructedSignal_values_correspondOriginalTime 
        self.yLimit = max(self.differenceSignal_values)
        self.setXRange(0, 5)
        self.plotItem.getViewBox().setLimits(xMin=0, xMax=self.originalSignal_duration, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
        self.plot(self.originalSignal_time, self.differenceSignal_values, pen = 'y') # plotting the difference between original and reconstructed signals at the same time values (time values of the original signal).

class FreqSignalGraph(pg.PlotWidget):
    def __init__(self, frequenciesOfInterest, parent=None):
        super().__init__(parent)
        self.ShowSignalFreqDomain(frequenciesOfInterest, OriginalSignalGraph())
    
    
    def ShowSignalFreqDomain(self, frequenciesOfInterest, originalSignal_instance):
       
        self.clear()
        
        # setting up needed values for fourier transform
        self.originalSignal_values = originalSignal_instance.originalSignal_values
        self.signalNoise = originalSignal_instance.signalNoise
        self.originalSignal_time = originalSignal_instance.originalSignal_time
        self.samples_values = originalSignal_instance.samples_values
        self.f_sampling = originalSignal_instance.f_sampling  # Samples per second
        self.signalFreq = originalSignal_instance.signalFreq
        
        self.freq_components = np.fft.fft(self.originalSignal_values + self.signalNoise)   # getting fft for the original signal
        self.frequencies = np.fft.fftfreq(len(self.originalSignal_values + self.signalNoise), self.originalSignal_time[1] - self.originalSignal_time[0])   # getting frequencies
        self.amplitudes = np.abs(self.freq_components)   # getting the amplitude component that each frequency is sharing with
        
        # print(f"used frequencies: {self.frequencies}")  #debugging
        # print(f"-------------------------------------------------------------------")
        # print(f"amplitudes: {self.amplitudes}")
        
        # frequency repetition
        pos_repeated_frequencies = []
        pos_repeated_freq_amps = []
        neg_repeated_frequencies = []
        neg_repeated_freq_amps = []
        low_amplitudes = []
        low_amp_freqs = []
    
        
        # repetiton of the whole signal(positive and negative frequencies "the whole block") in the positive part
        #for loopCounter in range(1, 3):
        for i in range (len(self.frequencies)):
            pos_repeated_frequencies.append(self.frequencies[i] + self.f_sampling)
            pos_repeated_freq_amps.append(self.amplitudes[i])
            
        # repetiton of the whole signal(positive and negative frequencies "the whole block") in the negative part   
        for i in range (len(self.frequencies)):
            neg_repeated_frequencies.append(self.frequencies[i] - self.f_sampling)
            neg_repeated_freq_amps.append(self.amplitudes[i])
        
        for i in range (len(self.frequencies)):
            if self.amplitudes[i] <= 500:
                low_amplitudes.append(self.amplitudes[i])
                low_amp_freqs.append(self.frequencies[i])
        # for setting x and y graph ranges
        max_freq = max(self.frequencies)
        max_repeated_freq = max(pos_repeated_frequencies) 
        max_x_limit = max(max_freq, max_repeated_freq)
        min_freq = min(self.frequencies)
        min_repeated_freq = min(neg_repeated_frequencies) 
        min_x_limit = min(min_freq, min_repeated_freq)
         
        max_amplitude = max(self.amplitudes)
        min_amplitude = min(self.amplitudes)
        
        
        self.setXRange(min_x_limit, max_x_limit)
        self.setYRange(min_amplitude, max_amplitude)
        if self.f_sampling < 2 * self.signalFreq:
            self.plot(pos_repeated_frequencies, pos_repeated_freq_amps, pen = "r")
            self.plot(neg_repeated_frequencies, neg_repeated_freq_amps, pen = "r")
        else:
            self.plot(pos_repeated_frequencies, pos_repeated_freq_amps, pen = "y")
            self.plot(neg_repeated_frequencies, neg_repeated_freq_amps, pen = "y")
        self.plot(self.frequencies, self.amplitudes, pen = "b")
        self.plot(low_amp_freqs, low_amplitudes, "b")
        