n,m,x,y,k=map(int,input().split())
board=[]
dice=[[0]*3 for _ in range(4)]
move=[[],[0,1],[0,-1],[-1,0],[1,0]]
for _ in range(n):
    board.append(list(map(int,input().split())))
directions=list(map(int,input().split()))

def roll(dice,d):
    if d==1:
        dice[1][2],dice[3][1]=dice[3][1],dice[1][2]
        dice[1].insert(0,dice[1].pop())
    elif d==2:
        dice[1][0], dice[3][1] = dice[3][1], dice[1][0]
        dice[1].append(dice[1].pop(0))
    elif d==3:
        l = []
        for i in range(4):
            l.append(dice[i][1])
        l.append(l.pop(0))
        for i in range(4):
            dice[i][1] = l[i]
    else:
        l = []
        for i in range(4):
            l.append(dice[i][1])
        l.insert(0, l.pop())
        for i in range(4):
            dice[i][1] = l[i]

for d in directions:
    if not(0<=x+move[d][0]<n and 0<=y+move[d][1]<m):
        continue
    x +=move[d][0]
    y +=move[d][1]
    roll(dice,d)
    if board[x][y]==0:
        board[x][y]=dice[3][1]
    else:
        dice[3][1]=board[x][y]
        board[x][y]=0
    print(dice[1][1])
