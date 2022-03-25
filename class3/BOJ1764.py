import sys
input=sys.stdin.readline
n,m=map(int,input().split())
never_heard=set()
never_see=set()
for _ in range(n):
    never_heard.add(input().rstrip())
for _ in range(m):
    never_see.add(input().rstrip())

dbj=list(never_see & never_heard)
print(len(dbj))
for name in sorted(dbj):
    print(name)