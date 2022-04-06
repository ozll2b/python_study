def solution(triangle):
    n=len(triangle)
    d = []
    d.append(triangle[0])
    for i in range(1,n):
        l=[]
        for j in range(i+1):
            if j==0:
                l.append(d[i-1][0]+triangle[i][0])
            elif 0<j<i:
                l.append(max(d[i-1][j-1:j+1])+triangle[i][j])
            else:
                l.append(d[i-1][j-1]+triangle[i][j])
        d.append(l)
    m = 0
    for numbers in d:
        m = max(m, max(numbers))
    return m

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))