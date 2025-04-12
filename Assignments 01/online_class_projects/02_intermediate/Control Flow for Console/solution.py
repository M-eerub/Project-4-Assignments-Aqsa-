import random

NUM_ROUNDS = 5  # Number of rounds to play

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Initialize the score
    your_score = 0

    # Play multiple rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers for the player and the computer
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        print("Your number is", your_number)

        # Get the user's guess
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        # Make sure the user enters a valid input
        while guess not in ["higher", "lower"]:
            guess = input("Please enter 'higher' or 'lower': ").lower()

        # Check if the guess is correct
        if (guess == "higher" and your_number > computer_number) or (guess == "lower" and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            your_score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        # Display the current score
        print("Your score is now", your_score)
        print()

    # Final message based on the score
    print("Thanks for playing!")
    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Start the game
if __name__ == "__main__":
    main()
