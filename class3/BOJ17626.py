import sys
input = sys.stdin.readline
n=int(input())

dp=[int(1e9)]*(n+1)

k=1
for i in range(1,n+1):
    if k**2==i:
        dp[i]=1
        k+=1
        continue
    for j in range(1,k):
        dp[i]=min(dp[i],dp[j**2]+dp[i-(j**2)])

print(dp[n])
