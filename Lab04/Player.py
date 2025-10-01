from abc import ABC, abstractmethod
class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    @abstractmethod
    def make_move(self,board):
        pass

    