# numbers = (0, 1, 2, 3, 4, 5)
#
# print(numbers, sep=";")
# print(*numbers, sep=";")

def testStar(*args):
    print(args)
    for x in args:
        print(x)

testStar(0, 1, 2, 3, 4, 5)

print()

testStar()