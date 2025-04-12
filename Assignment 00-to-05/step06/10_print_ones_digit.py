def print_ones_digit(num):
    # Use modulo operator to get the ones digit
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the function to print the ones digit
    print_ones_digit(num)

# Run the program
if __name__ == "__main__":
    main()
