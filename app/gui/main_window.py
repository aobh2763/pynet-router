from PySide6.QtWidgets import QMainWindow, QApplication
from .ui import UI_MainWindow
from .handlers import GraphicsHandler, MainHandlers

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.network = None
        self.latest_path = None
        self.ui.setupUi(self)
        
        # Make unresizable
        self.setFixedSize(self.size())
        
        # Center window
        frame_geo = self.frameGeometry()
        screen_center = QApplication.primaryScreen().availableGeometry().center()
        frame_geo.moveCenter(screen_center)
        self.move(frame_geo.topLeft())
        
        self.graphics = GraphicsHandler(self.ui.graphicsView)
        self.builder = None
        self.solver = None
        self.handlers = MainHandlers(self, self.network, self.graphics, self.builder, self.solver)
        
        self.ui.new_network_button.clicked.connect(self.handlers.new_network_clicked)
        self.ui.add_router_button.clicked.connect(self.handlers.add_router_clicked)
        self.ui.edit_router_button.clicked.connect(self.handlers.edit_router_clicked)
        self.ui.delete_router_button.clicked.connect(self.handlers.delete_router_clicked)
        self.ui.link_routers_button.clicked.connect(self.handlers.link_routers_clicked)
        self.ui.save_network_button.clicked.connect(self.handlers.save_network_clicked)
        self.ui.load_network_button.clicked.connect(self.handlers.load_network_clicked)
        self.ui.set_constraints_button.clicked.connect(self.handlers.set_constraints_clicked)
        self.ui.find_route_button.clicked.connect(self.handlers.find_route_clicked)
        
        self.ui.actionAdd_Router.triggered.connect(self.handlers.add_router_clicked)
        self.ui.actionEdit_Router.triggered.connect(self.handlers.edit_router_clicked)
        self.ui.actionDelete_Router.triggered.connect(self.handlers.delete_router_clicked)
        self.ui.actionLink_Routers.triggered.connect(self.handlers.link_routers_clicked)
        self.ui.actionNew_Network.triggered.connect(self.handlers.new_network_clicked)
        self.ui.actionDisplay_Routers.triggered.connect(self.handlers.display_routers_clicked)
        self.ui.actionDisplay_Latest_Path.triggered.connect(self.handlers.display_latest_path_clicked)
        self.ui.actionHide_Latest_Path.triggered.connect(self.handlers.hide_latest_path_clicked)
        self.ui.actionSet_Constraints.triggered.connect(self.handlers.set_constraints_clicked)
        self.ui.actionFind_Route.triggered.connect(self.handlers.find_route_clicked)
        self.ui.actionSave_Network.triggered.connect(self.handlers.save_network_clicked)
        self.ui.actionLoad_Network.triggered.connect(self.handlers.load_network_clicked)
        
        self.ui.save_network_button.setDisabled(True)
        self.ui.add_router_button.setDisabled(True)
        self.ui.edit_router_button.setDisabled(True)
        self.ui.link_routers_button.setDisabled(True)
        self.ui.delete_router_button.setDisabled(True)
        self.ui.set_constraints_button.setDisabled(True)
        self.ui.find_route_button.setDisabled(True)
        
        self.ui.actionAdd_Router.setDisabled(True)
        self.ui.actionEdit_Router.setDisabled(True)
        self.ui.actionDelete_Router.setDisabled(True)
        self.ui.actionLink_Routers.setDisabled(True)
        self.ui.actionSave_Network.setDisabled(True)
        self.ui.actionSet_Constraints.setDisabled(True)
        self.ui.actionFind_Route.setDisabled(True)
        self.ui.actionDisplay_Routers.setDisabled(True)
        self.ui.actionDisplay_Latest_Path.setDisabled(True)
        self.ui.actionHide_Latest_Path.setDisabled(True)