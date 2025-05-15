def pythonFood():
    width = 80
    text = 'spam and eggs'
    leftMargin = (width - len(text)) // 2
    print(" " * leftMargin, text)


def centerText(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    leftMargin = (80 - len(text)) // 2
    print(" " * leftMargin, text, end=end, file=file, flush=flush)

with open('Centered', mode='w') as centered_file:
    # pythonFood(file=centered_file)
    centerText("Dank", "Meme", file=centered_file)
    centerText("This is something that I made here", "Some other thing that is here", file=centered_file)
    