def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b = a
    x1 = b % 10
    b //= 10

    x2 = b % 10
    b //= 10

    x3 = b % 10
    b //= 10

    x4 = b % 10
    b //= 10

    x5 = b % 10
    b //= 10
    return x1 < x2 < x3 < x4 < x5 

print(main(98765))