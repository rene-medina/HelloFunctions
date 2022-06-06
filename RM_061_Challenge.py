def sum_numbers(*args: float) -> float:
    """
    Takes a string of int, separated by comma, and returns its sum
    :param args: comma separated values to be added
    :return: the sum of the csv
    """

    total = 0
    for value in args:
        total += value
    return total

