import math
n=int(input())
num=math.factorial(n)
cnt=0
s=str(num)
i=len(s)-1

while s[i]=='0':
    i -=1
    cnt +=1
print(cnt)
