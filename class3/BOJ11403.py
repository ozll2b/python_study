n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j]==0:
                if graph[i][k] and graph[k][j]:
                    graph[i][j]=1
                    continue

for g in graph:
    print(' '.join(list(map(str,g))))
