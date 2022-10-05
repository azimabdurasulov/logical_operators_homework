from re import X


def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    x1 = x % 10
    x //= 10

    x2 = x % 10
    x //= 10

    x3 = x % 10
    x //= 10
    return x3 * 100 + x2 * 10 + x1 == x1 * 100 + x2 * 10 + x3

print(main(454))