from collections import deque

n,m=map(int,input().split())
r=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    r[a].append(b)
    r[b].append(a)

def bfs(num,n):
    bacon=[0]*(n+1)
    visited=[num]
    q=deque()
    q.append(num)

    while q:
        k=q.popleft()
        for i in r[k]:
            if i not in visited:
                bacon[i]=bacon[k]+1
                visited.append(i)
                q.append(i)
    return sum(bacon)

result=[]

for num in range(1,n+1):
    result.append(bfs(num,n))

print(result.index(min(result))+1)