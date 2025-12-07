from PySide6.QtWidgets import QMainWindow, QApplication
from .ui import UI_MainWindow
from .handlers import GraphicsHandler, MainHandlers

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.network = None
        self.ui.setupUi(self)
        
        # Make unresizable
        self.setFixedSize(self.size())
        
        # Center window
        frame_geo = self.frameGeometry()
        screen_center = QApplication.primaryScreen().availableGeometry().center()
        frame_geo.moveCenter(screen_center)
        self.move(frame_geo.topLeft())
        
        self.graphics = GraphicsHandler(self.ui.graphicsView)
        self.handlers = MainHandlers(self, self.network, self.graphics)
        
        self.ui.new_network_button.clicked.connect(self.handlers.new_network_clicked)
        self.ui.add_router_button.clicked.connect(self.handlers.add_router_clicked)
        self.ui.edit_router_button.clicked.connect(self.handlers.edit_router_clicked)
        self.ui.delete_router_button.clicked.connect(self.handlers.delete_router_clicked)
        self.ui.link_routers_button.clicked.connect(self.handlers.link_routers_clicked)
        self.ui.save_network_button.clicked.connect(self.handlers.save_network_clicked)
        self.ui.load_network_button.clicked.connect(self.handlers.load_network_clicked)
        
        self.ui.save_network_button.setDisabled(True)
        self.ui.add_router_button.setDisabled(True)
        self.ui.edit_router_button.setDisabled(True)
        self.ui.link_routers_button.setDisabled(True)
        self.ui.delete_router_button.setDisabled(True)
        self.ui.set_constraints_button.setDisabled(True)
        self.ui.find_route_button.setDisabled(True)
        
        