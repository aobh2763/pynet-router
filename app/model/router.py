class Router:
    """
    A class representing a network router.
    
    Attributes:
        id (int): The unique identifier for the router.
        name (str): The name of the router.
        x (float): The x-coordinate of the router's position.
        y (float): The y-coordinate of the router's position.
        security_level (int): The security level of the router.
        firewall_enabled (bool): Indicates if the firewall is enabled.
        links (list): A list of links connected to the router.
    """
    
    def __init__(self, id: int, name: str, x: float, y: float, security_level: int, firewall_enabled: bool):
        """Initializes a Router instance.

        Args:
            id (int): The unique identifier for the router.
            name (str): The name of the router.
            x (float): The x-coordinate of the router's position.
            y (float): The y-coordinate of the router's position.
            security_level (int): The security level of the router.
            firewall_enabled (bool): Indicates if the firewall is enabled.
        """
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.security_level = security_level
        self.firewall_enabled = firewall_enabled
        self.links = []
        
    def __eq__(self, other: object) -> bool:
        """Checks equality between two Router instances based on their IDs.
        
        Args:
            other (object): The other Router instance to compare.
            
        Returns:
            bool: True if both routers have the same ID, False otherwise.
        """
        if not isinstance(other, Router):
            return NotImplemented

        return self.id == other.id

    def __hash__(self) -> int:
        """Returns the hash of the Router instance based on its ID.
        
        Returns:
            int: The hash value of the router.
        """
        return hash(self.id)
        
    def add_link(self, link):
        """Adds a link to the router's list of links.
        
        Args:
            link: The link to be added.
        """
        self.links.append(link)
        
    def __str__(self) -> str:
        """Returns a string representation of the router.
        
        Returns:
            str: A string describing the router.
        """
        return f"Router ID: {self.id}, Name: {self.name}, Position: ({self.x}, {self.y}), Security Level: {self.security_level}, Firewall Enabled: {self.firewall_enabled}"