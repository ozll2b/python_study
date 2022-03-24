import sys
from collections import deque

input=sys.stdin.readline

t=int(input())
for _ in range(t):
    cnt=0
    n,m=map(int,input().split())
    doc=deque([[i,x] for i,x in enumerate(list(map(int,input().split())))])
    while True:
        d,p=doc.popleft()
        if any(p<x[1] for x in doc):
            doc.append([d,p])
        else:
            cnt +=1
            if d==m:
                print(cnt)
                break
