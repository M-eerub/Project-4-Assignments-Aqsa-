def main():
    number_counts = {}  # Dictionary to store counts

    while True:
        number = input("Enter a number (or press enter to finish): ")

        if number == "":
            break

        # Convert to int
        number = int(number)

        # Count the number using dictionary
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    # Print the results
    print("\nResults:")
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")

# Run the program
main()
