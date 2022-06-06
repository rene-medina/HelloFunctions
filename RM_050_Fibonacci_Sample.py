def fibonacci(n):
    """Returns the `n` th fibonaccie number of `n`."""
    fib_result = None
    # Notice the following assignment...
    nbr_minus1, nbr_minus2 = 1, 0

    if 0 <= n <= 1:
        fib_result = n
        return fib_result

    for i in range(n):
        fib_result = nbr_minus1 + nbr_minus2
        nbr_minus2 = nbr_minus1
        nbr_minus1 = fib_result

    return fib_result


for j in range(10):
    print(fibonacci(j))


