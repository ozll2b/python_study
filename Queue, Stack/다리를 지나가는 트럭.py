from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks=deque(truck_weights)
    bridge=deque()
    total=0
    while trucks or total:
        if total:
            total -= bridge.popleft()

        while len(bridge)<bridge_length:
            if trucks and total+trucks[0]<=weight:
                bridge.append(trucks.popleft())
                total += bridge[-1]
            else:
                bridge.append(0)

            answer+=1
    return answer



# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     trucks=deque(truck_weights)
#     bridge=deque()
#     total=0
#     while trucks:
#         if bridge:
#             total -= bridge.popleft()
#
#         while len(bridge)<bridge_length:
#             if trucks and total+trucks[0]<=weight:
#                 bridge.append(trucks.popleft())
#                 total += bridge[-1]
#             else:
#                 bridge.append(0)
#
#             answer+=1
#
#     for i in range(len(bridge)-1,-1,-1):
#         if bridge[i]:
#             break
#     return answer +(i+1)


# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     road=[]
#     while truck_weights:
#         if sum(road)+truck_weights[0]<=weight or len(road)==0:
#             road.append(truck_weights.pop(0))
#         else:
#             if len(road)<bridge_length:
#                 answer += bridge_length
#                 road.clear()
#             else:
#                 road.pop(0)
#                 answer += 1
#     return answer







print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))