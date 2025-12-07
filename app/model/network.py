from .router import Router
from .link import Link
from .path import Path

class Network:
    """
    Represents a network consisting of routers and links.
    
    Attributes:
        id (int): The unique identifier of the network.
        name (str): The name of the network.
        routers (set[Router]): A set of routers in the network.
        router_count (int): The count of routers in the network.
        link_count (int): The count of links in the network.
        path_count (int): The count of paths in the network.
    """
    
    def __init__(self, id: int, name: str):
        """Initializes the Network with the given ID and name.

        Args:
            id (int): The unique identifier of the network.
            name (str): The name of the network.
        """
        self.id = id
        self.name = name
        self.routers = set()
        self.router_count = 0
        self.link_count = 0
        self.path_count = 0
        
    def add_router(self, name: str, x: float, y: float, security_level: int, firewall_enabled: bool) -> Router:
        """Adds a new router to the network.

        Args:
            name (str): The name of the router.
            x (float): The x-coordinate of the router's location.
            y (float): The y-coordinate of the router's location.
            security_level (int): The security level of the router.
            firewall_enabled (bool): Indicates if the router has a firewall enabled.

        Returns:
            Router: The newly added router.
        """
        new_router = Router(
            self.router_count,
            name,
            x,
            y,
            security_level,
            firewall_enabled
        )
        
        self.routers.add(new_router)
        
        self.router_count += 1
        
        return new_router

    def remove_router(self, router: Router) -> bool:
        """Removes a router from the network.

        Args:
            router (Router): The router to be removed.
            
        Returns:
            bool: True if the router was removed, False otherwise.
        """
        
        if router in self.routers:
            for link in router.links:
                self.unlink(link.routerA.id, link.routerB.id)
                
            self.routers.remove(router)
            return True
        
        return False
        
    def get_router_by_id(self, id: int) -> Router:
        """Retrieves a router by its unique identifier.

        Args:
            id (int): The unique identifier of the router.

        Returns:
            Router: The router with the specified ID, or None if not found.
        """
        for router in self.routers:
            if router.id == id:
                return router
        return None
    
    def link(self, idA: int, idB: int, cost: float, name: str = "") -> bool:
        """Creates a link between two routers in the network.
        
        Args:
            idA (int): The unique identifier of the first router.
            idB (int): The unique identifier of the second router.
            cost (float): The cost associated with the link.
            name (str, optional): The name of the link. Defaults to "".
            
        Returns:
            bool: True if the link was created successfully, False otherwise.
        """
        if (self.get_link(idA, idB) is not None):
            return False
        
        routerA = self.get_router_by_id(idA)
        routerB = self.get_router_by_id(idB)
        
        if (routerA is None or routerB is None):
            return False
        
        if (routerA == routerB):
            return False
        
        if (name == ""):
            name = f"{routerA.name} - {routerB.name}" 
        new_link = Link(self.link_count,
                        name,
                        cost,
                        routerA,
                        routerB)
        
        routerA.add_link(new_link)
        routerB.add_link(new_link)
        
        self.link_count += 1
        return True
    
    def unlink(self, idA: int, idB: int) -> bool:
        """Removes the link between two routers in the network.
        
        Args:
            idA (int): The unique identifier of the first router.
            idB (int): The unique identifier of the second router.
            
        Returns:
            bool: True if the link was removed successfully, False otherwise.
        """
        link = self.get_link(idA, idB)
        
        if (link is None):
            return False
        
        routerA = self.get_router_by_id(idA)
        routerB = self.get_router_by_id(idB)
        
        if (routerA is None or routerB is None):
            return False
        
        routerA.remove_link(link)
        routerB.remove_link(link)
        
        return True
    
    def print_routers(self):
        """Prints all routers in the network.
        """
        for router in self.routers:
            print(router)
    
    def get_link(self, idA: int, idB: int) -> Link | None:
        """Retrieves the link between two routers by their IDs.
        
        Args:
            idA (int): The unique identifier of the first router.
            idB (int): The unique identifier of the second router.
            
        Returns:
            Link | None: The link between the two routers, or None if no link exists.
        """
        routerA = self.get_router_by_id(idA)
        routerB = self.get_router_by_id(idB)
        
        if (routerA is None or routerB is None):
            return None
        
        if (routerA == routerB):
            return None
        
        for link in routerA.links:
            if link.concerns(routerB):
                return link
        
        return None
    
    def get_network_matrix(self) -> list[list[float]]:
        """Generates a cost matrix representing the network topology.
        
        Returns:
            list[list[float]]: A 2D matrix where element [i][j] represents the cost of the link from router i to router j, or infinity if no direct link exists.
        """
        network_matrix = [[0.0 for j in range(self.router_count)]for i in range(self.router_count)]
        
        for i in range(self.router_count):
            for j in range(self.router_count):
                if (i != j):
                    link = self.get_link(i, j)
                    if (link is not None):
                        network_matrix[i][j] = link.cost
                    else:
                        network_matrix[i][j] = float('inf')
        
        return network_matrix
    
    def create_path(self, source: Router, destination: Router, security_requirement: int, firewall_required: bool, links: list[Link]) -> Path:
        """Creates a path in the network.

        Args:
            source (Router): The starting router of the path.
            destination (Router): The ending router of the path.
            security_requirement (int): The security level required for the path.
            firewall_required (bool): Indicates whether a firewall is required for the path.
            links (list[Link]): The list of links that make up the path.

        Returns:
            Path: The created path object.
        """
        self.path_count += 1
        
        return Path(
            self.path_count,
            f"Path{self.path_count}",
            source,
            destination,
            security_requirement,
            firewall_required,
            links
        )