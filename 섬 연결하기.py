
def solution(n, costs):
    answer = 0
    connected=set()
    costs.sort(key=lambda x:(x[2],x[0]))
    while len(connected)<n:
        if not connected:
            a,b,cost=costs.pop(0)
        else:
            for i,c in enumerate(costs):
                if (c[0] in connected and c[1] not in connected) or (c[0] not in connected and c[1] in connected):
                    a,b,cost=costs.pop(i)
                    break
        connected.add(a)
        connected.add(b)
        answer += cost
    return answer

