n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
result=0

for p in a:
    if p==b and b>c:
        result +=1
    elif p<b:
        result +=1
    else:
        result+=(p-b)//c+1
        if (p-b)%c!=0:
            result +=1

print(result)