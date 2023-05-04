def optsearchtree(n, p):

    # n * n  : DP
    DP = [[None] * n for i in range(n)]
    # 최솟값을 주는 k의 값 
    R = [[None] * n for i in range(n)]

    for i in range(n):
        DP[i][i-1] = 0
        DP[i][i] = p[i]
        R[i][i] = i
        R[i][i-1] = 0

    