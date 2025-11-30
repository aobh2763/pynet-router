from app.model import Network

import os
import pickle

class FileWriter:
    def __init__(self, folder_path: str, file_name: str = "network"):
        self.folder_path = folder_path
        self.file_name = file_name
        
        os.makedirs(self.folder_path, exist_ok=True)
        self.file_path = os.path.join(self.folder_path, f"{self.file_name}.pynet")
        
    def write_network(self, data: Network):
        with open(self.file_path, 'wb') as file:
            pickle.dump(data, file)