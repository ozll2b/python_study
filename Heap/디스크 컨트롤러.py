import heapq as hq
def solution(jobs):
    answer,now,i=0,0,0
    start=-1
    n=len(jobs)
    heap=[]

    while i<n:
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start<j[0]<=now:
                hq.heappush(heap,[j[1],j[0]])
        if len(heap)>0: # 처리할 작업이 있는 경우
            current=hq.heappop(heap)
            start=now
            now+=current[0]
            answer +=(now-current[1]) # 작업 요청 시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음시간으로 넘어감
            now +=1
    return answer//n

print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))