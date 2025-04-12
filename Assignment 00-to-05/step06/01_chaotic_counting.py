import random

# DONE_LIKELIHOOD set karta hai kis chance se done() True return karega
DONE_LIKELIHOOD = 0.3  # 30% chance

# Randomly decide karne ke liye function
def done():
    return random.random() < DONE_LIKELIHOOD

# Chaotic counting function
def chaotic_counting():
    for i in range(1, 11):
        if done():
            return  # Stop counting aur wapas main() pe chalo
        print(i)

# Main function
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# Run the main function
main()
