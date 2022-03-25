from collections import deque

def bfs():
    queue=deque()
    queue.append(n)
    while queue:
        x=queue.popleft()
        if x==k:
            print(distant[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0<=nx<=MAX and not distant[nx]:
                distant[nx]=distant[x]+1
                queue.append(nx)
MAX=10**5
distant=[0]*(MAX+1)
n,k=map(int,input().split())

bfs()