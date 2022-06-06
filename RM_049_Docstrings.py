def return_int(prompt):
    """
    Gets an input recursively until the input can be converted to an `int`

    :param prompt: The prompt to be displayed to the user
    :return: An integer
    """
    while True:
        value = input(prompt)
        if value.isnumeric():
            return int(value)
        else:
            print("Invalid entry, please try again.")


v = return_int("Please enter a digit: ")
print(v)

