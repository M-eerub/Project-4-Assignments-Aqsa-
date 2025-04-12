
def tall_enough_loop():
    while True:
        height_input = input("How tall are you? (Press Enter to quit): ")

        # If user presses enter without typing anything
        if height_input == "":
            print("Goodbye!")
            break
        
        # Convert input to number
        height = int(height_input)

        if height >= 50:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# Call the function
tall_enough_loop()
