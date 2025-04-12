# Fruit prices stored in a dictionary (fruit name -> price per fruit)
fruit_prices = {
    "apple": 10.0,
    "durian": 25.5,
    "jackfruit": 30.0,
    "kiwi": 15.0,
    "rambutan": 9.5,
    "mango": 12.0
}

total_cost = 0  # Start with zero total

# Loop through each fruit in the dictionary
for fruit in fruit_prices:
    # Ask user how many of this fruit they want
    quantity = input(f"How many ({fruit}) do you want?: ")

    # Convert user input from string to integer
    quantity = int(quantity)

    # Add the cost for this fruit to the total
    total_cost += fruit_prices[fruit] * quantity

# After loop, print the total cost
print(f"Your total is ${total_cost}")
