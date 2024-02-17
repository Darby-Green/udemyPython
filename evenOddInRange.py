def sum_eo(n, t):
    if t == 'e':
        if n < - 0:
            return 0
        else:
            return sum(i for i in range(1, n) if i % 2 == 0)
    elif t == 'o':
        if n < - 0:
            return 0
        else:
            return sum(i for i in range(1, n) if i % 2 != 0)
    else:
        return -1


print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(11, 'spam'))
