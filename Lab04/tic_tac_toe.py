from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer
from Strategy import Strategy
from Game import Game

p1_symbol = "X"
p2_symbol = "O"

print("Player1: ")
print("\t1. AI")
print("\t2. Human\n")
choice1 = input("Enter first player (1/2): ")

print("Player2: ")
print("\t1. AI")
print("\t2. Human\n")
choice2 = input("Enter second player (1/2): ")

if choice1 == "1":
    p1 = ComputerPlayer("AI-1", p1_symbol, Strategy())
else:
    name1 = input("Enter Your name: ")
    p1 = HumanPlayer(name1, p1_symbol)

if choice2 == "1":
    p2 = ComputerPlayer("AI-2", p2_symbol, Strategy())
else:
    name2 = input("Enter Your name: ")
    p2 = HumanPlayer(name2, p2_symbol)


game = Game(p1,p2)
print("Are you ready? Lets Go!!! \n\n")
game.play()
