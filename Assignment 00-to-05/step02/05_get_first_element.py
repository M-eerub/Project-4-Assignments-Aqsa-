# Function to get the first element of the list
def get_first_element(lst):
    print(lst[0])  # Print the first element of the list

# User se list input lena
user_list = []
n = int(input("How many elements in your list? "))  # List ke size ka input lena
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Function call to print the first element
get_first_element(user_list)
