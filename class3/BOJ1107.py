
def close_num(n,broken):
    small,big=n,n
    while small>0:
        if all(int(x) not in broken for x in str(small)):
            break
        small -=1
    while big<1000000:
        if all(int(x) not in broken for x in str(big)):
            break
        big +=1
    if big-n>=n-small and small not in broken:
        return small
    else:
        return big

n=int(input())
m=int(input())
if m>0:
    broken=list(map(int,input().split()))
if m==0 or n==100:
    print(min(abs(100 - n),len(str(n))))
else:
    if len(broken)<10:
        close=close_num(n,broken)
        print(min(abs(n-close)+len(str(close)),abs(100-n)))
    else:
        print(abs(100-n))