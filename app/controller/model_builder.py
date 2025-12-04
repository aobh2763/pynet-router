from app.model import Router, Link, Network
from gurobipy import *

# MAKE SURE SOURCE AND DESTINATION FIT THE SECURITY CONSTRAINTS

# MINIMIZE : sum of COST * LINK

# POUR SOURCE :  xsj - xis = 1
# POUR A : xai - xja = 0 (ONLY CONSIDER ROUTERS THAT FIT SECURITY CONSTRAINTS)
# POUR DESTINATION : xid - xdj = -1

class ModelBuilder():
    def __init__(self,
                 network: Network,
                 security_requirement: int,
                 firewall_required: bool):
        self.network = network
        self.security_requirement = security_requirement
        self.firewall_required = firewall_required
        self.source = None
        self.destination = None
        self.model = Model("Routing")
    
    def set_source(self, source_id: int) -> bool:
        router = self.network.get_router_by_id(source_id)
        
        if (router is None):
            return False
        
        if (router.security_level < self.security_requirement):
            return False
        
        if (self.firewall_required and not router.firewall_enabled):
            return False
        
        self.source = router
        return True
    
    def set_destination(self, destination_id: int) -> bool:
        router = self.network.get_router_by_id(destination_id)
        
        if (router is None):
            return False
        
        if (router.security_level < self.security_requirement):
            return False
        
        if (self.firewall_required and not router.firewall_enabled):
            return False
        
        self.destination = router
        return True
    
    def is_routable(self, router: Router) -> bool:
        if (router.security_level < self.security_requirement):
            return False
        
        if (self.firewall_required and not router.firewall_enabled):
            return False
        
        return True
    
    def build_model(self) -> Model:
        router: Router
        link: Link
        vars = {}
        obj_fun = 0
        
        # Creating the variables
        for router in self.network.routers:
            if (not self.is_routable(router)):
                continue
            
            for link in router.links:
                other = link.other(router)
                
                if (not self.is_routable(other)):
                    continue
                
                vars[(router.id, other.id)] = self.model.addVar(vtype = GRB.BINARY, name = f"l{router.id}{other.id}")
        
        # Creating the objective function
        for router in self.network.routers:
            if (not self.is_routable(router)):
                continue
            
            for link in router.links:
                other = link.other(router)
                
                if (not self.is_routable(other)):
                    continue
                
                obj_fun += link.cost * vars[(router.id, other.id)]
        
        self.model.setObjective(obj_fun, GRB.MINIMIZE)
        
        # Creating the constraints
        for router in self.network.routers:
            links = []
            
            if (not self.is_routable(router)):
                continue
            
            formula = 0
            result = 0
            
            for link in router.links:
                other = link.other(router)
                
                if (not self.is_routable(other)):
                    continue
                
                formula += vars[(router.id, other.id)] - vars[(other.id, router.id)]
                
            match router:
                case self.source:
                    result = 1
                case self.destination:
                    result = -1
                case _:
                    result = 0
                    
            self.model.addConstr(formula == result, f"Router {router.id} flow")
        
        return self.model