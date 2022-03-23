import sys
n=int(input())
arr=list(set([sys.stdin.readline().strip() for i in range(n)]))
arr.sort(key=lambda x:(len(x),x))
print('\n'.join(arr))
