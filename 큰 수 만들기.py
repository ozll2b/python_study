def solution(number, k):
    answer=''
    n=len(number)-k

    while n>0:
        if len(number) == n:
            answer += number
            break
        m = 0
        for i in range(0,len(number)-n+1):
            if int(number[i]) >= m:
                m=int(number[i])
                max_idx = number.index(str(m))
                if m==9:
                    break

        answer += number[max_idx]
        number = number[max_idx+1:]
        n -= 1

    return answer