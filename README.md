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
