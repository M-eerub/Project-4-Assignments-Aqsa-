# Initialize an empty list to store values
user_list = []

# Continuously ask the user to enter values
while True:
    value = input("Enter a value: ")
    
    # If the user presses enter without typing anything, break the loop
    if value == "":
        break
    
    # Add the entered value to the list
    user_list.append(value)

# Print the list after the user stops entering values
print("Here's the list:", user_list)
