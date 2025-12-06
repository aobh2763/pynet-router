from PySide6.QtWidgets import QDialog
from .ui import UI_RouterSelector

class RouterSelector(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_RouterSelector()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.size())
    
    def get_data(self):
        return self.ui.spin_box.value()