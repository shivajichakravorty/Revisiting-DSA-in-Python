from math import *

def count_digits(n):
    """Returns the number of digits in a positive integer n."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    return floor(log10(n)) + 1

def count_digits_iterative(n):
    """Returns the number of digits in a positive integer n using an iterative approach."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    print(f"Number of digits (using logarithm): {count_digits(number)}")
    print(f"Number of digits (using iteration): {count_digits_iterative(number)}")