from ..router_creator import RouterCreator
from ..network_creator import NetworkCreator
from ..router_selector import RouterSelector
from ..router_editor import RouterEditor
from app.model import Network

class MainHandlers:
    def __init__(self, parent, network: Network):
        self.parent = parent
        self.network = network
    
    def display_routers(self):
        text = "Routers in the network:\n"
        
        for router in self.network.routers:
            text += f"{router}\n"
        
        self.parent.ui.textBrowser.setText(text)
        
    def new_network_clicked(self):
        dialog = NetworkCreator()
        
        if dialog.exec():
            data = dialog.get_data()
            
            if data["name"] == "":
                self.parent.ui.textBrowser.setText("Network name cannot be empty.")
                return
            
            if data["name"].isalnum() == False:
                self.parent.ui.textBrowser.setText("Network name must be alphanumeric.")
                return
            
            self.network = Network(0, data["name"])
            self.parent.network = self.network
            
            self.parent.ui.textBrowser.setText("New network created.")
            
            self.parent.ui.save_network_button.setDisabled(False)
            self.parent.ui.add_router_button.setDisabled(False)
            self.parent.ui.edit_router_button.setDisabled(False)
            self.parent.ui.delete_router_button.setDisabled(False)
            self.parent.ui.link_routers_button.setDisabled(False)
            self.parent.ui.set_constraints_button.setDisabled(False)
            self.parent.ui.find_route_button.setDisabled(False)
        
    def add_router_clicked(self):
        dialog = RouterCreator()
        self.display_routers()
        
        dialog.ui.id_input.setValue(self.network.router_count)
        dialog.ui.id_input.setEnabled(False)
        
        if dialog.exec():
            data = dialog.get_data()
            
            if isinstance(data, str):
                self.parent.ui.textBrowser.setText(data)
                return
            
            self.network.add_router(
                data["name"],
                data["x"],
                data["y"],
                data["security_level"],
                data["firewall_enabled"]
            )
            
        self.display_routers()
        
    def edit_router_clicked(self):
        dialog1 = RouterSelector()
        self.display_routers()
        
        if not dialog1.exec():
            return
        
        router_id = dialog1.get_data()
        router = self.network.get_router_by_id(router_id)
        
        if router is None:
            self.parent.ui.textBrowser.setText("Selected router not found.")
            return
        
        dialog2 = RouterEditor(router)
        dialog2.ui.id_input.setEnabled(False)
        
        if dialog2.exec():
            data = dialog2.get_data()
            
            if isinstance(data, str):
                self.parent.ui.textBrowser.setText(data)
                return
            
            router.name = data["name"]
            router.x = data["x"]
            router.y = data["y"]
            router.security_level = data["security_level"]
            router.firewall_enabled = data["firewall_enabled"]
            
        self.display_routers()
    
    def delete_router_clicked(self):
        dialog = RouterSelector()
        self.display_routers()
        
        if not dialog.exec():
            return
        
        router_id = dialog.get_data()
        router = self.network.get_router_by_id(router_id)
        
        if router is None:
            self.parent.ui.textBrowser.setText("Selected router not found.")
            return
        
        self.network.remove_router(router)
        
        self.display_routers()