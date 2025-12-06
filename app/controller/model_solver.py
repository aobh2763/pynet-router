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
    
    def create_path(self) -> Path | None:
        """Creates a path from the optimized model if one exists.

        Returns:
            Path | None: The path found by the model or None if no path exists.
        """
        if self.model.Status != GRB.OPTIMAL or self.model.ObjVal == 0:
            return None

        adj = {}
        edges = []

        for var in self.model.getVars():
            if var.X == 1.0:
                a, b = var.VarName.split("-")
                u = int(a[1:])
                v = int(b)

                adj.setdefault(u, set()).add(v)
                adj.setdefault(v, set()).add(u)

                edges.append((u, v))

        src = self.model_builder.source.id
        dst = self.model_builder.destination.id

        if src not in adj or dst not in adj:
            return None

        path_links = []
        visited = set([src])
        current = src

        while current != dst:
            neighbors = adj.get(current, set())
            next_nodes = [n for n in neighbors if n not in visited]

            if not next_nodes:
                return None

            nxt = next_nodes[0]
            
            link = self.model_builder.network.get_link(current, nxt)
            if link is None:
                link = self.model_builder.network.get_link(nxt, current)

            path_links.append(link)
            visited.add(nxt)
            current = nxt
            
        path = self.model_builder.network.create_path(
            self.model_builder.source,
            self.model_builder.destination,
            self.model_builder.security_requirement,
            self.model_builder.firewall_required,
            path_links
        )
        
        return path