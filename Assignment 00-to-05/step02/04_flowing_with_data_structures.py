# Function to add three copies of data to the list
def add_three_copies(my_list, data):
    my_list.append(data)  # Adding the first copy
    my_list.append(data)  # Adding the second copy
    my_list.append(data)  # Adding the third copy

# User se input lena
message = input("Enter a message to copy: ")

# List banani aur before print karna
my_list = []
print("List before:", my_list)

# Function call to add three copies of the message
add_three_copies(my_list, message)

# List after function call
print("List after:", my_list)
