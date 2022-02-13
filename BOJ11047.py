n,k=map(int, input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
result=0

arr.reverse()
for m in arr:
    count=k//m
    k=k%m
    result += count
    if k==0:
        break
print(result)