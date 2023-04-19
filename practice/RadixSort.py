

def radixSort(arr):
    maxVal = Max(arr) # 배열 원소들 중의 최댓 자릿수 파악하기.

    # 최하위 자릿수부터 시작 -> 1의 자리부터 maxVal의 자리까지.
    for i in range(1, maxVal + 1):

        # 각 자릿수의 숫자를 저장할 버킷 10개
        buckets = [[] for i in range(10)]

        for j in arr:
            #  현재 숫자를 기준으로 각 숫자를 해당 버킷에 넣는다.
            digit = getDigit(j,i)
            buckets[digit].append(j)
        

        arr = []
        for bucket in buckets:
            for num in bucket:
                arr.append(num)

    return arr

# 123 -> getDigit(123, 2) => 2

def getDigit(j,i): # i 는 원하는 자리수
    for n in range(1, i):
        j = j // 10
    return j % 10

# print(getDigit(123,2))

        

def Max(arr):
    maxval = max(arr)
    
    result = 1

    while((maxval//10) != 0):
        result += 1
        maxval = maxval // 10
    
    return result


test = [170, 45, 75, 90, 2, 802, 3, 66, 1, 100]

print(radixSort(test))

# bucket = [[] for i in range(10)]
# print(bucket)