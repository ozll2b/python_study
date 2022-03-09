from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,w,visited):
    queue=deque()
    queue.append((x,y,w))
    visited[x][y][w]=1
    while queue:
        x,y,w=queue.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][w]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny >=m:
                continue
            if graph[nx][ny]==0 and not visited[nx][ny][w]:
                queue.append((nx,ny,w))
                visited[nx][ny][w]=visited[x][y][w]+1
            if graph[nx][ny]==1 and not w:
                queue.append((nx, ny,w+1))
                visited[nx][ny][w+1]=visited[x][y][w]+1
    return -1

print(bfs(0,0,0,visited))