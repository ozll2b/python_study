from collections import deque
import sys

input=sys.stdin.readline


def D(num):
    if num*2>9999:
        return (num*2)%10000
    else:
        return num*2

def S(num):
    if num>0:
        return num-1
    else:
        return 9999

def L(num):
    front =num%1000
    back=num//1000
    return front*10+back

def R(num):
    front = num % 10
    back = num // 10
    return front * 1000 + back

def bfs(a,b,checked):
    q=deque([a])
    while q:
        num=q.popleft()
        if num==b:
            return
        else:
            d=D(num)
            s=S(num)
            l=L(num)
            r=R(num)
            if not checked[d]:
                q.append(d)
                checked[d]=[num,'D']
            if not checked[s]:
                q.append(s)
                checked[s] = [num, 'S']
            if not checked[l]:
                q.append(l)
                checked[l] = [num, 'L']
            if not checked[r]:
                q.append(r)
                checked[r] = [num, 'R']

t=int(input())
for _ in range(t):
    checked = [False] * 10001
    a,b=map(int,input().split())
    bfs(a,b,checked)
    result=''
    while b!=a:
        result = checked[b][1]+result
        b=checked[b][0]
    print(result)