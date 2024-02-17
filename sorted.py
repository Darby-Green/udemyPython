pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)

print(letter)

dank = [1,2,3,55,22,33,8]

numbers = sorted(dank)
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"]
names.sort()
print(names)