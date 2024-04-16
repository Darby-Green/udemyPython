availableParts = {"1": "Computer",
                  "2": "Monitor",
                  "3": "Keyboard",
                  "4": "Mouse",
                  "5": "Mouse Mat",
                  "6": "HDMI Cable",
                  "7": "DVD Drive"
                  }

currentChoice = None
while currentChoice != "0":
    if currentChoice in availableParts:
        chosenPart = availableParts[currentChoice]
        print(f"Adding {chosenPart}")
    else:
        print("Please choose a valid choice!")
        for key, value in availableParts.items():
            print(f"{key}: {value}")
        print("0: to Finish")
    currentChoice = input("> ")
