def power(a, n):
    res = a
    x = a
    if n == 0:
        return 1
    if n < 0:
        n = -n
        a = 1 / a
    for _ in range(0, n - 1):
        for _ in range(0, a - 1):
            res += x
        x = res
    return res


print(power(5,5))