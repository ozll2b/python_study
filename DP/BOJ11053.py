import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            result[i] = max(result[i], result[j]+1)
            print(i,result[i])
print(max(result))
