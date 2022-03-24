import sys
input=sys.stdin.readline

def is_VPS(string):
    stack=[]
    for s in string:
        if stack and (s==')' and stack[-1]=='('):
            stack.pop()
        else:
            stack.append(s)
    return 'YES' if not stack else 'NO'

n=int(input())

for _ in range(n):
    print(is_VPS(input().rstrip()))