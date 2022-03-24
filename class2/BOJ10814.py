import sys

input=sys.stdin.readline
n=int(input())
members=[]
for i in range(n):
    members.append(list(map(str,input().split())))
    members[i].append(i)
members.sort(key=lambda x:(int(x[0]),x[2]))
for age,name,order in members:
    print(age,name)