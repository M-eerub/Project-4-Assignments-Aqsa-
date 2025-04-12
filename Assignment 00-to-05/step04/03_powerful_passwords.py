from hashlib import sha256  # Import SHA256 hash function from hashlib

# Function to check login by comparing password hash
def login(email, stored_logins, password_to_check):
    """
    Checks if the hashed version of the entered password matches
    the stored hashed password for the given email.
    """

    # Hash the password we want to check
    hashed_password = hash_password(password_to_check)

    # Compare it with the stored hashed password for this email
    if stored_logins[email] == hashed_password:
        return True
    else:
        return False

# This function hashes a password using SHA256
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Main part of the program
def main():
    # Dictionary storing emails and their hashed passwords
    stored_logins = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("karel"),
        "student@stanford.edu": hash_password("123!456?789")
    }

    # Test logins:
    print(login("example@gmail.com", stored_logins, "word"))           # ❌ Wrong password
    print(login("example@gmail.com", stored_logins, "password"))       # ✅ Correct password

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))     # ❌ Case sensitive
    print(login("code_in_placer@cip.org", stored_logins, "karel"))     # ✅ Correct password

    print(login("student@stanford.edu", stored_logins, "password"))    # ❌ Wrong password
    print(login("student@stanford.edu", stored_logins, "123!456?789")) # ✅ Correct password

# Run the program
if __name__ == '__main__':
    main()
