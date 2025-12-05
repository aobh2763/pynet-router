from app.model import Link, Path
from .model_builder import ModelBuilder
from gurobipy import *

class ModelSolver():
    def __init__(self, builder: ModelBuilder):
        self.model_builder = builder
        self.model = builder.model
    
    def create_path(self):
        vars = self.model.getVars()
        links = []
        
        for var in vars:
            if (var.X == 1.0):
                id_A = int(var.varName.split("-")[0][1:])
                id_B = int(var.varName.split("-")[1])
                link = self.model_builder.network.get_link(id_A, id_B)
                
                if link is not None:
                    links.append(link)
        
        return Path(0, "Path", self.model_builder.source, self.model_builder.destination, self.model_builder.security_requirement, self.model_builder.firewall_required, links)
        
    def test(self):
        self.model.optimize()
        
        for var in self.model.getVars():
            print(f"{var.varName} = {var.x}")