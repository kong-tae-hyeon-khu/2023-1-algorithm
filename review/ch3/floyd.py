# Setting / 그래프의 인접행렬식 표현
INFINITE = 10000

# 가중치 그래프. 
W = [
    [0,1,INFINITE,1,5], # 1
    [9,0,3,2,INFINITE], # 2
    [INFINITE,INFINITE,0,4,INFINITE], # 3
    [INFINITE,INFINITE,2,0,3], # 4
    [3,INFINITE,INFINITE,INFINITE,0] # 5
]


D = W[:]

# 문제 : 가중치 포함 그래프의 각 정점에서 다른 모든 정점까지의 최단 거리를 계산해라.
#  n : 정점(노드)의 수
def floyd(n, W,D):
    D = W
    for k in range(0, n): # {v0 . . . vk}

        for i in range(0,n):

            for j in range(0,n):

                # 경우 1 : {v1, v2, . .  Vk} 의 정점들 만을 통해서 vi 에서 vj로
                # 가는 최단 경로가 vk를 거치지 않는 경우

                # 경우 2 : vk 를 거치는 경우!
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

# 시간 복잡도 : n^3
# D = floyd(5,W,D)

# 최단 거리 
for i in range(5):
    print(D[i])


P = [[None] * 5 for i in range(5)]


def floyd2(n, W, D):
    D = W
    for k in range(5):
        for i in range(5):
            for j in range(5):

                if (D[i][k] + D[k][j] < D[i][j]):
                    P[i][j] = k + 1
                    D[i][j] = D[i][k] + D[k][j]

def path(q,r):
    if (P[q-1][r-1] != None):
        path(q,P[q-1][r-1])
        print(P[q-1][r-1])
        path(P[q-1][r-1],r)


# floyd2(5,W,D)
# print(P)
# print(path(5,3))