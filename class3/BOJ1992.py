n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

answer=''
def quadtree(n,r):
    global answer
    x,y=r
    o,z=0,0

    if n==1:
        if graph[x][y]==1:
            answer +='1'
        else:
            answer +='0'
        return

    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j]==1:
                o +=1
            else:
                z+=1
            if o*z>0:
                break
    if o==n**2:
        answer +='1'
    elif z==n**2:
        answer +='0'
    else:
        answer +='('
        for i in range(x,x+(n//2)+1,n//2):
            for j in range(y, y+(n // 2) + 1, n // 2):
                quadtree(n//2,(i,j))
        answer += ')'
    return
quadtree(n,(0,0))
print(answer)
