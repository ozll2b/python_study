from collections import deque
n,k=map(int,input().split())
arr=deque([x for x in range(1,n+1)])
result=[]
while arr:
    for _ in range(k-1):
        arr.append(arr.popleft())
    result.append(str(arr.popleft()))
print('<'+', '.join(result)+'>')

