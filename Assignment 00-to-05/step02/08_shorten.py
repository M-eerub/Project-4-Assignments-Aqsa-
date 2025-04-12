# Define the MAX_LENGTH constant
MAX_LENGTH = 3

# Function to shorten the list to MAX_LENGTH by removing elements from the end
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        # Remove the last element and print it
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")
    
# Main function to test the shorten function
def main():
    # Example list
    lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    # Print original list
    print("Original list:", lst)
    
    # Call the shorten function
    shorten(lst)
    
    # Print the shortened list
    print("Shortened list:", lst)

# Call the main function to run the program
main()
