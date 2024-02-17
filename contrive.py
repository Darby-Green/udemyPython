numbers = [1, 45, 31, 12, 60]

for numbers in numbers:
    if numbers % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine!")