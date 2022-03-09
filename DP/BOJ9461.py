d=[0]*101

d[1]=1
d[2]=1
d[3]=1

for i in range(3,101):
    d[i]=(d[i-2]+d[i-3])

t=int(input())
for _ in range(t):
    print(d[int(input())])