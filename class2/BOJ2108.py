import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
dic = {x : 0 for x in arr}
for num in arr:
    dic[num] += 1

new=sorted(dic.items(), key=lambda x: x[1])

avgsum = round(sum(arr)/len(arr))
mid=arr[len(arr)//2]

m=new[-1][1]
max_list=[x for x in new if x[1]==m]
often=max_list[-1][0] if len(max_list)==1 else max_list[1][0]
r=max(arr)-min(arr)

print(avgsum)
print(mid)
print(often)
print(r)