from itertools import product

count = 0
for x in product('0123456789abc', repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if s.count('2') == 1:
            for i in '02468ac':
                s = s.replace(i, '*')
            for i in '13579b':
                s = s.replace(i, '/')
            if s.count('**') == 0 and s.count('//') == 0:
                count += 1
print(count)