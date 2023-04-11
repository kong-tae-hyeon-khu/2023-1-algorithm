S = [27,10,12,20,25,13,15,22]


def mergesort2(low, high):

    # mid : 7 // 2 = 3
    # high : 7

    if (low < high) :
        mid = (low + high) // 2
        mergesort2(low, mid) # 배열(S) 를 low ~ mid 까지.
        mergesort2(mid + 1 , high) # 배열(S)를 mid + 1 ~ high 까지.
        merge2(low, mid, high)


def merge2(low, mid, high):
    U = [] # low . . . . high : 합병하는데 필요한 지역 배열.
    print(U)
    i = low
    j = mid + 1
    k = low

    while (i <= mid and j <= high):
        if (S[i] < S[j]):
            U[k] = S[i]
            i += 1
        else:
            U[k] = S[j]
            j += 1
        k += 1

    if (i > mid):
        while (j <= high):
            U[k] = S[j]
            k += 1
            j += 1

    else :
        while (i <= mid):
            U[k] = S[i]
            k += 1
            i += 1
    
    # U 를 다시 S에 적어주자.
    for i in range(low, high + 1):
        S[i] = U[i]



mergesort2(0,7)
print(S)

    