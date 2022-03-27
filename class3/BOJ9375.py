from collections import defaultdict
from functools import reduce
import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    clothes=defaultdict(int)
    for _ in range(n):
        c,k=map(str,input().split())
        clothes[k]+=1

    num = list(clothes.values())
    print((reduce(lambda x, y: x*(y+1), num,1))-1)