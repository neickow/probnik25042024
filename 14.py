def f(n):
    s = 0
    while n > 0:
        if n % 3 == 2:
            s += 1
        n = n // 3
    return s

s = 2 * 9 ** 10 - 3 ** 5 + 5
print(f(s))