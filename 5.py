# mnr=10**20
# for N in range(1, 1000):
#     R = bin(N)[2:]
#     if N%3==0:
#         R = R+'010'
#     else:
#         R = R+bin(5*(N%3))[2:]
#     R = int(R , 2)
#     if R%2==0 and R>300:
#         mnr=min(mnr, R)
# print(mnr)
mnr=10**20
for N in range(1, 1000):
    R = bin(N)[2:]
    if N%3==0:
        R = R+'010'
    else:
        R = R+bin(5*(N%3))[2:]
    R = int(R , 2)
    if R==314:
        print(N)

