from .router import Router
from .link import Link
from .path import Path

class Network:
    def __init__(self,
                 id: int,
                 name: str):
        self.id = id
        self.name = name
        self.routers = set()
        self.router_count = 0
        self.link_count = 0
        self.path_count = 0
        
    def add_router(self, name, x, y, security_level) -> Router:
        new_router = Router(
            self.router_count,
            name,
            x,
            y,
            security_level
        )
        
        self.routers.add(new_router)
        
        self.router_count += 1
        
        return new_router
        
    def get_router_by_id(self, id: int) -> Router:
        for router in self.routers:
            if router.id == id:
                return router
        return None
    
    def link(self,
             idA: int,
             idB: int,
             cost: float,
             name: str = "") -> bool:
        routerA = self.get_router_by_id(idA)
        routerB = self.get_router_by_id(idB)
        
        if (routerA is None or routerB is None):
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
    
    def print_routers(self) -> None:
        for router in self.routers:
            router.print_router()
    
    def get_link(self,
                 idA: int,
                 idB: int) -> Link | None:
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
    
    def get_network_matrix(self) -> list[list[int]]:
        network_matrix = [[0 for j in range(self.router_count)]for i in range(self.router_count)]
        
        for i in range(self.router_count):
            for j in range(self.router_count):
                if (i != j):
                    link = self.get_link(i, j)
                    if (link is not None):
                        network_matrix[i][j] = link.cost
                    else:
                        network_matrix[i][j] = float('inf')
                else:
                    network_matrix[i][j] = 0
        
        return network_matrix
    
    def create_path(self,
                    router_ids: list[int],
                    security_requirement: int) -> Path | None:
        if (len(router_ids) == 0):
            return None
        
        if (len(router_ids) == 1):
            router = self.get_router_by_id(router_ids[0])
            if (router is None):
                return None
            return Path(self.path_count,
                        f"Path from {router.name} to {router.name}",
                        router,
                        router,
                        security_requirement)
        
        source = self.get_router_by_id(router_ids[0])
        destination = self.get_router_by_id(router_ids[-1])
        
        if (source is None or destination is None):
            return None
        
        path_links = []
        for i in range(len(router_ids) - 1):
            link = self.get_link(router_ids[i], router_ids[i + 1])
            if (link is None):
                return None
            path_links.append(link)
        
        new_path = Path(self.path_count,
                        f"Path from {source.name} to {destination.name}",
                        source,
                        destination,
                        security_requirement,
                        path_links)
        
        self.path_count += 1
        return new_path