# Helper function to greet the user
def greet(name):
    print("Greetings " + name + "!")

# Main function
def main():
    # Ask the user for their name
    name = input("What's your name? ")
    
    # Call the greet function with the user's name
    greet(name)

# Run the program
if __name__ == "__main__":
    main()
