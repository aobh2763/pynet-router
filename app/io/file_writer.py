from app.model import Network

import os
import pickle

class FileWriter:
    """
    Handles writing Network objects to files.
    
    Attributes:
        folder_path (str): The path to the folder where the file will be saved.
        file_name (str): The name of the file to save.
        file_path (str): The full path to the file including folder and name.
    """
    
    def __init__(self, folder_path: str, file_name: str = "network"):
        """Initializes the FileWriter with the given folder path and file name.

        Args:
            folder_path (str): The path to the folder where the file will be saved.
            file_name (str, optional): The name of the file to save. Defaults to "network".
        """
        self.folder_path = folder_path
        self.file_name = file_name
        
        os.makedirs(self.folder_path, exist_ok=True)
        self.file_path = os.path.join(self.folder_path, f"{self.file_name}.pynet")
        
    def write_network(self, data: Network):
        """Writes the network to the specified file.

        Args:
            data (Network): The network object to be written to the file.
        """
        with open(self.file_path, 'wb') as file:
            pickle.dump(data, file)