import sys
input=sys.stdin.readline
n=int(input())

roads=list(map(int,input().split()))
costs=list(map(int,input().split()))
costs=costs[:-1]
cost=0
min_cost=costs[0]
for i in range(len(costs)):
    if costs[i]<=min_cost:
        min_cost = costs[i]
        cost += min_cost*roads[i]
    else:
        cost += min_cost*roads[i]

print(cost)