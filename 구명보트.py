from collections import deque
def solution(people,limit):
    answer=0
    people=deque(sorted(people))
    while people:
        a=people.popleft()
        answer += 1
        while people and a+people.pop()>limit:
            answer +=1
    return answer
