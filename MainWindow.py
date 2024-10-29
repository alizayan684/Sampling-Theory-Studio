import sys
from main_ui import Ui_Sampler
from PySide6 import QtWidgets
import pyqtgraph as pg
import pandas as pd

class MainWindow(Ui_Sampler, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__();
        self.setupUi(self);
        
        # setting up sampling slider values
        self.samplingFreqSlider.setMinimum( 0.5 * self.originalSignalPlot.signalFreq)  # min value
        self.samplingFreqSlider.setMaximum( 7 * self.originalSignalPlot.signalFreq)   # max value
        self.samplingFreqSlider.setValue( self.originalSignalPlot.f_sampling)    # inital value
        self.normFreqLCD.display(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.actualFreqLCD.display(self.samplingFreqSlider.value())
        
        self.samplingFreqSlider.valueChanged.connect(self.setSamplingSliderValue)
        self.browseSignalButton.clicked.connect(self.browseSignal)        
        
    def browseSignal(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self, caption="Select a CSV file", dir="/D", filter="(*.csv)"
        )
        if filePath:
            self.df = pd.read_csv(filePath, header=None)
            self.browsedSignal = []
            self.browsedSignal = self.df.to_numpy().flatten()
            self.originalSignalPlot.ShowSampledSignal(self.browsedSignal)
            self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
            self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
            self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)    
    
    def setSamplingSliderValue(self):
        print(f"current value: {self.samplingFreqSlider.value()}")
        self.originalSignalPlot.f_sampling = self.samplingFreqSlider.value()
        self.normFreqLCD.display(float(self.samplingFreqSlider.value()/self.originalSignalPlot.signalFreq))
        self.actualFreqLCD.display(self.samplingFreqSlider.value())
        self.originalSignalPlot.ShowSampledSignal(originalSignal= self.originalSignalPlot.originalSignal_values, signalFreq= self.originalSignalPlot.signalFreq, yLimit= self.originalSignalPlot.yLimit, f_sampling = self.originalSignalPlot.f_sampling, originalSignal_time= self.originalSignalPlot.originalSignal_time)
        self.sampledSignalPlot.ReconstructSampledSignal(self.originalSignalPlot, reconstructionMethod = self.sampledSignalPlot.reconstructionMethod)
        self.differencePlot.ShowDifferenceSignal(self.originalSignalPlot, self.sampledSignalPlot)
        self.frequencyDomainPlot.ShowSignalFreqDomain(self.originalSignalPlot)
            
if __name__ == '__main__':
    app = QtWidgets.QApplication([]);
    window = MainWindow();
    window.show();
    sys.exit(app.exec());
