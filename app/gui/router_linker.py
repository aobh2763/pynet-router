from PySide6.QtWidgets import QDialog
from .ui import UI_RouterLinker

class RouterLinker(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_RouterLinker()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.size())
    
    def get_data(self):
        return {
            "router1": self.ui.router_a_input.value(),
            "router2": self.ui.router_b_input.value(),
            "cost": self.ui.cost_input.value()
        }