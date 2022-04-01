from collections import deque

n,m=map(int,input().split())
board=[0]*101
visited=[False]*101

snake= {}
ladder= {}
for _ in range(n):
    start,end=map(int,input().split())
    ladder[start]=end
for _ in range(m):
    start, end = map(int, input().split())
    snake[start]=end

q=deque([1])

while q:
    x=q.popleft()
    if x== 100:
        print(board[x])
        break
    for dice in range(1,7):
        next = x+dice
        if next<=100 and not visited[next]:
            if next in ladder.keys():
                next=ladder[next]
            if next in snake.keys():
                next=snake[next]
            if not visited[next]:
                visited[next]=True
                board[next]=board[x]+1
                q.append(next)

