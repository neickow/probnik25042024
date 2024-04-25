s=open('24-j6.txt').readline()
l=1
mxl=0
for i in range(len(s)-1):
    if int(s[i])<int(s[i+1]):
        l+=1
    else:
        if l==5:
            mxl+=1
        l=1
print(mxl)