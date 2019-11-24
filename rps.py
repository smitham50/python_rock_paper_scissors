import random

print('...rock...')
print('...paper...')
print('...scissors...')

player1 = input("Enter Player 1's choice: ")

choices = ["rock", "paper", "scissors"]

move = random.choice(choices)

print(f"The computer played: {move}")


if player1 == move:
    print("Draw!")
elif player1 == "rock" and move == "scissors":
    print("Player 1 Wins!")
elif player1 == "paper" and move == "rock":
    print("Player 1 Wins!")
elif player1 == "scissors" and move == "paper":
    print("Player 1 Wins!")
else:
    print("The computer Wins!")