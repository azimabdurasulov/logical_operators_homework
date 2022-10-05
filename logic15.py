def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1 = a // 100
    x2 = a % 100 // 10
    x3 = a % 10
    return a // 100 > 0 and (x1 + x2 + x3) % 2 == 1

print(main(436))
