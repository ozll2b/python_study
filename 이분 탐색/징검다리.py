def solution(distance, rocks, n):
    position=[0]+sorted(rocks)+[distance]
    left=1
    right=distance

    while left<right:
        mid=(left+right)//2
        print('++++',left,right,mid)
        cnt=0
        i,j=0,1
        while j<=len(position)-1:
            if position[j]-position[i]<mid:
                cnt +=1
                j +=1
            else:
                i=j
                j+=1
            print(i,j,cnt)
        if cnt>n:
            right =mid
        else:
            left = mid+1
    return left-1


print(solution(25,[2, 14, 11, 21, 17],2))