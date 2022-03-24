n=int(input())
result=0
for i in range(1,n):
    if i+sum(list(map(int,str(i))))==n:
        result=i
        break
print(result)


