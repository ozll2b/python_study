import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result1 = [1] * N
result2=[1]*N
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            result1[i] = max(result1[i], result1[j]+1)

arr.reverse()
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            result2[i] = max(result2[i], result2[j]+1)
result2.reverse()
result=[x+y-1 for x,y in zip(result1,result2)]
print(max(result))
