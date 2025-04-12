def sum_of_numbers(numbers):
    total = 0  # Shuruaat me total 0 hai
    for num in numbers:
        total += num  # Har number ko total me jodte hain
    return total

# Example usage:
my_list = [2, 4, 6, 8]
result = sum_of_numbers(my_list)
print("The sum is:", result)
