# Function jo do numbers ka average nikalta hai
def find_average(num1, num2):
    average = (num1 + num2) / 2
    return average

# Example use
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Function ko call karke result print karo
result = find_average(a, b)
print("The average is:", result)
