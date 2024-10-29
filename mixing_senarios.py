# Description: This file contains the class that will be used to generate the mixing scenarios for the simulation
import numpy as np

class MixingScenarios:
    def __init__(self):
        self.signals = {}
        self.time = np.linespace(0, 1, 1000)
    

    def generate_signal(self, signal_name, signal_params:list):
        """
        This method will generate the sinosoidal signal based on the parameters given
        signal_name: str: The name of the signal
        signal_params: list: The parameters of the signal [frequency, phase]
        
        """
        self.signals[signal_name] = np.sin(2*np.pi*signal_params[0]*self.time + signal_params[1])
        return self.signals[signal_name]