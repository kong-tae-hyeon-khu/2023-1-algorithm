"""
Matrix-Multiplication(A,B):

    n = length(A)
    initialize a n * n matrix C with all elements set to 0

    for i to n :
        for j to n:
            for k to n:
                C[i][j] += A[i][k] * B[k][j]

    return C

"""
a = [[1,2,3],[4,5,6],[7,8,9]] # 3 * 3
b = [[1,2,3],[4,5,6], [7,8,9]] # 3 * 3

c = [[1,2],[3,4]]
d = [[1,2],[3,4]]

def MatrixMultiplication(A,B):

    n = len(A) # == len(B) , 행 또는 열의 갯수.
    
    C = [[0] * n for _ in range(n)]
    
    # i 열 k 행
    for i in range(0, n):
        for j in range(0,n):
            for k in range(0,n):
                
                C[i][j] += A[i][k] * B[k][j]
                print(i,j,C[i][j])

    return C
                
    

    
print(MatrixMultiplication(c,d))

# Nomal Matrix
# A : AxB , B : BxD -> C : A*D

"""
def nomalMatrix(A, B):
    C = [[0] * len(A)] * 
    for i in range(0, len(A)):
        for j in range(0, len(B)):
            for k in range(0, len(B)):
                C[i][j] += A[i][k] * B[k][j]
"""
