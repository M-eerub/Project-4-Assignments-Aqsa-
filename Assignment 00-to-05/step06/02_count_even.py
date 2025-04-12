def count_even(lst):
    # Step 1: List ko input se fill karna
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        lst.append(int(user_input))

    # Step 2: Even numbers count karna
    even_count = 0
    for number in lst:
        if number % 2 == 0:
            even_count += 1

    # Step 3: Result print karna
    print("Number of even numbers:", even_count)

# Function call
my_list = []
count_even(my_list)
