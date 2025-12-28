def fib(n):
    """Return the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Examples:
        >>> fib(0)
        0
        >>> fib(1)
        1
        >>> fib(5)
        5
        >>> fib(10)
        55
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    ans = fib(3)
    print(f"The Fibonacci number is: {ans}")
