INF = 10000 # 가중치 연결 없는 경우

# 예제
W = [[0,7,4,6,1],
     [INF,0,INF,INF,INF],
     [INF,2,0,5,INF],
     [INF,3,INF,0,INF],
     [INF,INF,INF,1,0]]


def dijkstra(W):
    n = len(W[0])
    length = n * [0]
    touch = n * [0]
    save_length= n * [0]
    f = set()
    for i in range(1,n):
        length[i] = W[0][i]        
        
    for i in range(n-1):
        min = INF
        for i in range(1,n):
            if (0 <= length[i] < min):
                min = length[i]
                vnear = i
    
        e = (touch[vnear], vnear)
        f.add(e)
        

        for i in range(1, n):
            if (length[vnear] + W[vnear][i] < length[i]):
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear
                
                
        save_length[vnear] = length[vnear] # 길이 저장
        length[vnear] = -1
    
    return save_length, f


s , f = dijkstra(W)
print(f) # 집합.
print(s) # 최단 거리.