import sys

input=sys.stdin.readline
n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
plus,minus,zero=0,0,0

def cut(paper,n,start):
    global plus,minus,zero
    p,m,z=0,0,0
    x,y=start
    if n==1:
        if paper[x][y]==1:
            plus +=1
        elif paper[x][y]==0:
            zero +=1
        else:
            minus +=1
        return
    for i in range(x,x+n):
        p += len([paper[i][j] for j in range(y,y+n) if paper[i][j]==1])
        m += len([paper[i][j] for j in range(y,y+n) if paper[i][j] == -1])
        z += len([paper[i][j] for j in range(y,y+n) if paper[i][j] == 0])

        if p!=n*(i-x+1) and m!=n*(i-x+1) and z!=n*(i-x+1):
            break

    if p==n**2:
        plus += 1
    elif m==n**2:
        minus +=1
    elif z==n**2:
        zero +=1
    else:
        for a in range(x, x + n, n // 3):
            for b in range(y, y + n, n // 3):
                cut(paper, n // 3, [a, b])

cut(paper, n,[0,0])

print(minus,zero,plus,sep='\n')
