import sys
from main_ui import Ui_Sampler
from PySide6 import QtWidgets
import pyqtgraph as pg
import pandas as pd




# here, we will define the methods and vars related for all the graphs (i.e: browse, clear, ....), not defined specially for one of the four graphs 
    
    
        

class MainWindow(Ui_Sampler, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__();
        self.setupUi(self);
        self.browseSignalButton.clicked.connect(self.browseSignal)
        
        
        
    def browseSignal(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self, caption="Select a CSV file", dir="/D", filter="(*.csv)"
        )
        if filePath:
            self.df = pd.read_csv(filePath, header=None)
            self.browsedSignal = []
            self.browsedSignal = self.df.to_numpy().flatten()
            self.originalSignalPlot.ShowSampledSignal(self.browsedSignal, 5)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication([]);
    window = MainWindow();
    window.show();
    sys.exit(app.exec());