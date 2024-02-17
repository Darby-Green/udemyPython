avalable_parts = ["Computer",
                  "Monitor",
                  "Keyboard",
                  "Mouse",
                  "Mouse Mat",
                  "HDMI Cable",
                  "DVD Drive"
                  ]
valid_choices = []
for i in range(1,len(avalable_parts)+1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice)-1
        chosen_part = avalable_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("The List is now: {}".format(computer_parts))
    else:
        print("Please choose and option:")
        for number, part in enumerate(avalable_parts):
            print("{0}: {1}".format(number+1, part))

    current_choice = input()

print(computer_parts)


