def multiply(x: float, y: float) -> float:
    """Multiplies 2 numbers"""

    return x * y


def fibonacci(n: int) -> int:
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


def is_palindrome(text: str) -> bool:
    """"Returns `True` if the string spells the same forwards and backwards (Palindrome)"""
    backwards = text[::-1].casefold()
    return backwards == text.casefold()


def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """Surrounds the text with '**' and centers it on the screen"""
    if text == "*":
        print(text*screen_width)
    elif len(text) > screen_width:
        raise ValueError("The string {0} is wider ({1} chars) than the screen allows ({2} chars)."
                         .format(text, len(text), screen_width))
    # We could have printed an error (below) and continue processing, but stopping execution is better.
    #       print("Sorry - your string is wider than the screen allows")
    else:
        print("**{}**".format(text.center(screen_width - 4)))


print("This code contains samples of Docstrings (overall function documentation)")
print("and Annotations (documentation for the function's parameters used in its signature)")
print("Both Docstrings an Annotations can be seen by hovering a function.")
print()
print("In Annotations, notice how parameters with default values are annotated.")

