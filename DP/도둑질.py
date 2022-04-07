def solution(money):
    n=len(money)
    dp1=[0]*n
    dp2=[0]*n
    # 1번 집을 터는 경우
    dp1[0]=money[0]
    for i in range(1,n-1): # 마지막 집은 털지 못함
        dp1[i] = max(dp1[i-1],dp1[i-2]+money[i])
    # 1번 집을 털지 않는 경우
    dp1[0]=0
    for i in range(1,n):
        dp2[i]=max(dp2[i-1],dp2[i-2]+money[i])
    return max(dp1[-2],dp2[-1])
print(solution([1,2,3,1]))