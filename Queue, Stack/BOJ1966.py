from collections import deque

t=int(input())

for _ in range(t):
    n,m = map(int, input().split())
    queue= deque([[i,x] for i,x in enumerate(list(map(int,input().split())))])
    while queue:
        idx,i = queue.popleft()
        if any(i<x[1] for x in queue):
            queue.append([idx,i])
        else:
            if idx==m:
                print(n-len(queue))
                continue
