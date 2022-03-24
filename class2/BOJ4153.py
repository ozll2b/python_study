
def is_right_triangle(arr):
    if arr[0]**2+arr[1]**2==arr[2]**2:
        return 'right'
    else:
        return 'wrong'

while True:
    arr=list(map(int,input().split()))
    arr.sort()
    if sum(arr)==0:
        break
    print(is_right_triangle(arr))
