from collections import deque
n,m=map(int, input().split())
graph=[]
queue=deque()
for i in range(m):
    graph.append(list(map(int,input().split())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))
def bfs():
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[ny][nx]==0:
                graph[ny][nx]= graph[y][x]+1
                queue.append((ny,nx))
    return graph
bfs()
day=0
for l in graph:
    if 0 in l:
        print(-1)
        exit(0)
    else:
        day=max(day,max(l))
print(day-1)