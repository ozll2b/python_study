import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2

    log = sum([x-mid for x in tree if x>=mid])

    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)