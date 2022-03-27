import sys

input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
s=[0]*(n+1)
s[1]=num[0]

for i in range(2,n+1):
    s[i]=s[i-1]+num[i-1]

for _ in range(m):
    i,j=map(int,input().split())
    print(s[j]-s[i-1])