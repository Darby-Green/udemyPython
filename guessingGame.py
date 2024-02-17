import random


def getInteger(prompt):
    """
    Get and int from (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered

    :param prompt:  String user will see when there prompted
        to enter a value.
    :return: the int that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number" .format(temp))

print(input.__doc__)
print("*" * 80)
print(getInteger.__get__)
print("*" * 80)

highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = getInteger(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")