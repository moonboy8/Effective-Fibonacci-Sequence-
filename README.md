# Fibonacci Sequence Calculator

This Python program allows you to calculate and display the Fibonacci sequence up to the `n`-th term, where `n` is provided by the user. The program also gives the option to either display the entire Fibonacci sequence or just the `n`-th term. It supports large Fibonacci numbers by allowing Python's `int` type to handle large values through the configuration of `sys.set_int_max_str_digits`.

## Features
- Calculate the Fibonacci sequence up to any term number `n`.
- Option to display the full Fibonacci sequence or just the `n`-th term.
- Support for large Fibonacci numbers by adjusting the integer string conversion limit.

## Requirements
- Python 3.x
- No external libraries required (standard Python libraries used)

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. The program will prompt you for input:
   - **Which term of the Fibonacci sequence do you want to find?** (Enter an integer `n`)
   - **Do you want to list out all the numbers (1) or do you want just the nth number (2)?**

   Depending on your choice:
   - If you choose option `1`, the program will print the Fibonacci sequence up to the `n`-th term.
   - If you choose option `2`, the program will print only the `n`-th Fibonacci number.

## Example

### Sample Run:

```bash
Which term of the Fibonacci sequence do you want to find?: 10
Do you want to list out all the numbers (1) or do you want just the nth number (2): 1
Fibonacci sequence (first 10 terms):
Term 1: 0
Term 2: 1
Term 3: 1
Term 4: 2
Term 5: 3
Term 6: 5
Term 7: 8
Term 8: 13
Term 9: 21
Term 10: 34
Time taken: 0.000003 seconds



### Issues:

This program calculates Fibonacci numbers using an iterative method, which has a time complexity of O(n). For smaller values of n (up to tens of thousands), this approach works well. However, as n increases, the program's performance may degrade due to the nature of Fibonacci growth.

For extremely large values of n, the time required to compute large Fibonacci numbers may grow substantially, but Python's built-in handling of arbitrary-precision integers ensures the program can calculate Fibonacci numbers of great magnitude.

Large Fibonacci Numbers: The program's performance can degrade significantly for very large values of n due to the rapid growth of Fibonacci numbers. Computing the Fibonacci numbers for n greater than 10,000 can take considerable time and memory, especially if printing all terms is selected.

Integer Overflow: While Python can handle arbitrarily large integers, the Fibonacci sequence grows exponentially. For extremely large values of n, the result can be a number with millions of digits, causing a slowdown in calculations and possible memory constraints.

Time Limit for Displaying Results: Printing a very large number or a long sequence of Fibonacci numbers can take a significant amount of time, especially if the user chooses to display all terms. This might lead to a long wait before results are shown.

User Input Errors: The program assumes that the user enters valid integers for the term number (n). Invalid inputs (such as non-numeric values) are not handled in this version of the program, and may result in unexpected behavior or crashes.


