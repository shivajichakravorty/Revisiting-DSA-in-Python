def reverse_number(n):
    """Returns the reverse of a positive integer n."""
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

def palindrome_check(n):
    """Checks if a positive integer n is a palindrome."""
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    return n == reverse_number(n)

if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    print(f"Reversed number: {reverse_number(number)}")
    print(f"Is palindrome: {palindrome_check(number)}")