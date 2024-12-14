import sys
import time
sys.set_int_max_str_digits(100000)

# Ask the user for input
fib_num = int(input("Which term of the Fibonacci sequence do you want to find?: "))
choice = int(input("Do you want to list out all the numbers (1) or do you want just the nth number (2): "))

# Function to generate the Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return []  # Return an empty list for non-positive input
    elif n == 1:
        return [0]  # Return the first term
    elif n == 2:
        return [0, 1]  # Return the first two terms
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)
    return fib_sequence

# Record the start time
start_time = time.time()

# Run the Fibonacci function and store the result
result = fibonacci(fib_num)

# Record the end time
end_time = time.time()

# Print the results based on the user's choice
if result:  # Only proceed if the sequence is not empty
    if choice == 1:
        # List out all the terms
        print(f"Fibonacci sequence (first {fib_num} terms):")
        for i, term in enumerate(result):
            print(f"Term {i + 1}: {term}")
            print(" " * 90)  # Spacing for readability (optional)
    elif choice == 2:
        # Print just the nth term (fib_num-1 for 0-based index)
        print(f"The {fib_num}-th term of the Fibonacci sequence is: {result[fib_num - 1]}")
    else:
        print("Invalid choice. Please choose 1 or 2.")
else:
    print("The input must be a positive integer.")

# Calculate elapsed time
elapsed_time = end_time - start_time

# Display the time taken
print(f"Time taken: {elapsed_time:.15f} seconds")
