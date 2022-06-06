def fizz_buzz(seq: int):
    """Returns fizz if an 'int' is divisible by 3,
               buzz if it is divisible by 5, and,
               fizz buzz if if it is divisible by 3 and 5.
    """
    if seq % 3 == 0 and seq % 5 == 0:
        return("fizz buzz")
    if seq % 3 == 0:
        return("fizz")
    if seq % 5 == 0:
        return("buzz")
    return (str(seq))


for i in range(1, 101):
    print("{0:3} - {1}".format(i, fizz_buzz(i)))
