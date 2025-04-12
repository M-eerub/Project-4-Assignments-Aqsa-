import random  # Random number generate karne ke liye

def roll_dice():
    die1 = random.randint(1, 6)  # Pehla dice
    die2 = random.randint(1, 6)  # Dusra dice
    print("Die 1:", die1)
    print("Die 2:", die2)

# Dice ko 3 baar roll karna hai
print("First Roll:")
roll_dice()

print("\nSecond Roll:")
roll_dice()

print("\nThird Roll:")
roll_dice()
