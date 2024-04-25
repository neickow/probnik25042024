print('19 ЗАДАНИЕ')
def f(a, b, p):
    if a+b>=80 and p==3:
        return True
    if a+b>=80 and p==2:
        return False
    if a+b<80 and p==3:
        return False
    if p%2==1:
        return f(a+1, b, p+1) or f(a+b, b, p+1) or f(a, b+1, p+1) or f(a, b+a, p+1)
    if p%2==0:
        return f(a+1, b, p+1) or f(a+b, b, p+1) or f(a, b+1, p+1) or f(a, b+a, p+1)
for s in range(1, 71):
    if f(8, s, 1):
        print(s)
        break
print('20 ЗАДАНИЕ')
def f(a, b, p):
    if a+b>=80 and p==4:
        return True
    if a+b>=80 and p==3:
        return False
    if a+b<80 and p==4:
        return False
    if p%2==1:
        return f(a+1, b, p+1) or f(a+b, b, p+1) or f(a, b+1, p+1) or f(a, b+a, p+1)
    if p%2==0:
        return f(a+1, b, p+1) and f(a+b, b, p+1) and f(a, b+1, p+1) and f(a, b+a, p+1)
for s in range(1, 71):
    if f(8, s, 1):
        print(s)
print('21 ЗАДАНИЕ')
def f(a, b, p):
    if a+b>=80 and p in (3, 5):
        return True
    if a+b>=80 and p in (2, 4):
        return False
    if a+b<80 and p==5:
        return False
    if p%2==1:
        return f(a+1, b, p+1) and f(a+b, b, p+1) and f(a, b+1, p+1) and f(a, b+a, p+1)
    if p%2==0:
        return f(a+1, b, p+1) or f(a+b, b, p+1) or f(a, b+1, p+1) or f(a, b+a, p+1)
for s in range(1, 72):
    if f(8, s, 1):
        print(s)