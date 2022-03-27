from functools import reduce
n=int(input())
m=int(input())
s=input()

i=0
cnt=[]
c=0
while i<len(s)-2:
    if s[i:i+3]=='IOI':
        i +=2
        c +=1
    else:
        i +=1
        if c>0:
            cnt.append(c)
            c=0
if c:
    cnt.append(c)

print(sum([x-n+1 for x in cnt if x>=n]))

