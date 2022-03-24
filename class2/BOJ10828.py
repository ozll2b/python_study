import sys

n=int(input())
stack=[]


def start(data):
    command=data[0]
    if command=='push':
        stack.append(int(data[1]))
    elif command=='pop':
        if len(stack)>0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif command=='size':
        print(len(stack))
    elif command=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command=='top':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)



for i in range(n):
    data=list(sys.stdin.readline().split())
    start(data)