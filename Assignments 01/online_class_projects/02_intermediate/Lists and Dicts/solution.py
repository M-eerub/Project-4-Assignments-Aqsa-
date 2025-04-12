def access_element(lst, index):
    # Try to access the element at the given index
    if index < 0 or index >= len(lst):
        return "Index out of range."  # Return error message if the index is invalid
    else:
        return lst[index]  # Return the element at the valid index

def modify_element(lst, index, new_value):
    # Try to modify the element at the given index
    if index < 0 or index >= len(lst):
        return "Index out of range."  # Return error message if the index is invalid
    else:
        lst[index] = new_value  # Update the element at the valid index
        return lst  # Return the modified list

def slice_list(lst, start, end):
    # Try to slice the list from start to end index
    if start < 0 or end > len(lst) or start >= end:
        return "Invalid slice indices."  # Return error message if the indices are invalid
    else:
        return lst[start:end]  # Return the sliced part of the list

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list to work with
    print("Current list:", lst)
    
    # Ask the user for the operation they want to perform
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    # Handle different operations
    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))  # Call access function
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))  # Call modify function
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))  # Call slice function
    else:
        print("Invalid operation.")  # Invalid operation entered

# Run the game
index_game()
