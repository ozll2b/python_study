# def solution(triangle):
#     n=len(triangle)
#     d = []
#     d.append(triangle[0])
#     m=max(d)
#     for i in range(1,n):
#         l=[]
#         for j in range(i+1):
#             if j==0:
#                 l.append(d[i-1][0]+triangle[i][0])
#             elif 0<j<i:
#                 l.append(max(d[i-1][j-1:j+1])+triangle[i][j])
#             else:
#                 l.append(d[i-1][j-1]+triangle[i][j])
#         d.append(l)
#         m=max(l)
#
#     return m
def solution(triangle):
    answer=0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0: # 가장 왼쪽
                triangle[i][j] += triangle[i-1][j]
            elif j== len(triangle[i])-1: # 가장 오른쪽
                triangle[i][j] += triangle[i-1][j-1]
            else: # 가운데
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
    answer = max(triangle[-1])
    return answer
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))