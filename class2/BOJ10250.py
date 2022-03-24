t=int(input())
for _ in range(t):
    h,w,n=map(int,input().split())
    ans,res=divmod(n,h)
    if res==0:
        res=h
        ans -=1
    print(str(res)+'0'+str(ans+1)) if ans+1<=9 else print(str(res)+str(ans+1))

