from itertools import combinations
n,k=map(int,input().split())
arr=[i for i in combinations([x for x in range(1,n+1)],k)]
print(len(arr))