def f(a, s='', b=38):
    if a>b:
        return False
    if a == b:
        if 'ABA' in s:
            return True
        else:
            return False
    return f(a*2, s+'A') + f(a+3, s+'B')

print(f(2))