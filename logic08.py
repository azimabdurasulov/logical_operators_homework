def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    a = a % 2 == 0
    b = b % 2 == 0
    return a or b

print(main(54, 45))
