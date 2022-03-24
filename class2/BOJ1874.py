import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
arr=deque([int(input()) for _ in range(n)])

stack=[]
op=[]
i=1

while arr:
    if stack and stack[-1]==arr[0]:
        stack.pop()
        arr.popleft()
        op.append('-')
    elif i<=arr[0]:
        stack.append(i)
        op.append('+')
        i +=1
    else:
        print('NO')
        exit(0)

print('\n'.join(op))
