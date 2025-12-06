from app.model import Network

import pickle

class FileReader:
    """
    Handles reading Network objects from files.
    
    Attributes:
        file_path (str): The path to the file to be read.
    """
    
    def __init__(self, file_path: str):
        """Initializes the FileReader with the given file path.

        Args:
            file_path (str): The path to the file to be read.
        """
        self.file_path = file_path
        
        try:
            with open(self.file_path, 'rb'):
                pass
        except FileNotFoundError:
            raise print(f"File not found: {self.file_path}")
        
    def read_network(self) -> Network:
        """Reads the network from the specified file.
        
        Returns:
            Network: The network object read from the file.
        """
        with open(self.file_path, 'rb') as file:
            return pickle.load(file)