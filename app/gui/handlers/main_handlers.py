from ..router_creator import RouterCreator
from ..network_creator import NetworkCreator
from ..router_selector import RouterSelector
from ..router_editor import RouterEditor
from ..router_linker import RouterLinker

from app.model import Network, Link

from app.io import FileReader, FileWriter

from PySide6.QtWidgets import QListWidgetItem, QFileDialog
from PySide6.QtCore import Qt

class MainHandlers:
    def __init__(self, parent, network: Network, graphics_handler):
        self.parent = parent
        self.network = network
        self.graphics_handler = graphics_handler
    
    def display_routers(self):
        text = "Routers in the network:\n"
        
        for router in self.network.routers:
            text += f"{router}\n"
        
        self.parent.ui.textBrowser.setText(text)
        
    def new_network_clicked(self):
        dialog = NetworkCreator()
        
        if not dialog.exec():
            return
            
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
        
    def add_router_clicked(self):
        dialog = RouterCreator()
        self.display_routers()
        
        dialog.ui.id_input.setValue(self.network.router_count)
        dialog.ui.id_input.setEnabled(False)
        
        if not dialog.exec():
            return
        
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
        self.graphics_handler.update_graphics(self.network)
        
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
        
        for link in router.links:
            item = QListWidgetItem(str(link))
            item.setData(Qt.UserRole, link)
            dialog2.ui.link_list.addItem(item)
        
        dialog2.ui.delete_selected.clicked.connect(lambda: self.delete_selected_clicked(dialog2))
        
        if not dialog2.exec():
            return
        
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
        self.graphics_handler.update_graphics(self.network)
    
    def delete_selected_clicked(self, dialog: RouterEditor):
        if not dialog.ui.link_list.currentItem():
            dialog.ui.error_label.setText("No link selected.")
            return
        
        link: Link
        link = dialog.ui.link_list.currentItem().data(Qt.UserRole)
        
        self.network.unlink(link.routerA.id, link.routerB.id)
        dialog.ui.error_label.setText(f"Link between Router {link.routerA.id} and Router {link.routerB.id} deleted.")
        
        dialog.ui.link_list.takeItem(dialog.ui.link_list.currentRow())
    
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
        self.graphics_handler.update_graphics(self.network)
    
    def link_routers_clicked(self):
        dialog = RouterLinker()
        self.display_routers()
        
        if not dialog.exec():
            return

        data = dialog.get_data()
        
        routerA_id = data["router1"]
        routerB_id = data["router2"]
        
        if self.network.link(routerA_id, routerB_id, data["cost"]):
            self.parent.ui.textBrowser.setText(f"Routers {routerA_id} and {routerB_id} linked successfully.")
        else:
            if routerA_id == routerB_id:
                self.parent.ui.textBrowser.setText("Cannot link a router to itself.")
            else:
                self.parent.ui.textBrowser.setText("Failed to link routers. They may already be linked.")
                
        self.graphics_handler.update_graphics(self.network)
        
    def save_network_clicked(self):
        folder_path = QFileDialog.getExistingDirectory(
            self.parent,
            "Select Folder to Save Network",
            ""
        )

        if not folder_path:
            return

        writer = FileWriter(folder_path, self.network.name)
        writer.write_network(self.network)

        self.parent.ui.textBrowser.setText(f"Network saved to {writer.file_path}.")
        
        self.parent.ui.textBrowser.setText(f"Network saved to {folder_path}.")
        
    def load_network_clicked(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.parent,
            "Load Network",
            "",
            "PyNet Networks (*.pynet)"
        )
        
        if file_path == "":
            return
        
        reader = FileReader(file_path)
        self.network = reader.read_network()
        self.parent.network = self.network
        
        self.parent.ui.save_network_button.setDisabled(False)
        self.parent.ui.add_router_button.setDisabled(False)
        self.parent.ui.edit_router_button.setDisabled(False)
        self.parent.ui.delete_router_button.setDisabled(False)
        self.parent.ui.link_routers_button.setDisabled(False)
        self.parent.ui.set_constraints_button.setDisabled(False)
        
        self.display_routers()
        self.graphics_handler.update_graphics(self.network)