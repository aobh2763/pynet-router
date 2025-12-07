from app.model import Path
from .model_builder import ModelBuilder
from gurobipy import *

class ModelSolver():
    """
    Handles solving the optimization model to find a path.
    
    Attributes:
        model_builder (ModelBuilder): An instance of ModelBuilder used to create the model.
        model (gurobipy.Model): The constructed optimization model.
    """
    
    def __init__(self, builder: ModelBuilder):
        """Initializes the ModelSolver with a ModelBuilder instance.

        Args:
            builder (ModelBuilder): An instance of ModelBuilder used to create the model.
        """
        self.model_builder = builder
        self.model = builder.model
        
        self.model.optimize()
    
    def create_path(self) -> Path | None:
        """Creates a path from the optimized model if one exists.

        Returns:
            Path | None: The path found by the model or None if no path exists.
        """
        if self.model.Status != GRB.OPTIMAL or self.model.ObjVal == 0:
            return None

        used_edges = {}
        for var in self.model.getVars():
            if var.X > 0.5:
                a, b = var.VarName[1:].split("-")
                u, v = int(a), int(b)
                used_edges.setdefault(u, []).append(v)

        src = self.model_builder.source.id
        dst = self.model_builder.destination.id

        path_nodes = [src]
        current = src

        while current != dst:
            if current not in used_edges or not used_edges[current]:
                return None

            nxt = used_edges[current].pop(0)
            link = self.model_builder.network.get_link(current, nxt)
            if link is None:
                link = self.model_builder.network.get_link(nxt, current)
            if link is None:
                return None

            path_nodes.append(nxt)
            current = nxt

        path_links = []
        for i in range(len(path_nodes) - 1):
            u, v = path_nodes[i], path_nodes[i + 1]
            link = self.model_builder.network.get_link(u, v)
            path_links.append(link)

        return self.model_builder.network.create_path(
            self.model_builder.source,
            self.model_builder.destination,
            self.model_builder.security_requirement,
            self.model_builder.firewall_required,
            path_links
        )