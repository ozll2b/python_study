t=int(input())
d=[]

d.append([1, 0])
d.append([0, 1])
d.append([1, 1])
for i in range(3, 41):
    d.append([d[i - 1][0] + d[i - 2][0], d[i - 1][1] + d[i - 2][1]])

for _ in range(t):
    n=int(input())
    zero,one=d[n]
    print(zero,one)
