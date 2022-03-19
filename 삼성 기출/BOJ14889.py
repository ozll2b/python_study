from itertools import combinations
import sys

input=sys.stdin.readline

n=int(input())
s=[]
for _ in range(n):
    s.append(list(map(int,input().split())))
total=[x for x in range(n)]
A=list(combinations(total,n//2))

diff=[]
dp=[[0]*n for _ in range(n)]

for i in range(n):
    ans=0
    for j in range(i,n):
        if i!=j:
            dp[i][j]=s[i][j]+s[j][i]

def sum_s(member):
    ans =0
    for i in range(len(member)):
        for j in range(i,len(member)):
            ans += dp[member[i]][member[j]]
    return ans

for a in A:
    b=tuple(set(total)-set(a))
    diff.append(abs(sum_s(a)-sum_s(b)))
print(min(diff))
