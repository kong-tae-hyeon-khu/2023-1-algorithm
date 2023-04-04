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
        print("V", P[q][r] + 1)
        path(P[q][r], r)
    
    

# 최종 출력.
floyd(5, W, P)
path(2,0) # V3 -> V1 거치는 점들 출력.

# ------------------------------------------------------ #

# 문제 2



# 2-1
def order(p, i, j):
    # 구현부
    if (i == j):
        print("A", i)
    else:
        k = p[i][j]
        print("(",end="")
        order(p,i,k)
        order(k+1,j)
        print(")", end="")


# A1(5x2) , A2(2x3), A3(3,4), A4(4,6), A5(6,7), A6(7,8)
d = [5,2,3,4,6,7,8]
n = len(d) - 1

m = [[0 for j in range(1, n +2 )] for i in range(1, n+2)]
p = [[0 for j in range(1,n+2)] for i in range(1, n+2)]

print(m)
print(p)