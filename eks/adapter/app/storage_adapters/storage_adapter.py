from abc import ABC, abstractmethod

class StorageAdapter(ABC):
    @abstractmethod
    def get_file_content(self, file_key: str) -> str:
        pass