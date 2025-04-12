# Define the maximum value for the Fibonacci sequence
MAX_VALUE = 10000

def fibonacci():
    # Starting values for Fib(0) and Fib(1)
    a, b = 0, 1

    # Print the first two Fibonacci numbers
    print(a, end=" ")
    print(b, end=" ", flush=True)

    # Generate Fibonacci numbers until the maximum value is reached
    while True:
        # Calculate the next Fibonacci number
        a, b = b, a + b

        # If the next Fibonacci number exceeds MAX_VALUE, stop the loop
        if b >= MAX_VALUE:
            break
        
        # Print the current Fibonacci number
        print(b, end=" ", flush=True)

# Call the fibonacci function to print the sequence
fibonacci()
