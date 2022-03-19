n,l=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

cnt=0

def check_route(n,l,route):
    placed=[0]*n
    for i in range(n-1):
        if route[i] != route[i+1]:
            if abs(route[i]-route[i+1])>1:
                return False
            else:
                if route[i]-route[i+1]==1:
                    if i+1+l>n:
                        return False
                    check = route[i+1]
                    for j in range(i+1,i+1+l):
                        if placed[j] or route[j]!=check:
                            return False
                        placed[j]=1
                elif route[i+1] - route[i]==1:
                    if i-l<-1:
                        return False
                    check = route[i]
                    for j in range(i,i-l,-1):
                        if placed[j] or route[j]!=check:
                            return False
                        placed[j]=1
    return True

for r in graph:
    if check_route(n,l,r):
        cnt +=1

for c in range(n):
    if check_route(n,l,[graph[r][c] for r in range(n)]):
        cnt +=1
print(cnt)

