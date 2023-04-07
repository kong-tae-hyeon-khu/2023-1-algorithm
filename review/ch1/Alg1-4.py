# 행렬 곱셈

# 문제 : 두 개의 nXn 행렬의 곱을 구하라
# 입력 : 양의 정수 n, 수의 2차원 배열 A와 B. 여기서 이 행렬의 행과
#       열은 0부터 n-1 까지의 첨자를 갖는다.

# 출력 : A와 B의 곱이 되는 수의 2차원 배열 C. 이 행렬의 행과 열은 모두
#        0부터 n-1 까지의 첨자를 갖는다.


def matrixmult(n, A, B, C):

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]



A = [
    [1,2],
    [3,4]
]

B = [
    [4,3],
    [2,1]
]

C = [
    [0,0],
    [0,0]
]

matrixmult(2, A,B,C)
print(C)