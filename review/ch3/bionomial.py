# 이항계수 : 분할 정복식 접근 방법
def bin(n, k):
    if (k == 0 or k == n):
        return 1
    else:
        return bin(n-1, k-1) + bin(n-1, k)
    


# 이항 계수 : 동적계획법
def bin2(n,k):
    # 일단 DP[n][k] 생성.  [0. . . . . n][0 . . . . . k] => [n+1][k+1]
    DP = [[0] * (k+1) for i in range(n+1)]
    for i in range(n+1): # 0 ~ n 까지 .

        for j in range(0, min(i,k)+1): # 0 ~ k 또는 0~i 까지.

            if (j == 0 or j == i):
                DP[i][j] = 1
            else:
                DP[i][j] = DP[i-1][j-1] + DP[i-1][j]

    return DP[n][k]
