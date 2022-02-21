# n=int(input())
# def hanoi_cnt(n):
#     return hanoi_cnt(n-1)+2**(n-1) if n>1 else 1
# def hanoi(n):
#     rod=[1,2,3]
#     result=[]
#     cnt=hanoi_cnt(n)
#     if n==1:
#         result=[[1,3]]
#     else:
#         pre_hanoi=hanoi(n-1)
#         for i in range(cnt):
#             if not result:
#                  result.append([1, 3]) if n%2!=0 else result.append([1,2])
#             elif i%2!=0:
#                 result.append(pre_hanoi[(i-1)//2])
#             else:
#                 result.append([result[i-2][1],list(set(rod)-set(result[i-2]))[0]])
#     return result
# print(hanoi_cnt(n))
# for a,b in hanoi(n):
#     print(a,b)

def hanoi(n, a, b):
    if n > 1:
        hanoi(n-1, a, 6-a-b)              # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을
                                          # 중간으로 먼저 다 옮긴다
    print(a, b)

    if n > 1:
        hanoi(n-1, 6-a-b, b)

n = int(input())

print(2**n -1)                               #총 이동해야 하는 횟수
hanoi(n, 1, 3)
