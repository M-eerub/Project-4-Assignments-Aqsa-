def print_multiple(message, repeats):
    # Print the message 'repeats' number of times
    for _ in range(repeats):
        print(message)

def main():
    # Ask the user for the message
    message = input("Please type a message: ")
    # Ask the user for the number of repeats
    repeats = int(input("Enter a number of times to repeat your message: "))
    # Call the function to print the message the specified number of times
    print_multiple(message, repeats)

# Run the program
if __name__ == "__main__":
    main()
