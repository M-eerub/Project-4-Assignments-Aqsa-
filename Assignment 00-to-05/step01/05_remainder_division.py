# User se pehla number lena
num1 = int(input("Please enter an integer to be divided: "))

# User se doosra number lena
num2 = int(input("Please enter an integer to divide by: "))

# Division aur remainder calculate karna
quotient = num1 // num2   # Yeh divide karke sirf whole number deta hai
remainder = num1 % num2   # Yeh remainder deta hai

# Result print karna
print(f"The result of this division is {quotient} with a remainder of {remainder}")
