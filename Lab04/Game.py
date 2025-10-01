from Board import Board
class Game:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.currnet_turn = 0
    def play(self):
        players = [self.player1, self.player2]
        while not self.board.is_full():
            self.board.display()
            players[self.currnet_turn].make_move(self.board)
            if self.board.check_winner():
                self.board.display()
                print(f"\n\nPlayer {self.currnet_turn + 1} has won! \n\n")
                break
            self.switch_turns()
        if self.board.is_full():
            self.board.display()
            print("draw, nobody wins")
            
    def switch_turns(self):
        self.currnet_turn = (self.currnet_turn + 1) % 2
        