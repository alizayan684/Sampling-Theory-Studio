
from main_ui  import Ui_Sampler
from PySide6.QtWidgets import QApplication

import sys
class Composer(Ui_Sampler):
    def __init__(self):
        super(Composer, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    composer = Composer()
    composer.show()
    sys.exit(app.exec())