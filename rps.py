import random

print('...rock...')
print('...paper...')
print('...scissors...')

player_score = 0
computer_score = 0

game_over = False

#computer choices
choices = ["rock", "paper", "scissors"]

#player move
player = input("Enter your choice: ")

print("")

#computer move
computer = random.choice(choices)
print(f"The computer played: {computer}")

while not game_over:
    if player == computer:
        print("Draw!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You win!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_score += 1
    else:
        print("The computer wins!")
        computer_score += 1
    print(f"Your score is: {player_score} || The computer's score is: {computer_score}")
    if player_score == 3 or computer_score == 3:
        if player_score == 3:
            print("You win!\n")
        else:
            print("You lose!\n")
        game_over = True
    else:
        print('...rock...')
        print('...paper...')
        print('...scissors...\n')
        player = input("Enter your choice: ")
        print("")
        computer = random.choice(choices)
        print(f"The computer played: {computer}\n")


