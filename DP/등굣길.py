def solution(m, n, puddles):

    dx=[0,-1]
    dy=[-1,0]
    ground=[[1]*m for _ in range(n)]
    route=[[0]*m for _ in range(n)]
    for j,i in puddles:
        ground[i-1][j-1]=0

    for x in range(n):
        for y in range(m):
            if x==0 and y==0:
                route[x][y]=1
                continue
            elif ground[x][y]:
                for i in range(2):
                    px=x+dx[i]
                    py=y+dy[i]
                    if 0<=px<n and 0<=py<m:
                        route[x][y] += route[px][py]

    return route[n-1][m-1]%1000000007
