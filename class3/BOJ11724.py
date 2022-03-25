from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

q=deque()

def bfs():
    while q:
        x=q.popleft()
        visited[x]=True
        for y in graph[x]:
            if not visited[y]:
                q.append(y)
                visited[y]=True

cnt=0
for i in range(1,n+1):
    if not visited[i]:
        q.append(i)
        bfs()
        cnt +=1

print(cnt)
