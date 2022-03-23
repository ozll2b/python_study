
def color(new):
    c1,c2=0,0
    for i in range(8):
        if i%2==0:
            c1 += len([x for x in new[i][::2] if x!='B'])+len([x for x in new[i][1::2] if x != 'W'])
            c2 += len([x for x in new[i][::2] if x!='W'])+len([x for x in new[i][1::2] if x != 'B'])
        else:
            c2 += len([x for x in new[i][::2] if x != 'B']) + len([x for x in new[i][1::2] if x != 'W'])
            c1 += len([x for x in new[i][::2] if x != 'W']) + len([x for x in new[i][1::2] if x != 'B'])

    return min(c1,c2)

n,m=map(int,input().split())

board=[]
for _ in range(n):
    board.append(input())
new=[]
result=[]

for i in range(n-7):
    for j in range(m-7):
        for k in range(i,i+8):
            new.append(board[k][j:j+8])
        result.append(color(new))
        new=[]
print(min(result))

