from app.model import Router, Link, Network
from gurobipy import *

# MAKE SURE SOURCE AND DESTINATION FIT THE SECURITY CONSTRAINTS

# MINIMIZE : sum of COST * LINK

# POUR SOURCE :  xsj - xis = 1
# POUR A : xai - xja = 0 (ONLY CONSIDER ROUTERS THAT FIT SECURITY CONSTRAINTS)
# POUR DESTINATION : xid - xdj = -1

class ModelBuilder():
    """
    Builds an optimization model for routing in a network.
    
    Attributes:
        network (Network): The network containing routers and links.
        security_requirement (int): The minimum security level required for routers.
        firewall_required (bool): Indicates if a firewall is required for the routers.
        source (Router | None): The source router for the routing.
        destination (Router | None): The destination router for the routing.
        model (gurobipy.Model): The constructed optimization model.
    """
    
    def __init__(self, network: Network, security_requirement: int, firewall_required: bool):
        """Initializes the ModelBuilder with the given network and requirements.

        Args:
            network (Network): The network containing routers and links.
            security_requirement (int): The minimum security level required for routers.
            firewall_required (bool): Indicates if a firewall is required for the routers.
        """
        self.network = network
        self.security_requirement = security_requirement
        self.firewall_required = firewall_required
        self.source = None
        self.destination = None
        self.model = None
    
    def set_source(self, source_id: int) -> bool:
        """Sets the source router if it meets the security and firewall requirements.

        Args:
            source_id (int): The ID of the source router.

        Returns:
            bool: True if the source router is set successfully, False otherwise.
        """
        router = self.network.get_router_by_id(source_id)
        
        if (router is None):
            return False
        
        if (self.is_routable(router) == False):
            return False
        
        self.source = router
        return True
    
    def set_destination(self, destination_id: int) -> bool:
        """Sets the destination router if it meets the security and firewall requirements.

        Args:
            destination_id (int): The ID of the destination router.

        Returns:
            bool: True if the destination router is set successfully, False otherwise.
        """
        router = self.network.get_router_by_id(destination_id)
        
        if (router is None):
            return False
        
        if (self.is_routable(router) == False):
            return False
        
        self.destination = router
        return True
    
    def is_routable(self, router: Router) -> bool:
        """Checks if a router meets the security and firewall requirements.

        Args:
            router (Router): The router to check.

        Returns:
            bool: True if the router meets the requirements, False otherwise.
        """
        if (router.security_level < self.security_requirement):
            return False
        
        if (self.firewall_required and not router.firewall_enabled):
            return False
        
        return True
    
    def build_model(self):
        """Builds the optimization model for routing.

        Returns:
            gurobipy.Model: The constructed optimization model.
        """
        router: Router
        link: Link
        vars = {}
        obj_fun = 0
        
        # Reset model
        self.model = Model("Routing")
        
        # Creating the variables
        for router in self.network.routers:
            if (not self.is_routable(router)):
                continue
            
            for link in router.links:
                other = link.other(router)
                
                if (not self.is_routable(other)):
                    continue
                
                vars[(router.id, other.id)] = self.model.addVar(vtype = GRB.BINARY, name = f"l{router.id}-{other.id}")
        
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