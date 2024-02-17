tree1 = "pods"
tree2 = "pod"

if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are not the same")

x = 5
y = 7

if x > y:
    print("X is greater than Y")
elif x < y:
    print("X is less than Y")
else:
    print("X and Y are equal")

for i in range(0, 10):
    print(i)

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break


