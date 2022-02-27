from collections import deque
n=int(input())
k=int(input())

dx,dy=[0,1,0,-1],[1,0,-1,0]
board=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    i,j=map(int,input().split())
    board[i][j]=2 #사과는 2로 초기화

l=int(input())
direction=[]
for _ in range(l):
    x,c=input().split()
    direction.append([int(x),c])

def move(x,y):
    d=0 #시작방향
    board[x][y]=1 #시작 위치는 1로 초기화
    queue=deque()
    queue.append((x,y))
    time=0

    while queue:
        time +=1
        x +=dx[d]
        y +=dy[d]
        if 1<=x<n+1 and 1<=y<n+1 and board[x][y]!=1:
            if board[x][y]==2:
                board[x][y]=1
            elif board[x][y]==0:
                nx,ny=queue.popleft()
                board[x][y]=1
                board[nx][ny]=0
            queue.append((x,y))
        else:
            return time
        if direction:
            if time==direction[0][0]:
                if direction[0][1]=='D':
                    d = (d+1)%4
                else:
                    d = (d-1)%4
                direction.pop(0)

print(move(1,1))




