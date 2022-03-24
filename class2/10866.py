from collections import deque
import sys

def operate_deque(command):
    if command[0]=='push_front':
        deque.appendleft(int(command[1]))
    elif command[0]=='push_back':
        deque.append(int(command[1]))
    elif command[0]=='pop_front':
        print(deque.popleft())  if deque else print(-1)
    elif command[0]=='pop_back':
        print(deque.pop()) if deque else print(-1)
    elif command[0]=='size':
        print(len(deque))
    elif command[0]=='empty':
        print(0) if deque else print(1)
    elif command[0]=='front':
        print(deque[0])  if deque else print(-1)
    elif command[0]=='back':
        print(deque[-1]) if deque else print(-1)

n= int(input())
deque=deque()
for i in range(n):
    command=list(sys.stdin.readline().split())
    operate_deque(command)