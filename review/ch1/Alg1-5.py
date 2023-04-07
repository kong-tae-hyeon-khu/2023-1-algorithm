# 이분 검색 알고리즘

# 문제 : 크기가 n인 "정렬된" 배열 S에 x가 있는가?
# 입력 : 양수 n, 배열 S[1 . . n], 키 x
# 출력 : x 가 S 의 어디에 있는지의 위치. 만약 없으면 -1


def binary_search(n, S, x):
    location = -1

    low = 0
    high = n-1

    while (low <= high and location == -1):

        mid = (low + high) // 2
        if (x == S[mid]):
            location = mid
        elif (x < S[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return location


test = [1,3,5,7,9,13]
n = 6

x = 7

print(binary_search(n,test,x))



