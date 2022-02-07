import sys
sys.setrecursionlimit(10**6)
t=int(sys.stdin.readline())

def dfs(start,group):
    visited[start]=group
    for i in graph[start]:
        if not visited[i]:
            a=dfs(i,-group)
            if not a:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

for _ in range(t):
    V,E=map(int,sys.stdin.readline().split())
    graph=[[]for _ in range(V+1)]
    visited=[False]*(V+1)
    for _ in range(E):
        a,b=map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,V+1):
        if not visited[i]:
            result = dfs(i,1)
            if not result:
                break
    print("YES" if result else "NO")

