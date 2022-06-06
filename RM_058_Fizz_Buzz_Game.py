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


for i in range(1, 21):
    if i % 2 == 0:
        human = input("Please enter your answer: ")
        if human == fizz_buzz(i):
            print("Good! - My turn...")
        else:
            print("Sorry, you're wrong... For {0} the correct answer is {1}"
                  .format(i, fizz_buzz(i)))
            break
    else:
        print("Computer's answer: {}".format(fizz_buzz(i)))
else:
    print("Congratulations, you win!!!! GAME OVER")
