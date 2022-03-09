def solution(n, computers):
    answer = 0
    graph=[[] for _ in range(n)]
    visited=[0]*n
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i!=j:
                graph[i].append(j)

    for i in range(n):
        if sum(visited)==n:
            break
        if not visited[i]:
            dfs(graph,i,visited)
            answer +=1
    return answer

def dfs(graph,v,visited):
    visited[v]=1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)