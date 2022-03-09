import sys

input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
sum,result=0,0
for t in sorted(arr):
    sum += t
    result += sum
print(result)