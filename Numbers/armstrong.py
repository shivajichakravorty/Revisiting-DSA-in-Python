def armstrong_number(n):
    """
    Check if a number is an Armstrong number.

    An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits raised to the power of the number of digits.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is an Armstrong number, False otherwise.
    """
    # Convert the number to string to easily iterate over digits
    digits = str(n)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the calculated sum is equal to the original number
    return armstrong_sum == n

def armstrong_number_iterative(n):
    """
    Check if a number is an Armstrong number using an iterative approach.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is an Armstrong number, False otherwise.
    """
    original_number = n
    num_digits = len(str(n))
    armstrong_sum = 0
    
    while n > 0:
        digit = n % 10
        armstrong_sum += digit ** num_digits
        n //= 10
    
    return armstrong_sum == original_number

if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    print(f"Is Armstrong number: {armstrong_number(number)}")
    print(f"Is Armstrong number (iterative): {armstrong_number_iterative(number)}")