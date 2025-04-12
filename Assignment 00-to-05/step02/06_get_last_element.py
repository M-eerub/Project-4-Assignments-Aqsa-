# Function to get the last element of the list
def get_last_element(lst):
    print(lst[-1])  # Print the last element of the list using negative index

# User se list input lena
user_list = []
n = int(input("How many elements in your list? "))  # List ke size ka input lena
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

# Function call to print the last element
get_last_element(user_list)
