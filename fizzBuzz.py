def fizz_buzz(numb):
    '''
    Fizz bUZZ GAME
    returns Fizz when numb / by 3
    returns Buzz when numb / by 5
    returns Fizz Buzz when numb / by both 3 and 5 (15)
    if not / by the above numbers then returns the original value
    :param numb:
    :return:
    '''
    if numb % 15 == 0:
        return "fizz buzz"
    elif numb % 3 == 0:
        return "fizz"
    elif numb % 5 == 0:
        return "buzz"
    else:
        return str(numb)

for i in range(1, 16):
    print(fizz_buzz(i))
# numb = int(input("Pick a Number: "))
# print(fizz_buzz(numb))

# for i in range(1,16):
#     dank = fizz_buzz(i)
#     tonk = input("Please guesses a number: ")
#
#     if dank == tonk:
#         continue
#     elif i >= 15:
#         print("That's correct")
#     elif dank != tonk:
#         print("Wrong")
#         break

nextNumb = 0
while nextNumb < 15:
    nextNumb += 1
    print(fizz_buzz(nextNumb))
    nextNumb += 1
    correctAnswer = fizz_buzz(nextNumb)
    playerInput = input("Your go: ")
    if playerInput != correctAnswer:
        print("That's the wrong answer, {} was the correct answer."
              .format(correctAnswer))
        break
else:
    print("well done you reached {}"
          .format(nextNumb - 1))