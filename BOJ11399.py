import sys

input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
time=[]
sum=0
result=0
for i in range(1,n+1):
    time.append([i,arr[i-1]])
time.sort(key=lambda x:x[1])
for t in time:
    sum += t[1]
    result += sum
print(result)