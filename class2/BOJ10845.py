from collections import deque
import sys

def q(queue,string):
    arr=string.split(' ')
    cmd=arr[0]
    if len(arr)==2:
        num=arr[1]
    if cmd=='push':
        queue.append(num)
    elif cmd=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd=='size':
        print(len(queue))
    elif cmd=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)

input=sys.stdin.readline
n=int(input())
queue=deque()
for _ in range(n):
    q(queue,input().rstrip())