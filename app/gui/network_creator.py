from PySide6.QtWidgets import QDialog
from .ui import UI_NetworkCreator

class NetworkCreator(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_NetworkCreator()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.size())
    
    def get_data(self):
        return {
            "name": self.ui.name_input.text()
        }