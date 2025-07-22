def fact(n):
    """ Calculate !n """
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result

def factRecur(n):
    """ Calculate !n recursively"""
    if n <= 1:
        return 1
    else:
        return n * factRecur(n-1)\


def fib(n): # not the most efficient way to cal fib numbers
    """F(n) = F(n-1) + F(n-2)"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibFast(n): # Much faster than the recursion
    result = 0
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        numb1 = 0
        numb2 = 1
        for i in range(1, n + 1):
            result = numb2 + numb1
            numb2 = numb1
            numb1 = result
    return result


for i in range(10):
    print(i, fibFast(i))