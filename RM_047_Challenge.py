def return_int(prompt):
    while True:
        value = input(prompt)
        if value.isnumeric():
            if int(value) >= 0:
                return int(value)
        print("Please enter a valid number")
        print()


def return_eo(prompt):
    while True:
        value = input(prompt)
        if value.casefold().strip() in "eo":
            return value.casefold().strip()
        print("Please enter e for even or o for an odd sum")
        print()


def sum_eo(up_bound, even_odd):
    if even_odd == "o":
        start = 1
    elif even_odd == "e":
        start = 2
    else:
        return -1
    step = 2
    total = 0
    for i in range(start, up_bound, step):
        total += i
    return total


n = return_int("Please enter a positive, upper bound number: ")
t = return_eo("Please enter e for even or o for an odd sum: ")

cond = "odd"
if t == "e":
    cond = "even"

print("The result of summing {0} numbers up to {1} is {2}"
      .format(cond, n, sum_eo(n, t)))

# Course Solution:
#
# def sum_eo(n, t):
#     """Sum even or odd numbers in range.
#
#     Return the sum of even or odd natural numbers, in the range 1..n-1.
#
#     :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
#     :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
#     :return: The sum of the even or odd numbers in the range.
#             Returns -1 if `t` is not 'e' or 'o'.
#     """
#     if t == "e":
#         start = 2
#     elif t == 'o':
#         start = 1
#     else:
#         return -1
#
#     return sum(range(start, n, 2))
