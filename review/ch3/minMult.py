# DP -> M[i][j] : i <= j 일 때, 
#               Ai 부터 Aj 까지의 행렬을 곱하는데 필요한 기본적인 곱셈의 최소 횟수

#  minimum(M[i][k] + M[k+1][j] + Alpha) 

# P -> 최적 순서의 구축

d = [5,2,3,4,6,7,8] # 5x2 X 2x3 X 3x4 X 4x6 X 6x7 X 7x8


# n = 6
def minmult(n,d): #  n : 항의 개수 (A1, A2 , . . , An) 
    
    DP = [[None] * 6 for i in range(6)]

    for i in range(n):
        DP[i][i] = 0 

    for diagonal in range(1, n): # 대각선의 의미를 알고 있어야해.
        for i in range(0, n - diagonal):
            j = i + diagonal 
            
            # 변형 없이 순차대로 곱하는 경우야. => A1 A2 A3 DP[0][2] => DP[0][0] DP[1][2] + 
            min = DP[i][i] + DP[i+1][j] + d[i]*d[i+1]*d[j+1] # 여기가 문제인거 같아. # k = i 인 경우.
            DP[i][j] = min

            for k in range(i + 1 , j):
                if (DP[i][k] + DP[k+1][j] + d[i]*d[k+1]*d[j+1] < min):
                    min = DP[i][k] + DP[k+1][j] + d[i]*d[k+1]*d[j+1]
                    DP[i][j] = min
            

                
            
            

    return DP[0][n-1]


print(minmult(6,d))
                





