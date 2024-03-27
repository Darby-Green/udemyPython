def factorial(numb):
    '''
    prints the factorial for a given number numb
    if numb < 1 then it just return 1
    :param numb:
    :return:
    '''
    if numb < 1:
        return 1
    return numb * factorial(numb - 1)

for i in range(36):
    print(factorial(i))