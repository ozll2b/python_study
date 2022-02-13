import sys
input=sys.stdin.readline

n=int(input())
meet_list=[]
answer=[]
for _ in range(n):
    meet_list.append(list(map(int,input().split())))
meet_list.sort(key=lambda x:(x[1],x[0]))
print(meet_list)
for meet in meet_list:
    if not answer:
        answer.append(meet)
    else:
        if answer[-1][1]<=meet[0]:
            answer.append(meet)
print(len(answer))