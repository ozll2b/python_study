import sys

input=sys.stdin.readline
dp=[0]*13
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4,13):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

t=int(input())
for _ in range(t):
    print(dp[int(input())])