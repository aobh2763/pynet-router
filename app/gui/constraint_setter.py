from PySide6.QtWidgets import QDialog
from .ui import UI_ConstraintSetter

class ConstraintSetter(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_ConstraintSetter()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.size())
         
    def get_data(self):
        if (self.ui.firewall_input.value() == 1):
            firewall_required = True
        else:
            firewall_required = False
        
        return {
            "source": self.ui.source_input.value(),
            "destination": self.ui.destination_input.value(),
            "security_requirement": self.ui.security_input.value(),
            "firewall_required": firewall_required
        }