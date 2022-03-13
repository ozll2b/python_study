import copy
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
answer = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque()
    cg = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if cg[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if cg[nx][ny] == 0:
                cg[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0
    for row in cg:
        cnt += row.count(0)
    answer = max(answer, cnt)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0


make_wall(0)
print(answer)



