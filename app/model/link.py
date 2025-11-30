from .router import Router

class Link:
    def __init__(self,
                 id: int,
                 name: str,
                 cost: float,
                 routerA: Router,
                 routerB: Router):
        self.id = id
        self.name = name
        self.cost = cost
        self.routerA = routerA
        self.routerB = routerB
        
    def is_valid(self) -> bool:
        if (self.routerA == self.routerB):
            return False
        
        return True
    
    def concerns(self, router: Router) -> bool:
        return self.routerA == router or self.routerB == router
    
    def other(self, router: Router) -> Router | None:
        if self.routerA == router:
            return self.routerB
        elif self.routerB == router:
            return self.routerA
        else:
            return None