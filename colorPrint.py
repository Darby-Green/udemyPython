import colorama

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

print(RED, "This will be in red")
print("and so is this")
print(BLUE, "This will be in blue")


def colorPrint(text: str, *effects: str) -> None:
    """
    Print text using the ANSI sequences to change color
    :param text: text to print
    :param effects: effects we want, zero or more constants defined at start
    """
    effectString = "".join(effects)
    outputString = "{0}{1}{2}".format(effectString,text,RESET)
    print(outputString)

colorama.init()
colorPrint("Hello, red", RED)
colorPrint("Hello, red in bold", RED, BOLD)
colorPrint("Hello, blue", BLUE)
colorPrint("Hello, blue reversed", BLUE, REVERSE)
colorPrint("Hello, blue underlined and bold", BLUE, UNDERLINE, BOLD)
print("Normal terminal color")
colorPrint("Hello, green", GREEN)
colorama.deinit()