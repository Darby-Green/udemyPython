name = input("Please enter your name: ")
age = int(input("How old are you? "))
if age >= 18 and age < 30:
    print("Have a nice holiday, {}!".format(name))
else:
    print("m8, this isn't for you...")
