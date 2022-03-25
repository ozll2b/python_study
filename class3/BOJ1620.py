import sys
input=sys.stdin.readline

n,m=map(int,input().split())

names={}
num={}
for i in range(n):
    name=input().rstrip()
    names[i+1]=name
    num[name]=i+1


for _ in range(m):
    p=input().rstrip()
    if p.isdigit():
        print(names[int(p)])
    else:
        print(num[p])