import random

# Get user input
player_choice = input("Enter rock, paper or scissors: ").lower()

# Define computer choice
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

# Game logic
if player_choice == computer_choice:
    print("It's a tie!")
    
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock crushes scissors.")
    
elif player_choice == "paper" and computer_choice == "rock":
    print("You win! Paper covers rock.")
    
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors cut paper.")
    
else:
    print(f"You lose! The computer chose {computer_choice}.")
