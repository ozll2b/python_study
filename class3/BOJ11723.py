import sys
input=sys.stdin.readline

def op(s,command):
    c=command[0]
    if len(command)>1:
        x=int(command[1])
    if c=='add':
        s.add(x)
    elif c=='remove':
        if x in s:
            s.remove(x)
    elif c=='check':
        if x in s:
            print(1)
        else:
            print(0)
    elif c=='toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    else:
        s.clear()

m=int(input())
s=set()
for _ in range(m):
    command=list(map(str,input().split()))
    if command[0]=='all':
        s={x for x in range(1,21)}
    else:
        op(s,command)
