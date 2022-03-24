
n,m=map(int,input().split())
card=list(map(int,input().split()))
result=[]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k]<=m:
                result.append(m-(card[i]+card[j]+card[k]))

print(m-min(result))