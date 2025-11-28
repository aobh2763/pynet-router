class Router:
    def __init__(self,
                 id: int,
                 name: str,
                 x: float,
                 y: float,
                 security_level: int) -> None:
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.security_level = security_level
        self.links = []
        
    def add_link(self, link: str) -> None:
        self.links.append(link)
        
    def print_router(self) -> None:
        print(f"Router ID: {self.id}, Name: {self.name}, Position: ({self.x}, {self.y}), Security Level: {self.security_level}")