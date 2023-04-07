# Dynamic Programming -> Bottom to Up

INFINITE = 1000

NULL = 9999
W = [
    [0,1,INFINITE,1,5],
    [9,0,3,2,INFINITE],
    [INFINITE, INFINITE, 0, 4, INFINITE],
    [INFINITE, INFINITE, 2, 0 , 3],
    [3, INFINITE, INFINITE, INFINITE, 0]
]
P = [
    [NULL,NULL,NULL,NULL,NULL],
    [NULL,NULL,NULL,NULL,NULL],
    [NULL,NULL,NULL,NULL,NULL],
    [NULL,NULL,NULL,NULL,NULL],
    [NULL,NULL,NULL,NULL,NULL],
]
# 문제 1-1 : 최단 경로 배열 만들기.
def floyd(size,  W, P):

    D = W

    for k in range(0, size):
        for i in range(0,size):
            for j in range(0,size):
                if (D[i][k] + D[k][j] < D[i][j]): #  k를 거쳐가는 상황이 더 좋을 때.
                    P[i][j] = k # k 를 거친다.
                    D[i][j] = D[i][k] + D[k][j]
    

# 문제 1-2 : 최단 경로 출력하기

def path(q,r):
    
    if P[q][r] != NULL :
        path(q, P[q][r])
        print("V", P[q][r] + 1, end= " -> ")
        path(P[q][r], r)
    
    

# 최종 출력.


floyd(5, W, P)

# V3 -> V1 경로.
print("경로 출력 !")

print("V 3 -> " , end=" ")
path(2,0) # 거치는 점들
print("V 1")

print()


# ------------------------------------------------------------------#

# 문제 2

# A1 : 5X2 , A2 : 2X3, A3 : 3X4, A4 : 4X6 , A5 : 6X7, A6 : 7X8
d = [5,2,3,4,6,7,8] 
n = len(d) - 1 # 행렬의 갯수.




# 곱셈의 횟수의 최소치.
m = [[0 for j in range(1, n+2)] for i in range(1,n+2)]


# 최적의 순서로 갈라지는 기점
p = [[0 for j in range(1, n+2)] for i in range(1,n+2)]

# 현재 행렬은 6개이지만, 기록을 위한 배열은 7X7 이다. 따라서 편의를 위해서 인덱스를 1부터 6까지 사용하자.


def minMulti(n,d, p):
    for diagonal in range(1,n): # 1 -> n-1
        for i in range(1, n- diagonal + 1):
            j = i + diagonal
            # 최솟값 찾기.
            # 일단 k = i 로 가정.
            m[i][j] = m[i][i] + m[i+1][j] + d[i-1]*d[i]*d[j]
            p[i][j] = i

            for k in range(i + 1 , j):
                min = m[i][k] + m[k+1][j] + d[i-1]*d[k]*d[j]
                if min < m[i][j] :
                    m[i][j] = min
                    p[i][j] = k
    return m[1][n]

# 최적 순서 출력.
def order(p, i , j):
    if i == j :
        print("A", i, end="", sep="")
    else:
        k = p[i][j]
        print("(", end="")
        order(p,i,k)
        order(p,k+1, j)
        print(")", end="")

# 사용하지 않는 m[0] 의 행을 무시하고 출력하기 위함.
def printMatrix(m):
    for i in range(1, len(m[0])):
        print(m[i])

print("적용 전")
printMatrix(m)

print()

minMulti(n, d, p)

print("적용 후")
printMatrix(m)

print()
order(p,1,6)
