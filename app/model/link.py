from .router import Router

class Link:
    """
    Represents a link between two routers in the network.
    
    Attributes:
        id (int): The unique identifier of the link.
        name (str): The name of the link.
        cost (float): The cost associated with the link.
        routerA (Router): One endpoint router of the link.
        routerB (Router): The other endpoint router of the link.
    """
    def __init__(self, id: int, name: str, cost: float, routerA: Router, routerB: Router):
        """Initialize a Link between two routers.

        Args:
            id (int): The unique identifier of the link.
            name (str): The name of the link.
            cost (float): The cost associated with the link.
            routerA (Router): One endpoint router of the link.
            routerB (Router): The other endpoint router of the link.
        """
        self.id = id
        self.name = name
        self.cost = cost
        self.routerA = routerA
        self.routerB = routerB
        
    def is_valid(self) -> bool:
        """Checks if the link is valid (i.e., connects two different routers).

        Returns:
            bool: True if the link is valid, False otherwise.
        """
        if (self.routerA == self.routerB):
            return False
        
        return True
    
    def concerns(self, router: Router) -> bool:
        """Checks if the link concerns the given router.

        Args:
            router (Router): The router to check.

        Returns:
            bool: True if the link concerns the router, False otherwise.
        """
        return self.routerA == router or self.routerB == router
    
    def other(self, router: Router) -> Router | None:
        """Returns the other router connected by the link.

        Args:
            router (Router): The router to find the counterpart for.

        Returns:
            Router | None: The other router connected by the link, or None if the given router is not connected by this link.
        """
        if self.routerA == router:
            return self.routerB
        elif self.routerB == router:
            return self.routerA
        else:
            return None