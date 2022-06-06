def return_int(prompt):
    while True:
        value = input(prompt)
        if value.isnumeric():
            return int(value)
        print("Please enter a valid number")
        print()


print("Thanks, your age is: {} years old".format(return_int("Please enter your age: ")))
print()
