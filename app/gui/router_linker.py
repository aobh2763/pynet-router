from PySide6.QtWidgets import QDialog
from .ui import UI_RouterLinker

class RouterLinker(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_RouterLinker()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.size())