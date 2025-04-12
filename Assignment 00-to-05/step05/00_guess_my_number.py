import random

def main():
    # Randomly choose a number between 0 and 99
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    # Loop until the user guesses the correct number
    while True:
        # Ask the user for their guess
        guess = int(input("Enter a guess: "))

        # Check if the guess is correct
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break

# Run the game
main()
