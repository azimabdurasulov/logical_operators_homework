def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    a = a % 2 == 1
    b = b % 2 == 1
    return a or b

print(main(35, 890))
