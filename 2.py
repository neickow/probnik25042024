print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w <= z) and ((y <= x)==(z <= y))
                if f:
                    print(x, y, z, w)