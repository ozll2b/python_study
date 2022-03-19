from collections import deque

def spin_c(wheel, d):
    wheel=deque(wheel)
    if d==1:
        wheel.appendleft(wheel.pop())
    elif d==-1:
        wheel.append(wheel.popleft())
    return list(wheel)

def spin(w,num,d):
    dir=[0,0,0,0]
    dir[num]=d
    i=num
    while i>0:
        if w[i][6]!=w[i-1][2]:
            dir[i-1]=-dir[i]
        i-=1
    j=num
    while j<3:
        if w[j][2]!=w[j+1][6]:
            dir[j+1]=-dir[j]
        j+=1

    for i in range(4):
        w[i]=spin_c(w[i],dir[i])
    return w
w=[]
for _ in range(4):
    w.append(list(map(int,input())))

k=int(input())
for i in range(k):
    num, d=map(int,input().split())
    w=spin(w,num-1,d)


score=0
for i in range(4):
    if w[i][0]:
        score += 2**i

print(score)

