from collections import deque
import sys

dx=[1,2,-1,-2,1,2,-1,-2]
dy=[-2,-1,-2,-1,2,1,2,1]

def bfs(x,y,cnt):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        if x==tx and y==ty:
            return cnt[x][y]
        for j in range(8):
            nx=x+dx[j]
            ny=y+dy[j]
            #이동하지 않았던 좌표로만 이동(무한루프 방지)
            if 0<=nx<i and 0<=ny<i and not cnt[nx][ny]:
                cnt[nx][ny]=cnt[x][y]+1
                queue.append((nx,ny))

t=int(input())
for _ in range(t):
    i= int(sys.stdin.readline())
    x,y=map(int,sys.stdin.readline().split())
    tx,ty=map(int,sys.stdin.readline().split())
    cnt = [[0 for _ in range(i)] for _ in range(i)]
    print(bfs(x, y, cnt))

