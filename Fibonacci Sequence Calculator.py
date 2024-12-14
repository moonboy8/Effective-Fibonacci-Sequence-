import sys
import time
import matplotlib.pyplot as plt

# Adjusting the maximum allowed digits for large Fibonacci numbers
sys.set_int_max_str_digits(100000)

# Ask the user for input
fib_num = int(input("Which term of the Fibonacci sequence do you want to find?: "))
choice = int(input("Do you want to list out all the numbers (1) or do you want just the nth number (2): "))

# Function to generate the Fibonacci sequence and measure time for each term
def fibonacci_with_timing(n):
    if n <= 0:
        return [], []  # Return empty lists for invalid input
    elif n == 1:
        return [0], [0]  # Return the first term with 0 runtime
    elif n == 2:
        return [0, 1], [0, 0]  # Return the first two terms with 0 runtime

    fib_sequence = [0, 1]
    timings = [0, 0]  # Initialize runtimes for first two terms

    for i in range(2, n):
        start_time = time.time()
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        end_time = time.time()
        
        fib_sequence.append(next_term)
        timings.append(end_time - start_time)  # Measure time for this term

    return fib_sequence, timings

# Record the start time
start_time = time.time()

# Run the Fibonacci function and store the result
result, runtimes = fibonacci_with_timing(fib_num)

# Record the end time
end_time = time.time()

# Print the results based on the user's choice
if result:  # Only proceed if the sequence is not empty
    if choice == 1:
        # List out all the terms
        print(f"Fibonacci sequence (first {fib_num} terms):")
        for i, term in enumerate(result):
            print(f"Term {i + 1}: {term}")
    elif choice == 2:
        # Print just the nth term (fib_num-1 for 0-based index)
        print(f"The {fib_num}-th term of the Fibonacci sequence is: {result[fib_num - 1]}")
    else:
        print("Invalid choice. Please choose 1 or 2.")
else:
    print("The input must be a positive integer.")

# Calculate total elapsed time
elapsed_time = end_time - start_time

# Display the total time taken
print(f"Total time taken to compute the Fibonacci sequence: {elapsed_time:.15f} seconds")

# Plot the runtimes using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(runtimes) + 1), runtimes, marker='o', linestyle='-', color='b', label='Time per term')
plt.title('Fibonacci Term Calculation Time')
plt.xlabel('Term Number')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()
plt.show()
