import heapq

def solution(operations):
    minq, maxq = [], []
    visited = [False for _ in range(1000001)]

    for i in range(len(operations)):
        alpha,num=operations[i].split(' ')
        if alpha == 'I':
            heapq.heappush(minq, (int(num), i))
            heapq.heappush(maxq, (-int(num), i))
            visited[i] = True
        elif num == '-1': # 최솟값 삭제
            while minq and not visited[minq[0][1]]:
                heapq.heappop(minq)
            if minq:
                visited[minq[0][1]] = False
                heapq.heappop(minq)
        else:
            while maxq and not visited[maxq[0][1]]:
                heapq.heappop(maxq)
            if maxq:
                visited[maxq[0][1]] = False
                heapq.heappop(maxq)
    while minq and not visited[minq[0][1]]: heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]: heapq.heappop(maxq)

    if minq and maxq: # 최댓값 삭제
        return [-maxq[0][0], minq[0][0]]
    else:
        return [0,0]

print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))
