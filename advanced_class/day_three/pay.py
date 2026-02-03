from abc import ABC, abstractmethod

class Pay(ABC):

    @abstractmethod
    def other(self, amount) :
        pass