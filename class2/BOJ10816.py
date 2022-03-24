from collections import Counter

n=int(input())
card=list(map(int,input().split()))
m=int(input())
num=list(map(int,input().split()))
result=[]
cnt=Counter(card)
for x in num:
    result.append(cnt[x])
print(*result)
