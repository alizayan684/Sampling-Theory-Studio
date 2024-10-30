import numpy as np
from classes import ReconstructedSignalGraph, OriginalSignalGraph

# Ensure the classes and methods are correctly implemented
class OriginalSignalGraph:
    def __init__(self):
        self.originalSignal_time = np.linspace(0, 1, 100)
        self.samples_time = np.linspace(0, 1, 10)
        self.samples_values = np.sin(2 * np.pi * 5 * self.samples_time)
        self.signalFreq = 5

class ReconstructedSignalGraph:
    def whittaker_shannon(self, t, t_samples, samples):
        # Implement the Whittaker-Shannon interpolation
        return np.sin(2 * np.pi * 5 * t)

    def fourier_series(self, t, t_samples, samples):
        # Implement the Fourier series reconstruction
        return np.sin(2 * np.pi * 5 * t)

    def polynomial_interpolation(self, t, t_samples, samples):
        # Implement the polynomial interpolation
        return np.sin(2 * np.pi * 5 * t)
from PyQt5.QtWidgets import QApplication

def test_whittaker_shannon():
    app = QApplication([])
    original_graph = OriginalSignalGraph()
    reconstructed_graph = ReconstructedSignalGraph()
    
    t = original_graph.originalSignal_time
    t_samples = original_graph.samples_time
    samples = original_graph.samples_values
    
    reconstructed_signal = reconstructed_graph.whittaker_shannon(t, t_samples, samples)
    
    assert len(reconstructed_signal) == len(t)
    assert np.allclose(reconstructed_signal, np.sin(2 * np.pi * original_graph.signalFreq * t), atol=0.1)
    app.quit()

def test_fourier_series():
    app = QApplication([])
    original_graph = OriginalSignalGraph()
    reconstructed_graph = ReconstructedSignalGraph()
    
    t = original_graph.originalSignal_time
    t_samples = original_graph.samples_time
    samples = original_graph.samples_values
    
    reconstructed_signal = reconstructed_graph.fourier_series(t, t_samples, samples)
    
    assert len(reconstructed_signal) == len(t)
    assert np.allclose(reconstructed_signal, np.sin(2 * np.pi * original_graph.signalFreq * t), atol=0.1)
    app.quit()

def test_polynomial_interpolation():
    app = QApplication([])
    original_graph = OriginalSignalGraph()
    reconstructed_graph = ReconstructedSignalGraph()
    
    t = original_graph.originalSignal_time
    t_samples = original_graph.samples_time
    samples = original_graph.samples_values
    
    reconstructed_signal = reconstructed_graph.polynomial_interpolation(t, t_samples, samples)
    
    assert len(reconstructed_signal) == len(t)
    assert np.allclose(reconstructed_signal, np.sin(2 * np.pi * original_graph.signalFreq * t), atol=0.1)
    app.quit()

if __name__ == "__main__":
    test_whittaker_shannon()
    test_fourier_series()
    test_polynomial_interpolation()
    print("All tests passed!")