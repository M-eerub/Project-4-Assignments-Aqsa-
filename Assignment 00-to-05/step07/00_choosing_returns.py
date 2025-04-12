# Adult age constant (United States)
ADULT_AGE = 18

# Function to check if the person is an adult
def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Ask user for the age
    age = int(input("How old is this person?: "))
    
    # Call the function and print the result
    print(is_adult(age))

# Run the program
if __name__ == "__main__":
    main()
