import sys
input = sys.stdin.readline
a,b,c=map(int,input().split())


def square(N, k, d):
    if k == 0:
        return 1
    elif k == 1:
        return N % d

    tmp = square(N, k // 2, d)
    if k % 2:
        return (tmp * tmp * N) % d
    else:
        return (tmp * tmp) % d


print(square(a,b,c))