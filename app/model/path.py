from .router import Router
from .link import Link

class Path:
    """
    Represents a path in the network.
    
    Attributes:
        id (int): The unique identifier of the path.
        name (str): The name of the path.
        source (Router): The source router of the path.
        destination (Router): The destination router of the path.
        security_requirement (int): The minimum security level required for the path.
        firewall_required (bool): Indicates if a firewall is required for the path.
        links (list[Link]): The list of links that make up the path.
    """
    def __init__(self, id: int, name: str, source: Router, destination: Router, security_requirement: int, firewall_required: bool, links: list[Link]):
        """Initializes the Path with the given parameters.
        
        Args:
            id (int): The unique identifier of the path.
            name (str): The name of the path.
            source (Router): The source router of the path.
            destination (Router): The destination router of the path.
            security_requirement (int): The minimum security level required for the path.
            firewall_required (bool): Indicates if a firewall is required for the path.
            links (list[Link]): The list of links that make up the path.
        """
        self.id = id
        self.name = name
        self.source = source
        self.destination = destination
        self.security_requirement = security_requirement
        self.firewall_required = firewall_required
        self.links = links
    
    def add_link(self, link: Link):
        """Adds a link to the path if it is valid.
        
        Args:
            link (Link): The link to add to the path.
        """
        if (link.is_valid()):
            self.links.append(link)
            
    def check_security(self) -> bool:
        """Checks if the path meets the security requirements.

        Returns:
            bool: True if the path meets the security requirements, False otherwise.
        """
        for link in self.links:
            if not ((link.routerA.security_level >= self.security_requirement) or
                    (link.routerB.security_level >= self.security_requirement)):
                return False
        
        return True
    
    def is_valid(self) -> bool:
        """Checks if the path is valid.

        Returns:
            bool: True if the path is valid, False otherwise.
        """
        # Case of one router path
        if (len(self.links) == 0):
            if (self.source != self.destination):
                return False
            else:
                return True
        
        # The first link must concern the source
        if (not (self.links[0]).concerns(self.source)):
            return False
        
        # Two consecutive links must share a router
        for i in range(len(self.links) - 1):
            if not ((self.links[i + 1]).concerns((self.links[i]).routerA) or 
                    (self.links[i + 1]).concerns((self.links[i]).routerB)):
                return False
        
        # The last link must concern the destination
        if (not (self.links[-1]).concerns(self.destination)):
            return False

        return True

    def __str__(self) -> str:
        """Returns a string representation of the path.

        Returns:
            str: A string describing the path.
        """
        if (self.is_valid() == False):
            return f"Path ID: {self.id} is invalid."
        
        routers = [self.source.name]
        current = self.source
        for link in self.links:
            next_router = link.routerA if link.routerB == current else link.routerB
            routers.append(next_router.name)
            current = next_router

        links_str = " -> ".join(routers)
        return (f"Path ID: {self.id}, Name: {self.name}, Source: {self.source.name}, "
                f"Destination: {self.destination.name}, Security Requirement: {self.security_requirement}, Firewall Required: {self.firewall_required}, "
                f"Links: [{links_str}]")
        
    def path_cost(self) -> float:
        """Calculates the total cost of the path.
        
        Returns:
            float: The total cost of the path.
        """
        total_cost = 0.0
        for link in self.links:
            total_cost += link.cost
        return total_cost