from collections import deque
import sys

input=sys.stdin.readline
n=int(input())
space=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,0,0,1]
dy=[0,-1,1,0]

distance=[[0]*n for _ in range(n)]
size=2

for i in range(n): # 상어의 위치 찾고 0으로 초기화
    for j in range(n):
        if space[i][j]==9:
            temp=[i,j]
            space[i][j]=0

def is_possible(size):
    cnt=0
    for k in range(n):
        cnt += len([s for s in space[k] if 0 < s < size])
    return True if cnt else False



def bfs(temp,visited,cnt):
    global size
    result=[]
    q=deque([temp])
    a,b=temp
    location=distance[a][b]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]: # 범위를 초과하지 않고 방문하지 않았을 때
                if space[nx][ny]==0 or space[nx][ny]==size: # 빈칸이거나 크기가 같은 물고기가 있는 칸은 지나갈 수 있으므로 큐에 넣기
                    q.append([nx,ny])
                    visited[nx][ny]=True
                    distance[nx][ny] = distance[x][y]+1
                elif 0<space[nx][ny]<size: # 물고기의 크기가 아기상어보다 작으면서 빈칸이 아닐 때
                    distance[nx][ny] = distance[x][y]+1
                    visited[nx][ny]=True
                    if not result or (result and result[-1][2]==distance[nx][ny]-location): # 먹을 수 있는 물고기의 위치와 거리를 넣음
                        result.append([nx,ny,distance[nx][ny]-location])
                    elif result[-1][2]<distance[nx][ny]-location:
                        break
    if result:
        result.sort(key=lambda x:(x[0],x[1]))
        x,y=result[0][0],result[0][1]
        space[x][y]=0
        cnt +=1
        if cnt==size:
            size +=1
            cnt=0
        return [x,y],cnt
    else: # 더이상 이동 불가능 -> 엄마상어의 도움 필요
        print(location)
        exit(0)

cnt=0
while is_possible(size):
    visited=[[False]*n for _ in range(n)]
    temp,cnt=bfs(temp,visited,cnt)

x,y=temp
print(distance[x][y])