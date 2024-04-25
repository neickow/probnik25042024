from fnmatch import fnmatch

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

important = [i for i in range(2, 10000) if is_prime(i)]

def f(n):
    a = []
    i = 0
    while n > 1:
        while n % important[i] == 0 and n > 1:
            a.append(important[i])
            n = n // important[i]
        i += 1
    return a

for i in range(10 ** 4 + 1):
    if fnmatch(str(i), '*2?2'):
        a = f(i)
        if len(a) == 7:
            print(i, a[-1])