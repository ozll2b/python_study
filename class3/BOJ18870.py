n=int(input())
array=list(map(int,input().split()))
new=sorted(list(set(array)))
dic={}

for i in range(len(new)):
    dic[new[i]]=i

for i in range(len(array)):
    print(dic[array[i]],end=' ')