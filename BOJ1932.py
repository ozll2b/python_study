n=int(input())

t=[]

for _ in range(n):
    t.append(list(map(int,input().split())))

if n==1:
    print(t[0][0])
    exit(0)

d=[]
d.append(t[0])

for i in range(1,n):
    l=[]
    for j in range(i+1):
        if j==0:
            l.append(d[i-1][0]+t[i][0])
        elif 0<j<i:
            l.append(max(d[i-1][j-1:j+1])+t[i][j])
        else:
            l.append(d[i-1][j-1]+t[i][j])
    d.append(l)

m=0
for numbers in d:
    m=max(m,max(numbers))
print(m)