from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass
    

class File(ABC):
    @abstractmethod
    def parse(self, content):
        pass

    