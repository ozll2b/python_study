n,k=map(int, input().split())
a=[]
for i in range(n):
    a.append(int(input()))
result=0

a.reverse()
for m in range(0,len(a)):
    count=k//a[m]
    k=k%a[m]

    result += count
    if k==0:
        break
print(result)