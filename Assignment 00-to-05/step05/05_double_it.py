# User se number input lo
curr_value = int(input("Enter a number: "))

# Jab tak curr_value 100 se chhota hai, tab tak loop chale
while curr_value < 100:
    # curr_value ko double karo
    curr_value = curr_value * 2
    # naya value print karo
    print(curr_value, end=" ")
