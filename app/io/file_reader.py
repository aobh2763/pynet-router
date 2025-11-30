from app.model import Network

import pickle

class FileReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        
        try:
            with open(self.file_path, 'rb'):
                pass
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        
    def read_network(self) -> Network:
        with open(self.file_path, 'rb') as file:
            return pickle.load(file)