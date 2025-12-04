from .model_builder import ModelBuilder
from gurobipy import *

class ModelSolver():
    def __init__(self, model: ModelBuilder):
        self.model_builder = model
        self.model = model.model
    
    def create_path(self):
        pass
        
    def test(self):
        self.model.optimize()
        
        for var in self.model.getVars():
            print(f"{var.varName} = {var.x}")