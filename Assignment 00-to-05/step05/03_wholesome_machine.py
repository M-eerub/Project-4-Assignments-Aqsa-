def affirmation_check():
    correct_affirmation = "I am capable of doing anything I put my mind to."

    print("Please type the following affirmation:")
    print(correct_affirmation)
    
    # Keep asking until user types it correctly
    while True:
        user_input = input()
        if user_input == correct_affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation. Please try again:")

# Run the function
affirmation_check()
