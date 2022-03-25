
n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
blue=0
white=0
def cut(paper,n,start):
    global blue,white
    b,w=0,0
    x,y=start
    if n==1:
        if paper[x][y]:
            blue +=1
        else:
            white +=1
        return
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j]:
                b +=1
            else:
                w +=1
            if b*w:
                break
    if b==n**2:
        blue +=1

    elif w==n**2:
        white +=1

    else:
        cut(paper, n // 2, [x, y])
        cut(paper, n // 2, [x, y + (n // 2)])
        cut(paper, n // 2, [x + (n // 2), y])
        cut(paper, n // 2, [x + (n // 2), y + (n // 2)])

cut(paper, n,[0,0])

print(white)
print(blue)