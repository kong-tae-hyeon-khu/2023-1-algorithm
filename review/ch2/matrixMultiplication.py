# 단순한 행렬곱셈 알고리즘
# 문제 : n X n 크기의 행렬의 곱을 구하시오.
# 입력 : 양수 n, n X n 크기의 행렬 A 와 B
# 출력 : 행렬 A와 B의 곱인 C

C = [[0 for i in range(3)] for j in range(3)]
def matrix_mult(n, A, B):
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j] 
    return C

A  = [[1,2,3], [1,2,3], [1,2,3]]
B = [[3,2,1], [1,2,3], [1,2,3]]

print(matrix_mult(3,A,B))


# # 쉬트라센 버전
# def strassen(n, A, B):
#     if (n <= 3):
#         matrix_mult(n,A,B)
    
#     else:
#         A11 = A[0:n/2][0:n/2] 
#         B11 = 
        