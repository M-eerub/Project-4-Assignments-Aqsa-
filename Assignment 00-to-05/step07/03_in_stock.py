# Helper function - assume this is already written
def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "mango": 150,
        "orange": 0  # example of out of stock
    }
    return inventory.get(fruit, 0)

# Main function
def main():
    fruit = input("Enter a fruit: ").lower()  # user input, lowercase for consistency
    count = num_in_stock(fruit)
    
    if count > 0:
        print("This fruit is in stock! Here is how many:")
        print(count)
    else:
        print("This fruit is not in stock.")

# Run the main function
main()
