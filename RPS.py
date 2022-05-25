import random

items = ["Rock", "Paper", "Scissors"]

print("++++++++++++++++++++++++++++++++++")
print("        ROCK PAPER SCISSORS       ")
print("++++++++++++++++++++++++++++++++++")
print("1) Rock")
print("2) Paper")
print("3) Scissors")
print("Enter a number:")
x = int(input())
r = random.randrange(0,3)

player = items[x - 1]
computer = items[r]

print("Player = " + player)
print("Computer = " + computer)

if player == "Rock" and computer == "Paper":
    print("Player loses: Paper covers rock")
elif player == "Rock" and computer == "Scissors":
    print("Player wins: Rock gfg
elif player == "Paper" and computer == "Rock":
    print("Player wins: Paper covers rock")
elif player == "Paper" and computer == "Scissors":
    print("Player loses: Scissors cut paper")
elif player == "Scissors" and computer == "Rock":
    print("Player loses: Rock crushes Scissors")    
elif player == "Scissors" and computer == "Paper":
    print("Player wins: Scissors cut paper")
else:
    print("Game is a tie!")
     