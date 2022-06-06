import colorama

# colorama fixes Windows' lack of usage of the Escape Color  Sequences
# Some ANSI escape sequences for colours and effects

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

colorama.init()
print(RED, "This should print in RED...")
print("And it will continue printing until it is reset")
print()
print(RESET, "There, back to normal")
print("Additional effects:")
print(GREEN, "This is GREEN...")
print(YELLOW, "YELLOW...")
print(BLUE, "BLUE...")
print(MAGENTA, "MAGENTA...")
print(CYAN, "CYAN...")
print(WHITE, "WHITE")
print(BOLD, "BOLD...")
print(REVERSE, "REVERSE", RESET)
print(UNDERLINE, "and UNDERLINE")
print(RESET, "")
colorama.deinit()
