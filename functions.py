def multiply(x, y):
    """
    Multiplies 2 variables together that are passed into the
    function.
    :param x:
    :param y:
    :return: x and y multiplied together.
    """
    result = x * y
    return result


# print(multiply(10.5, 4))
#
# for i in range(1, 5):
#     result = multiply(2, i)
#     print(result)


def isPalindrome(string):
    """
    checks if the entered string is a Palindrome
    or not by using string[::-1] to reverse the string and check if both
    the normal and the reversed strings are the same
    :param string:
    :return: True if the string is a Palindrome
    False if it is not
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindromeSentence(sentence):
    """
    Checks if the entered sentence is a palindrome sentence
    by taking the sentence, putting it into a single string,
    while also taking out ant capitals and spaces, then passing
    the final string into the `isPalindrome` function
    :param sentence:
    :return: 
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return isPalindrome(string)


def fibonacci(n):
    """Return the `n` th fib no., for the positive `n`"""
    if 0 <= n <= 1:
        return n
    nMinus1, nMinus2 = 1,0
    result = None
    for f in range(n-1):
        result = nMinus2+nMinus1
        nMinus2 = nMinus1
        nMinus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))




# word = input("please enter a sentence to check: ")
# if palindromeSentence(word):
#     print("'{}' is a Palindrome".format(word))
# else:
#     print("'{}' is not a Palindrome".format(word))
