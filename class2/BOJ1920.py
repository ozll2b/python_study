n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

a.sort()

def binary_search(a,num):
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]==num:
            return 1
        if a[mid]>num:
            right = mid-1
        else:
            left = mid+1
    return 0

for x in b:
    print(binary_search(a,x))