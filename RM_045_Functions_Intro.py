def multiply(x, y):
    return x * y


def is_palindrome(string):
    backwards = string[::-1].casefold()
    return backwards == string.casefold()


def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalpha():
            string += char
# Notice the following shorthand version where the calc and comparison are done in the result itself.
#    return string[::-1].casefold() == string.casefold()
# The following version is preferred as it prevents code duplication: a function that calls another function
    return is_palindrome(string)


print("Please remember to leave exactly 2 blank lines after each function definition")
print()
print("The result of the call to the function multiply(10, 5) is {})".format(multiply(10, 5)))
print()
print('The function call: is_palindrome("radar") returns: {} '.format(is_palindrome("radar")))
print('The function call: is_palindrome("Radar") correctly returns: {} '.format(is_palindrome("Radar")))
print('while is_palindrome("rodent") return: {}'.format(is_palindrome("rodent")))
print("Recall that a Palindrome is a word that spells the same forward and backwards, ignoring case")
input("Press ENTER to continue")
print("\n"*10)

print("Similarly, checking if a sentence is a Palindrome first removes spaces, commas, etc from a string...")
print('The function call: is_palindrome_sentence("Was it a car, or a cat, I saw") returns: {} '.format(is_palindrome("radar")))
