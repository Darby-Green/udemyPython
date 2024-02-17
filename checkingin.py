parrot = "Norwegian Blue"
letter = input("Enter a chatacter: ")
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("{} is not in {}".format(letter, parrot))