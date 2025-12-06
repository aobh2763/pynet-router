from PySide6.QtWidgets import QDialog
from .ui import UI_RouterCreator

class RouterCreator(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_RouterCreator()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.size())
    
    def validate_data(self, name, x, y, security_level, firewall_enabled):
        msg = ""
        if name == "":
            msg += "Name cannot be empty.\n"
        
        if not (-2.0 <= x <= 21.0):
            msg += "X coordinate must be between -2 and 21.\n"
        
        if not (-1.0 <= y <= 12.0):
            msg += "Y coordinate must be between -1 and 12.\n"
        
        if not (1 <= security_level <= 5):
            msg += "Security level must be between 1 and 5.\n"
        
        if msg == "":
            return "Valid"
        else:
            return msg
    
    def get_data(self):
        if (self.ui.firewall_input.value() == 1):
            firewall_enabled = True
        else:
            firewall_enabled = False
            
        validation_result = self.validate_data(
            self.ui.name_input.text(),
            self.ui.x_input.value(),
            self.ui.y_input.value(),
            self.ui.security_input.value(),
            firewall_enabled
        )
        
        if (validation_result != "Valid"):
            return validation_result
        
        return {
            "name": self.ui.name_input.text(),
            "x": self.ui.x_input.value(),
            "y": self.ui.y_input.value(),
            "security_level": self.ui.security_input.value(),
            "firewall_enabled": firewall_enabled
        }