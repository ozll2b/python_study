import sys

input=sys.stdin.readline
n,m=map(int,input().split())
cleaned=[[False]*m for _ in range(n)]
r,c,d=map(int,input().split())
cleaned[r][c]=True
graph=[]

dr=[-1,0,1,0]
dc=[0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))


def turn_left():
    global d
    d -=1
    if d ==-1:
        d=3


cnt=1
turn_time=0
while True:
    turn_left()
    nr = r + dr[d]
    nc = c + dc[d]
    if not cleaned[nr][nc] and graph[nr][nc]==0:
        cleaned[nr][nc]=True
        r = nr
        c = nc
        cnt +=1
        turn_time=0
        continue
    else:
        turn_time +=1
    if turn_time==4:
        nr=r-dr[d]
        nc=c-dc[d]
        if graph[nr][nc]==0:
            r=nr
            c=nc
        else:
            break
        turn_time=0
print(cnt)