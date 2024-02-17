print("Please choose an option.")
print(" 1. Learn Python \n 2. Play Games \n 3. Go Outside \n 4. Quit")

while True:
    choice = input()
    if choice == "4":
        break
    elif choice in "123":
        print("You chose {}".format(choice))
    else:
        print("Please choose an option.")
        print(" 1. Learn Python \n 2. Play Games \n 3. Go Outside \n 4. Quit")