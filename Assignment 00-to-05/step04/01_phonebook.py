def main():
    # Empty phonebook dictionary to store contacts
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. Find a contact")
        print("3. Show all contacts")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            # Add a contact
            name = input("Enter contact name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Added {name} with number {number}.")

        elif choice == "2":
            # Find a contact
            search_name = input("Enter the name to search: ")
            if search_name in phonebook:
                print(f"{search_name}'s number is {phonebook[search_name]}")
            else:
                print(f"{search_name} not found in phonebook.")

        elif choice == "3":
            # Show all contacts
            if phonebook:
                print("\nAll Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty.")

        elif choice == "4":
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 4.")

# Run the main function
main()

