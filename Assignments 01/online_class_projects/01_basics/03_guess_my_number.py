import random

def main():
    # Random number choose karo between 0 to 99
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    while True:
        guess = int(input("Enter a guess: "))
        
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print("Congrats! The number was:", secret_number)
            break  # loop se bahar nikal jao jab guess sahi ho

# Run the game
main()
