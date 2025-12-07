from ..router_creator import RouterCreator
from ..network_creator import NetworkCreator
from ..router_selector import RouterSelector
from ..router_editor import RouterEditor
from ..router_linker import RouterLinker
from ..constraint_setter import ConstraintSetter

from app.model import Network, Link

from app.io import FileReader, FileWriter

from app.controller import ModelBuilder, ModelSolver

from PySide6.QtWidgets import QListWidgetItem, QFileDialog, QMessageBox
from PySide6.QtCore import Qt

class MainHandlers:
    def __init__(self, parent, network: Network, graphics_handler, builder: ModelBuilder, solver: ModelSolver):
        self.parent = parent
        self.network = network
        self.graphics_handler = graphics_handler
        self.builder = builder
        self.solver = solver
    
    def display_routers(self):
        text = "Routers in the network:\n"
        
        for router in self.network.routers:
            text += f"{router}\n"
        
        self.parent.ui.textBrowser.setText(text)
        
    def new_network_clicked(self):
        if self.network is not None:
            reply = QMessageBox.question(
                self.parent,
                "Confirm",
                "Are you sure you want to create a new network?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            
            if reply == QMessageBox.No:
                return
        
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
        self.graphics_handler.update_graphics(self.network)
        
        self.parent.ui.textBrowser.setText("New network created.")
        
        self.parent.ui.save_network_button.setDisabled(False)
        self.parent.ui.add_router_button.setDisabled(False)
        self.parent.ui.edit_router_button.setDisabled(False)
        self.parent.ui.delete_router_button.setDisabled(False)
        self.parent.ui.link_routers_button.setDisabled(False)
        self.parent.ui.set_constraints_button.setDisabled(False)
        self.parent.ui.find_route_button.setDisabled(True)
        
        self.parent.ui.actionAdd_Router.setDisabled(False)
        self.parent.ui.actionEdit_Router.setDisabled(False)
        self.parent.ui.actionDelete_Router.setDisabled(False)
        self.parent.ui.actionLink_Routers.setDisabled(False)
        self.parent.ui.actionSave_Network.setDisabled(False)
        self.parent.ui.actionSet_Constraints.setDisabled(False)
        self.parent.ui.actionFind_Route.setDisabled(True)
        self.parent.ui.actionDisplay_Routers.setDisabled(False)
        self.parent.ui.actionDisplay_Latest_Path.setDisabled(False)
        self.parent.ui.actionHide_Latest_Path.setDisabled(False)
        
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
        self.parent.ui.find_route_button.setDisabled(True)
        
        self.parent.ui.actionAdd_Router.setDisabled(False)
        self.parent.ui.actionEdit_Router.setDisabled(False)
        self.parent.ui.actionDelete_Router.setDisabled(False)
        self.parent.ui.actionLink_Routers.setDisabled(False)
        self.parent.ui.actionSave_Network.setDisabled(False)
        self.parent.ui.actionSet_Constraints.setDisabled(False)
        self.parent.ui.actionDisplay_Routers.setDisabled(False)
        self.parent.ui.actionDisplay_Latest_Path.setDisabled(False)
        self.parent.ui.actionHide_Latest_Path.setDisabled(False)
        
        self.display_routers()
        self.graphics_handler.update_graphics(self.network)
    
    def display_routers_clicked(self):
        self.display_routers()
    
    def set_constraints_clicked(self):
        dialog = ConstraintSetter()
        
        if not dialog.exec():
            return
        
        data = dialog.get_data()
        
        validation_result = ""
        
        source_router = self.network.get_router_by_id(data["source"])
        destination_router = self.network.get_router_by_id(data["destination"])
        
        if source_router is None:
            validation_result += "Source router does not exist.\n"
            
        if destination_router is None:
            validation_result += "Destination router does not exist.\n"
        
        if source_router is not None and destination_router is not None:
            if data["source"] == data["destination"]:
                validation_result += "Source and destination routers must be different.\n"
            
            if not source_router.firewall_enabled and data["firewall_required"]:
                validation_result += "Source router does not have a firewall enabled.\n"
            
            if not destination_router.firewall_enabled and data["firewall_required"]:
                validation_result += "Destination router does not have a firewall enabled.\n"
                
            if source_router.security_level < data["security_requirement"]:
                validation_result += "Source router does not meet the security requirement.\n"
            
            if destination_router.security_level < data["security_requirement"]:
                validation_result += "Destination router does not meet the security requirement.\n"
        
        if validation_result != "":
            self.parent.ui.textBrowser.setText(validation_result)
            return
        
        self.builder = ModelBuilder(self.network, data["security_requirement"], data["firewall_required"])
        self.builder.set_source(data["source"])
        self.builder.set_destination(data["destination"])
        
        self.parent.ui.textBrowser.setText("Constraints set successfully.")
        self.parent.ui.find_route_button.setDisabled(False)
        self.parent.ui.actionFind_Route.setDisabled(False)
    
    def find_route_clicked(self):
        if self.builder is None:
            self.parent.ui.textBrowser.setText("No constraints set.")
            return
        
        self.builder.build_model()
        
        self.solver = ModelSolver(self.builder)
        
        path = self.solver.create_path()
        
        if path is None:
            alert = QMessageBox.information(self.parent, "Warning", "No path could be found with the given constraints.")
        else:
            self.parent.latest_path = path
            self.parent.ui.textBrowser.setText(f"Path found:\n{path}\nWith a total cost of {path.path_cost()}")
            self.graphics_handler.update_graphics(self.network, path)
            alert = QMessageBox.information(self.parent, "Success", f"Path found with a total cost of {path.path_cost()}")
    
    def display_latest_path_clicked(self):
        path = self.parent.latest_path
        
        if path is None:
            self.parent.ui.textBrowser.setText("No path has been found yet.")
            return
        
        self.parent.ui.textBrowser.setText(f"Path found:\n{path}\nWith a total cost of {path.path_cost()}")
        self.graphics_handler.update_graphics(self.network, path)
    
    def hide_latest_path_clicked(self):
        self.graphics_handler.update_graphics(self.network, None)