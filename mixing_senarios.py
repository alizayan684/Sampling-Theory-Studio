# Description: This file contains the class that will be used to generate the mixing scenarios for the simulation
import numpy as np

class MixingScenarios:
    def __init__(self):
        self.signals = {}
        self.time = np.linspace(0, 1, 1000)
        self.tests = {}
        self.generate_tests()
    

    def generate_tests(self):
        """ This function will generate the tests that will be used for the simulation"""
        self.tests['test1'] = {'signal1': [2, 0], 'signal2': [6, 0], 'fmax': 6}
        self.tests['test2'] = {'signal1': [11, 0], 'signal2': [12, 0], 'signal3': [10, 10], 'fmax': 12}
        self.tests['test3'] = {'signal1': [1, 30], 'signal2': [10, 30], 'signal3': [30, 10], 'signal4': [20, 20], 'fmax': 30}

    def generate_signal(self, signal_name, signal_params:list):
        """
        This method will generate the sinosoidal signal based on the parameters given
        signal_name: str: The name of the signal
        signal_params: list: The parameters of the signal [frequency, phase]
        
        """
        self.signals[signal_name] = np.sin(2*np.pi*signal_params[0]*self.time + signal_params[1])
    
    def mix_signals(self):
        """ this function will mix all the signals that have been generated""" 
        mixed_signal = np.zeros(len(self.time))
        signals = self.signals.values()
        for signal in signals:
            mixed_signal += signal
        return mixed_signal
    
    def generate_mixed_signal(self, test_name):
        """
        This function will generate the mixed signal based on the test name
        test_name: str: The name of the test
        """
        self.signals = {}
        test = self.tests[test_name]
        for signal_name, signal_params in test.items():
            if signal_name != 'fmax':
               self.generate_signal(signal_name, signal_params)
        return self.mix_signals()
    