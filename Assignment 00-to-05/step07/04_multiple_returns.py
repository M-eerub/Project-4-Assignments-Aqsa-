# Function to get user data
def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    
    return first_name, last_name, email  # Returning as a tuple

# Main function to use the data
def main():
    user_info = get_user_data()
    print("Received the following user data:", user_info)

# Run the main function
main()
