def main():
    # User se number lo
    user_input = int(input("Enter a number: "))
    
    # Pehla doubling yahin se shuru hoga
    curr_value = user_input * 2

    # Jab tak curr_value 100 se chhota hai, tab tak double karte raho
    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value = curr_value * 2

    # Jab 100 ya usse zyada ho jaye, final value bhi print karo
    print(curr_value)

# Call the main function
main()
