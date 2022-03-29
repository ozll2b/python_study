import heapq
import sys

input = sys.stdin.readline
n = int(input())
q = []


def abs_heap(q, x):
    if x:
        heapq.heappush(q, (abs(x), x // abs(x)))
    else:
        if q:
            val, ab = heapq.heappop(q)
            print(val * ab)
        else:
            print(0)

for _ in range(n):
    abs_heap(q, int(input()))
