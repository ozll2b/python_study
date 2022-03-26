import sys

input=sys.stdin.readline
n,m=map(int,input().split())
password={}
for _ in range(n):
    site,pw=map(str,input().split())
    password[site]=pw
for _ in range(m):
    s=input().rstrip()
    print(password[s])
