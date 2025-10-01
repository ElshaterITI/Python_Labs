from Player import Player

class HumanPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def make_move(self, board):
        try:
            i, j = input("Enter the coordinates of your symbol to be in (comma-separated) e.g. 1,2 : ").split(",")
            i, j = int(i.strip()), int(j.strip())
        except ValueError:
            print("Invalid input format, try again")
            return self.make_move(board)

        # STATUS
        # -1 invalid input
        # 0 occupied cell
        # 1 success
        status = board.update((i, j), self.symbol)
        if status == -1:
            print("Invalid input, try again")
            return self.make_move(board)
        elif status == 0:
            print("The cell is occupied, try again")
            return self.make_move(board)
        else:
            return








