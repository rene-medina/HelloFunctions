def banner_text(text=" ", screen_width=80):
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
banner_text("Default values for the Arguments can be assigned in the function signature")
banner_text('i.e.  def banner_text(text=" ", screen_width=80):')
banner_text("However calling functions with multiple defaulted Arguments like this: ")
banner_text("banner_text(,80)")
banner_text("Causes an error: any Arguments passed needs to be specified with Keywords,")
banner_text("and any Arguments not used need to be excluded from the call:")
banner_text('banner_text(screen_width=80)    or     banner_text(text="*")')
banner_text("*", 80)
# banner_text(screen_width=80)
# banner_text(text="*")
