from Player import Player

class ComputerPlayer(Player):
    def __init__(self, name, symbol, strategy):
        super().__init__(name, symbol)
        self.strategy = strategy

    def make_move(self, board):
        i, j = self.strategy.get_move(board, self.symbol)

        # STATUS
        # -1 invalid input
        # 0 occupied cell
        # 1 success
        status = board.update((i, j), self.symbol)

        if status == -1:
            return self.make_move(board)
        elif status == 0:
            return self.make_move(board)
        else:
            return
