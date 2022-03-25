cnt=0
def dfs(graph,v,visited):
    global cnt
    visited[v]=True
    cnt +=1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return cnt
n = int(input())
m = int(input())
graph=[[] for _ in range(n+1)]

for k in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)
print(dfs(graph,1,visited)-1)
