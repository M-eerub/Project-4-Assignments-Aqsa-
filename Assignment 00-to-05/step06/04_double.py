def double(num):
    # Multiply the number by 2 and return it
    return num * 2

def main():
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = double(number)
    print("Double that is", result)

# Call the main function
main()
