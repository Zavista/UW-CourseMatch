from abc import ABC, abstractmethod

class PipeStep(ABC):
    
    @abstractmethod
    def process(self, data):
        pass