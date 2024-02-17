day = input("What day is it? ")
temp = int(input("How hot is it? "))
rain = False

if (day == "Saturday" and temp > 27) or not rain:
    print("Yay, you can go swim!!")
else:
    print("You can't swim now!")