import math  # Square root ke liye

# User se input lena
ab = float(input("Enter the length of AB: "))
ac = float(input("Enter the length of AC: "))

# Pythagorean theorem: BC² = AB² + AC²
bc = math.sqrt(ab**2 + ac**2)

# Output dikhana
print(f"The length of BC (the hypotenuse) is: {bc}")
