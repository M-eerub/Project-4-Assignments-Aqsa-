# Helper function to subtract 7
def subtract_seven(num):
    return num - 7

# Main function to get input and use the helper function
def main():
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print("Result after subtracting 7:", result)

# Run the main function
main()
