from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np
from scipy.interpolate import interp1d

class OriginalSignalGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent )
        self.signalFreq = 2 # initializing frequency of the original signal (a default signal with freq = 5 Hz before browsing any signal) (cycles per second)
        self.f_sampling = 3 * self.signalFreq # initializing sampling frequency to sample the signal (samples per second)
        self.duration = 1  # duration of the signal
        self.originalSignal_time =  np.linspace(0, self.duration,  1000) # initializing x values of the original signal(time domain)
        self.originalSignal_values = np.sin(2 * np.pi * self.signalFreq * self.originalSignal_time)  # initialization of the graph's original signal values
        self.ShowSampledSignal(self.originalSignal_values, self.signalFreq, self.f_sampling, self.originalSignal_time) # showing default signal when openning the application..]
       
        
        
    # showing sampled signal in the graph    
    def ShowSampledSignal(self, originalSignal, signalFreq, f_sampling, originalSignal_time = None):  # I pass the "originalSignal_time" as it will be needed for the default signal that occurs when starting the application
        self.clear()
        self.originalSignal = originalSignal
        self.signalFreq = signalFreq
        self.f_sampling = f_sampling
        self.originalSignal_time = originalSignal_time
        if self.originalSignal_time is None :
            pass
        
        self.plot(self.originalSignal_time, self.originalSignal_values, pen = 'r')
        self.samples_time = np.linspace(0, self.duration, int(self.duration * self.f_sampling))
        self.samples_values = np.sin(2 * np.pi * self.signalFreq * self.samples_time)
        self.plot(self.samples_time, self.samples_values, pen=None, symbol='o', symbolBrush='b', symbolSize=8, name="Samples")


##################################################################################################################################


class ReconstructedSignalGraph(pg.PlotWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize necessary values for Whittaker-Shannon reconstruction ( corresponding to the initial values of the instance made of the 'OriginalGraphSignal' class).
        self.originalSignal_time = OriginalSignalGraph().originalSignal_time
        self.signalFreq = OriginalSignalGraph().signalFreq
        self.f_sampling = OriginalSignalGraph().f_sampling
        self.duration = OriginalSignalGraph().duration
        self.reconstructedSignal_time = OriginalSignalGraph().samples_time
        self.reconstructedSignal_values = OriginalSignalGraph().samples_values
        self.reconstructionMethod = 'whittaker shannon' # initializing the reconstruction method to be whittaker shannon method.
        
        self.ReconstructSampledSignal(OriginalSignalGraph(), self.reconstructionMethod)

        
        
         
        
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
            self.reconstructedSignal_time = originalGraph_instance.samples_time
            self.reconstructedSignal_values = originalGraph_instance.samples_values
            
            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the whittaker shannon formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.whittaker_shannon(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            # Plot the reconstructed signal
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen='g')
            
            
            
            
    # reconstructing using Whittaker Shannon formula
    def whittaker_shannon(self, t, t_samples, samples):
        """
        Whittaker-Shannon interpolation for signal reconstruction.
        
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
        sinc_matrix = np.sinc((t[:, None] - t_samples[None, :]) / T)  # forming a matrix to apply the summation in the Whittaker Shannon formula without an explicit for loop.
        reconstructed_signal = np.dot(sinc_matrix, samples) # applying the summation
        
        return reconstructed_signal
        


####################################################################################################################################  
    
class DifferenceGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ShowDifferenceSignal(OriginalSignalGraph(), ReconstructedSignalGraph()) # many variabales of the instance made of this class are intialized in this method when we have just created the instance.
        
        
        
    def ShowDifferenceSignal(self, originalGraph_instance, reconstructedGraph_instance):
        """
        Params:
        originalGraph_instance (_instance_): already made instance of the OriginalSingalGraph
        reconstructedGraph_instance (_instance_): already made instance of the ReconstructedSignalGraph
            
        """
        self.clear()
        
        # setting up needed some instance variables needed for calculating and plotting the difference signal.
        self.originalSignal_time = originalGraph_instance.originalSignal_time  
        self.originalSignal_values = originalGraph_instance.originalSignal_values  
        self.reconstructedSignal_values_correspondOriginalTime = reconstructedGraph_instance.reconstructedSignal_values_correspondOriginalTime  
        self.differenceSignal_values = self.originalSignal_values - self.reconstructedSignal_values_correspondOriginalTime 
        #print(self.differenceSignal_values) # for checking the difference between both signals in the terminal
        self.setYRange(-1, 1)
        self.plot(self.originalSignal_time, self.differenceSignal_values, pen = 'y') # plotting the difference between original and reconstructed signals at the same time values (time values of the original signal).
        
        
        
################################################################################################################################


class FreqSignalGraph(pg.PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ShowSignalFreqDomain(OriginalSignalGraph())
    
    
    def ShowSignalFreqDomain(self, originalSignal_instance):
        
        """
        Params:
        originalSignal_instance: already made instance of the OriginalSignalGraph to plot the corresponding signal in the frequency domain graph.
        
        """
        self.clear()
        
        # setting up needed values for fourier transform
        self.originalSignal_values = originalSignal_instance.originalSignal_values
        self.f_sampling = originalSignal_instance.f_sampling  # samples per second
        
        # Frequency domain
        fft_values = np.fft.fft(self.originalSignal_values)           # apply FFT (contains complex values representing the amplitude and phase info)
        fft_freqs = np.fft.fftfreq(len(self.originalSignal_values), 1 / self.f_sampling)  # frequency bins
        fft_magnitude = np.abs(fft_values) / len(self.originalSignal_values)  # magnitude (normalized) (extracting the magnitude from the complex values)
        
        self.plot(fft_freqs, fft_magnitude, pen = 'b')