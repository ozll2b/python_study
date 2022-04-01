from collections import deque
import copy

n=int(input())
graph=[input() for _  in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

q1=deque()
q2=deque()
v1=[[False]*n for _ in range(n)]
v2=copy.deepcopy(v1)
c1,c2=0,0

def is_same_color(c1,c2):
    if c1==c2 or (c1=='R' and c2=='G') or (c1=='G' and c2=='R'):
        return True
    else:
        return False

def bfs1(visited,q):
    while q:
        x,y=q.popleft()
        visited[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=n or ny>=n or nx<0 or ny<0:
                continue
            if not visited[nx][ny] and graph[x][y]==graph[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True

def bfs2(visited,q):
    while q:
        x,y=q.popleft()
        visited[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=n or ny>=n or nx<0 or ny<0:
                continue
            if not visited[nx][ny] and is_same_color(graph[x][y],graph[nx][ny]):
                q.append((nx,ny))
                visited[nx][ny]=True


for i in range(n):
    for j in range(n):
        if not v1[i][j]:
            q1.append((i,j))
            bfs1(v1,q1)
            c1 +=1
        if not v2[i][j]:
            q2.append((i,j))
            bfs2(v2,q2)
            c2 +=1
print(c1,c2)


