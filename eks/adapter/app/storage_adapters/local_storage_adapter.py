import os
from .storage_adapter import StorageAdapter

class LocalStorageAdapter(StorageAdapter):
    def __init__(self, base_path="./data"):
        self.base_path = base_path

    def get_file_content(self, file_key: str) -> str:
        full_path = os.path.join(self.base_path, file_key)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Archivo {full_path} no existe localmente.")
        
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        return content