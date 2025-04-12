def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    if low <= n <= high:
        return True
    else:
        return False

# Sample run in main
def main():
    number = int(input("Enter a number: "))
    low = int(input("Enter the low value: "))
    high = int(input("Enter the high value: "))
    
    if in_range(number, low, high):
        print(f"{number} is in the range {low} to {high}.")
    else:
        print(f"{number} is NOT in the range {low} to {high}.")

if __name__ == "__main__":
    main()
