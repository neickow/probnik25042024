from ipaddress import *
k = 0
ipn = ip_network('174.114.120.0/255.255.252.0', 0)
for i in ipn:
    f = f'{i:b}'
    if f.count('1') % 2 == 0:
        k += 1
print(k)