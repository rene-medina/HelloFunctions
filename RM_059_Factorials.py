def factorial(nbr: int) -> int:
    """
    Returns the factorial of an `int`
    :param nbr: `int`
    :return: the factorial of an `int`
    """
    if nbr == 0:
        return 1

    calc = 1
    for i in range(1, nbr+1):
        calc *= i
    return calc


for j in range(0, 36):
    print(j, factorial(j))

