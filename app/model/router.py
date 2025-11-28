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
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Router):
            return NotImplemented

        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
        
    def add_link(self, link) -> None:
        self.links.append(link)
        
    def __str__(self) -> str:
        return f"Router ID: {self.id}, Name: {self.name}, Position: ({self.x}, {self.y}), Security Level: {self.security_level}"