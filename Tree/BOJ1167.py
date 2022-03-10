import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
tree=[[] for _ in range(n+1)]

for _ in range(n):
    arr= list(map(int,input().split()))[:-1]
    i=arr.pop(0)
    while arr:
        v=arr.pop(0)
        d=arr.pop(0)
        tree[i].append((v,d))

def bfs(start):
    visit = [-1]*(n+1)
    queue=deque()
    queue.append(start)
    visit[start]=0
    _max =[0,0]

    while queue:
        t = queue.popleft()
        for i,d in tree[t]:
            if visit[i] == -1:
                visit[i] = visit[t] + d
                queue.append(i)
                if _max[0]<visit[i]:
                    _max = visit[i],i
    return _max

distance, node = bfs(1)
distance, node = bfs(node)
print(distance)
