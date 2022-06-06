def banner_text(text, screen_width):
    if text == "*":
        print(text*screen_width)
    elif len(text) > screen_width:
        raise ValueError("The string {0} is wider ({1} chars) than the screen allows ({2} chars)."
                         .format(text, len(text), screen_width))
# We could have printed an error (below) and continue processing, but stopping execution is better.
#       print("Sorry - your string is wider than the screen allows")
    else:
        print("**{}**".format(text.center(screen_width - 4)))


banner_text("*", 80)
banner_text("Test", 80)
banner_text("Passing a string wider than the screen allows can be trapped as an error:", 80)
banner_text(" ", 80)
banner_text('raise ValueError("The string {0} is wider {1} than the screen allows {2}."', 80)
banner_text('.format(text, len(text), screen_width))', 80)
banner_text(" ", 80)
banner_text("See the full list of Exceptions in the Python documentation", 80)
# To see the error/crash, uncomment the following line:
# banner_text("Test"*21, 80)
banner_text("*", 80)
