def factors(n):
    """Returns a list of factors of a positive integer n."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    return [i for i in range(1, n + 1) if n % i == 0]

def factors_iterative(n):
    """Returns a list of factors of a positive integer n using an iterative approach.
    This is a bit optimal compared to the first approach. 
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    return result

def factors_optimized(n):
    """
    Iterate through numbers from 1 to the square root of n to find factors.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:  # Avoid adding the square root twice for perfect squares
                result.append(n // i)
    return sorted(result)




if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    print(f"Factors of {number}: {factors(number)}")
    print(f"Factors of {number} (iterative): {factors_iterative(number)}")
    print(f"Factors of {number} (optimized): {factors_optimized(number)}")