from .router import Router
from .link import Link

class Path:
    def __init__(self,
                 id: int,
                 name: str,
                 source: Router,
                 destination: Router,
                 security_requirement: int,
                 links: list[Link] = []):
        self.id = id
        self.name = name
        self.source = source
        self.destination = destination
        self.security_requirement = security_requirement
        self.links = links
    
    def add_link(self, link: Link) -> None:
        if (link.is_valid()):
            self.links.append(link)
            
    def check_security(self) -> bool:
        for link in self.links:
            if not ((link.routerA.security_level >= self.security_requirement) or
                    (link.routerB.security_level >= self.security_requirement)):
                return False
        
        return True
    
    def is_valid(self) -> bool:
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