def mergesort(n, S):
    # n = 7 (배열 사이즈) & index [0,1,2,3,4,5,6] 


    # h 와 m 이 분할된 배열의 사이즈가 되면 더 편할것.
    h = n // 2 # h = 3 
    m = n - h # m = 4
    U = []
    V = []
    if (n > 1) :
        # Copy S[0] through S[h - 1] to U[]
        for i in range(0, h):
            U.append(S[i])
        # Copy S[h] through S[n - 1] to V[]
        for j in range(h, n):
            V.append(S[j])
        
        mergesort(h, U)  
        mergesort(m, V)  
        merge(h, m ,U,V,S)

def merge(h,m,U,V,S):
    
    i = 0
    j = 0
    k = 0

    while i < h and j < m :
        if (U[i] < V[j]):
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1

    if (i > h):

        # Copy V 의 남은 항들을 S 로 !
        while (j < m):
            S[k] = V[j]
            k += 1
            j += 1
            
    else:
        # Copy U 의 남은 항들을 S 로 !
        while (i < h):
            S[k] = U[i]
            k += 1
            i += 1



n = 8
S = [27,10,12,20,25,13,15,22]

mergesort(n,S)
print(S)