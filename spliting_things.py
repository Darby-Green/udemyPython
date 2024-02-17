panagram = """The quick brown
 fox jumpes\tover
 the lazy dog"""

words = panagram.split()
print(words)
dank = []
numbers = "9,223,372,036,854,775,807"
gen_list = []
for i in numbers:
    if i != " " and i != ",":
        dank.append(int(i))

print(dank)
# Challenge solution
# dank = input("Please enter 3 numbers:")
# dank2 = dank.split(",")
# numb = []
# for i in dank2:
#     numb.append(int(i))
# total = numb[0]+numb[1]-numb[2]
# print(total)