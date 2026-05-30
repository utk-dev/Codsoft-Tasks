#Stone-Paper-Scissor Game

'''
Rock = -1
Paper = 1
Scissors = 0
'''

import random

while True:
    computer = random.choice([1,0,-1])

    print(f"r for 🪨\np for 📄\ns for ✂️\nType stop for ending the game")

    your_move = input("Enter your choice: ").lower()

    if your_move == "stop":
        print("GAME ENDED")
        break

    yourDict = {"r":-1, "p":1, "s":0}

    you = yourDict[your_move]

    reverseDict = {-1:"Rock", 1:"Paper", 0:"Scissors"}

    print(f"Computer chose: {reverseDict[computer]} \nYou chose: {reverseDict[you]}")

    if you == computer:
        print("It's a Tie !!")
        if (you-computer == -1) or (computer-you == 2):
            print("Computer Wins!!")
        else:
            print("You win!!")
