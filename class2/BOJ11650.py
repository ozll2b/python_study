import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
result=sorted(arr,key=lambda x:(x[0],x[1]))
for x,y in result:
    print(x,y)