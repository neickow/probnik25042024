s=open('17-4.txt').readlines()
s=[int(x) for x in s]
sr=sum(s)/len(s)
ans=0
sm=-10**10
for i in range(len(s)-1):
    if str(s[i])[-1]=='9' or str(s[i+1])[-1]=='9':
        if s[i]<sr and s[i+1]<sr:
            ans+=1
            sm=max(sm, s[i]+s[i+1])
print(ans, sm)