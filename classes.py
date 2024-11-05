from PySide6 import QtWidgets
import pyqtgraph as pg
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline

class OriginalSignalGraph(pg.PlotWidget):
    def __init__(self, parent = None):
        super().__init__(parent )
        self.signalFreq = 5 # initializing frequency of the original signal (a default signal with freq = 5 Hz before browsing any signal) (cycles per second)
        self.f_sampling = 4 * self.signalFreq # initializing sampling frequency to sample the signal (samples per second)
        self.duration = 1  # duration of the signal
        self.originalSignal_time =  np.linspace(0, self.duration,  1000) # initializing x values of the original signal(time domain)
        self.originalSignal_values = np.sin(2 * np.pi * self.signalFreq * self.originalSignal_time)  # initialization of the graph's original signal values
        self.yLimit = max(self.originalSignal_values)
        self.samples_time = np.arange(0, self.duration, step= 1/self.f_sampling) 
        self.samples_values = np.sin(2 * np.pi * self.signalFreq * self.samples_time)
        self.signalNoise = 0
        self.sampleNoise = 0
        self.ShowSampledSignal(self.originalSignal_values, self.signalNoise, self.signalFreq, self.yLimit, self.f_sampling, self.samples_values, self.sampleNoise, self.originalSignal_time) # showing default signal when openning the application
        
    # showing sampled signal in the graph    
    def ShowSampledSignal(self, originalSignal, signalNoise, signalFreq, yLimit, f_sampling, samples_values, sampleNoise, originalSignal_time = None): 
        # I pass the "originalSignal_time" as it will be needed for the default signal that occurs when starting the application and also to keep  the same signal time when changing the slider
        self.clear()
        self.originalSignal_values = originalSignal
        self.signalNoise = signalNoise
        self.signalFreq = signalFreq
        # self.yLimit = yLimit
        self.f_sampling = f_sampling
        self.samples_values = samples_values
        self.sampleNoise = sampleNoise
        self.originalSignal_time = originalSignal_time
        # if self.originalSignal_time is None :
        #     pass
        self.yLimit = max(self.originalSignal_values)
        self.plotItem.getViewBox().setLimits(xMin=0, xMax=1, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
        self.plot(self.originalSignal_time, self.originalSignal_values + self.signalNoise, pen = 'r')
        self.samples_time = np.arange(0, self.duration, step= 1/self.f_sampling)
        self.plot(self.samples_time, self.samples_values, pen=None, symbol='o', symbolBrush='b', symbolSize=8, name="Samples")

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
        self.reconstructedSignal_values = OriginalSignalGraph().samples_values + OriginalSignalGraph().sampleNoise
        self.reconstructionMethod = 'whittaker shannon' # initializing the reconstruction method to be whittaker shannon method.
        # self.reconstructionMethod = ['whittaker shannon','Fourier Series' , 'Polynomial Interpolation','Spline Interpolation']
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
            self.sampleNoise = originalGraph_instance.sampleNoise
            
            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the whittaker shannon formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.whittaker_shannon(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            self.yLimit = max(self.reconstructedSignal_values_correspondOriginalTime)
            self.plotItem.getViewBox().setLimits(xMin=0, xMax=1, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime + self.sampleNoise, pen='g')        
        
        elif self.reconstructionMethod == 'Fourier Series':
            # taking data needed for the Fourier Series construction from the OriginalGraph instance.
            self.originalSignal_time = originalGraph_instance.originalSignal_time
            self.reconstructedSignal_time = originalGraph_instance.samples_time
            self.reconstructedSignal_values = originalGraph_instance.samples_values

            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the Fourier Series formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.fourier_series(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            self.yLimit = max(self.reconstructedSignal_values_correspondOriginalTime)
            self.plotItem.getViewBox().setLimits(xMin=0, xMax=1, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen='g')
        
        elif self.reconstructionMethod == 'Polynomial Interpolation':
            # taking data needed for the Polynomial Interpolation construction from the OriginalGraph instance.
            self.originalSignal_time = originalGraph_instance.originalSignal_time
            self.reconstructedSignal_time = originalGraph_instance.samples_time
            self.reconstructedSignal_values = originalGraph_instance.samples_values

            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the Polynomial Interpolation formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.polynomial_interpolation(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            self.yLimit = max(self.reconstructedSignal_values_correspondOriginalTime)
            self.plotItem.getViewBox().setLimits(xMin=0, xMax=1, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen='g')

        elif self.reconstructionMethod == 'Spline Interpolation':
            # taking data needed for the Spline Interpolation construction from the OriginalGraph instance.
            self.originalSignal_time = originalGraph_instance.originalSignal_time
            self.reconstructedSignal_time = originalGraph_instance.samples_time
            self.reconstructedSignal_values = originalGraph_instance.samples_values

            # getting the reconstructed signal values corresponding to the original signal time values. (same as interpolation did but here we are using the Spline Interpolation formula)
            self.reconstructedSignal_values_correspondOriginalTime = self.spline_interpolation(self.originalSignal_time, self.reconstructedSignal_time, self.reconstructedSignal_values)
            self.yLimit = max(self.reconstructedSignal_values_correspondOriginalTime)
            self.plotItem.getViewBox().setLimits(xMin=0, xMax=1, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
            self.plot(self.originalSignal_time, self.reconstructedSignal_values_correspondOriginalTime, pen='g')

            
            

    
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
 
    # def fourier_series(self, t, t_samples, samples, num_terms=10):
    #     """
    #     Reconstructs a signal using the Fourier series.

    #     Parameters:
    #     - t : array-like
    #         The points in time at which to evaluate the reconstructed signal.
    #     - t_samples : array-like
    #         Sample times of the original signal.
    #     - samples : array-like
    #         Amplitude values of the original signal at each sample time.
    #     - num_terms : int
    #         Number of Fourier terms (harmonics) to include in the reconstruction.

    #     Returns:
    #     - reconstructed_signal : array-like
    #         The reconstructed signal evaluated at points t.
    #     """

    #     # Calculate the period of the signal from t_samples (assuming it is periodic)
    #     T = t_samples[-1] - t_samples[0]
    #     f0 = 1 / T  # Fundamental frequency

    #     # Compute the Fourier coefficients a_0, a_k, b_k
    #     a_0 = (2 / len(t_samples)) * np.sum(samples)  # DC component
    #     reconstructed_signal = a_0 / 2  # Initialize with half the DC component

    #     # Loop over the number of terms (harmonics) to calculate a_k and b_k
    #     for k in range(1, num_terms + 1):
    #         # Cosine and sine terms
    #         a_k = (2 / len(t_samples)) * np.sum(samples * np.cos(2 * np.pi * k * f0 * t_samples))
    #         b_k = (2 / len(t_samples)) * np.sum(samples * np.sin(2 * np.pi * k * f0 * t_samples))

    #         # Add the k-th term to the reconstructed signal
    #         reconstructed_signal += a_k * np.cos(2 * np.pi * k * f0 * t) + b_k * np.sin(2 * np.pi * k * f0 * t)

    #     return reconstructed_signal
    
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
    # reconstructing using Polynomial Interpolation formula
    def polynomial_interpolation(self, t, t_samples, samples):
        """
        Polynomial interpolation for signal reconstruction.
        
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
        # Use numpy's polyfit and polyval for polynomial interpolation
        coefficients = np.polyfit(t_samples, samples, deg=len(t_samples) - 1)
        reconstructed_signal = np.polyval(coefficients, t)
        
        return reconstructed_signal
    
    # reconstructing using Spline Interpolation formula
    def spline_interpolation(self, t, t_samples, samples):
        # def rectangular_interpolation(self, t, t_samples, samples):
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
        
        
    def ShowDifferenceSignal(self, originalGraph_instance, reconstructedGraph_instance):
        """
        Params:
        originalGraph_instance (_instance_): already made instance of the OriginalSingalGraph
        reconstructedGraph_instance (_instance_): already made instance of the ReconstructedSignalGraph
            
        """
        self.clear()
        
        # setting up needed some instance variables needed for calculating and plotting the difference signal.
        self.originalSignal_time = originalGraph_instance.originalSignal_time  
        self.originalSignal_values = originalGraph_instance.originalSignal_values + originalGraph_instance.signalNoise
        self.reconstructedSignal_values_correspondOriginalTime = reconstructedGraph_instance.reconstructedSignal_values_correspondOriginalTime  
        self.differenceSignal_values = self.originalSignal_values - self.reconstructedSignal_values_correspondOriginalTime 
        #print(self.differenceSignal_values) # for checking the difference between both signals in the terminal
        self.yLimit = max(self.differenceSignal_values)
        self.plotItem.getViewBox().setLimits(xMin=0, xMax=1, yMin=-self.yLimit - 0.3, yMax=self.yLimit + 0.3)
        self.plot(self.originalSignal_time, self.differenceSignal_values, pen = 'y') # plotting the difference between original and reconstructed signals at the same time values (time values of the original signal).

class FreqSignalGraph(pg.PlotWidget):
    def __init__(self, frequenciesOfInterest, parent=None):
        super().__init__(parent)
        self.ShowSignalFreqDomain(frequenciesOfInterest, OriginalSignalGraph())
    
    
    def ShowSignalFreqDomain(self, frequenciesOfInterest, originalSignal_instance):
        """
        Params:
        frequenciesOfInterest: all frequencies in the mix of signals I plot. note: it's passed by copy not by reference.
        originalSignal_instance: already made instance of the OriginalSignalGraph to plot the corresponding signal in the frequency domain graph.
        """
        self.clear()
        
        # setting up needed values for fourier transform
        self.originalSignal_values = originalSignal_instance.originalSignal_values
        self.f_sampling = originalSignal_instance.f_sampling  # Samples per second
        self.f_max =  originalSignal_instance.signalFreq
        
        aliasedFrequencies = []
        negativeFrequencies = [-freq for freq in frequenciesOfInterest] # forming the negative frequencies
        frequenciesOfInterest += negativeFrequencies  # appending the negative frequencies to the frequencies of interest array
        
        for i in range (len(frequenciesOfInterest)):
            if np.abs(frequenciesOfInterest[i]) > (self.f_sampling / 2):   # f_sampling/2 is the niquist frequency
                n = int(max(self.f_sampling, np.abs(frequenciesOfInterest[i])) / min(self.f_sampling, np.abs(frequenciesOfInterest[i])))  # n represents multiples of f_sampling that we must subtract from the frequency that is above the nyquist frequency to go in to the range of frequencies below or equal to the nyquist freq (f_sampling/2)
                
                if frequenciesOfInterest[i] >= 0: # check whether the freq is +ve or -ve to adjust the aliasing formula
                    aliased_freq = np.abs(frequenciesOfInterest[i] - n * self.f_sampling)  # formula: f_aliasing = | f - n * fs |
                else:
                    aliased_freq = - np.abs( np.abs(frequenciesOfInterest[i]) - n * self.f_sampling)
                # Add the aliased frequency to the aliased frequencies list
                aliasedFrequencies.append(aliased_freq)
                
                # replace this out of nyquist range frequency with its corresponding aliasing frequency
                frequenciesOfInterest[i] = aliased_freq  
                #print(frequenciesOfInterest)
                
        # Frequency domain
        fft_freqs = np.fft.fftfreq(len(self.originalSignal_values), 1 / 22)  # Frequency bins
        
        # Only plot the positive frequencies
        #positive_freqs = fft_freqs[:len(fft_freqs) // 2]
        impulse_magnitude = np.zeros_like(fft_freqs)
        
        for freq in frequenciesOfInterest:
            impulse_index = np.where(np.isclose(fft_freqs, freq, atol=1e-2))[0]  # Find index for frequency components
            if impulse_index.size > 0:
                impulse_magnitude[impulse_index] = 1  # Set the impulse magnitude
                
        #if self.f_sampling < 2 * self.f_max:
        for freq in frequenciesOfInterest:
            impulse_index = np.where(np.isclose(fft_freqs, freq, atol=1e-2))[0]  # Find index for frequency components
            if impulse_index.size > 0:
                impulse_magnitude[impulse_index] = 1  # Set the impulse magnitude
                    
        if impulse_index.size > 0:
            # Choose color based on frequency
            if freq <= (self.f_sampling / 2):
                color = 'g'  # Green for frequencies <= Nyquist
            else:
                color = 'r' 

        # Plotting the frequency domain representation
        self.setXRange(-11, 11)  # Set x-axis range from 0 to 11
        self.plotItem.getViewBox().setLimits(xMin=-11, xMax=11, yMin=-0.02, yMax=0.3)
        self.plot(fft_freqs, impulse_magnitude, pen = 'b')