import random

# Constants
NUM_ROUNDS = 5  # Set how many rounds you want to play

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # Keep track of the score
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num}")
        
        # Generate random numbers for the player and the computer
        your_number = random.randint(1, 100)
        computers_number = random.randint(1, 100)
        
        # Display the player's number
        print(f"Your number is {your_number}")
        
        # Ask for the player's guess (higher or lower)
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        # Check if the input is valid
        while guess not in ['higher', 'lower']:
            guess = input("Please enter either 'higher' or 'lower': ").lower()
        
        # Check if the guess is correct
        if (guess == 'higher' and your_number > computers_number) or (guess == 'lower' and your_number < computers_number):
            print(f"You were right! The computer's number was {computers_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computers_number}")
        
        # Show the current score
        print(f"Your score is now {score}")
    
    # At the end of all rounds, print a message based on the score
    print("\nThanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Call the main function to start the game
main()
