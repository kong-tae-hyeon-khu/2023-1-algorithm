# (1) 비내림차순 != 오름차순 (비슷하지만 다르다. 같은 값이 있을 수 있기 때문)
# n 개의 데이터 (키값은 1 ~ 1,000 사이의 자연수 random)

def bubble_sort(datas):
    length = len(datas)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if datas[j] > datas[j+1]:
                datas[j],datas[j+1] = datas[j+1], datas[j]    

def quick_sort(datas, start, end):
    
    if start >= end:
        return
    
    pivot_index = start
    left = start + 1
    right = end

    while left <= right:

        # 피벗보다 작은 데이터를 찾자.
            while left <= end and datas[left] <= datas[pivot_index] :
                 left += 1
        # 피벗보다 큰 데이터들 . . .
            while right > start and datas[right] >= datas[pivot_index] :
                 right -= 1
                
            if left > right: # 엇갈림.
                 datas[right] , datas[pivot_index] = datas[pivot_index] , datas[right]
            else: # 엇갈리지 않음.
                 datas[right], datas[left] = datas[left], datas[right]
                
    # 재귀 호출
    quick_sort(datas, start, right - 1)
    quick_sort(datas, right + 1, end)
            
# ---------------------------------------------------------------------------------------------------

# (2) 테이블 작성용
import random
import time






# Case 1 : N = 5000

test_data1 = []
test_data2 = []

for random_value in range(0, 5000):
     
     # 각각의 동일한 테스트 데이터 생성
     value = random.randint(1, 1000)
     test_data1.append(value)
     test_data2.append(value)

print("n = 5000 ------------------")

# (bubble sort)
start = time.time()
bubble_sort(test_data1)
end = time.time()
print(end - start)


# (quick_sort)
start = time.time()
quick_sort(test_data2, 0, len(test_data2) - 1)
end = time.time()
print(end-start)

# ---------------------------------------------------------------------------------------------------

# Case 2 : N = 10,000

test_data1 = []
test_data2 = []

for random_value in range(0, 10000):
     
     # 각각의 동일한 테스트 데이터 생성
     value = random.randint(1, 1000)
     test_data1.append(value)
     test_data2.append(value)

print("n = 10000 ------------------")

# (bubble sort)
start = time.time()
bubble_sort(test_data1)
end = time.time()
print(end - start)


# (quick_sort)
start = time.time()
quick_sort(test_data2, 0, len(test_data2) - 1)
end = time.time()
print(end-start)

""" 15,000 ~ 80,000 까지의 경우. (주석처리)
# ---------------------------------------------------------------------------------------------------

# Case 3 : N = 15,000
test_data1 = []
test_data2 = []

for random_value in range(0, 15000):
     
     # 각각의 동일한 테스트 데이터 생성
     value = random.randint(1, 1000)
     test_data1.append(value)
     test_data2.append(value)

print("n = 15000 ------------------")

# (bubble sort)
start = time.time()
bubble_sort(test_data1)
end = time.time()
print(end - start)


# (quick_sort)
start = time.time()
quick_sort(test_data2, 0, len(test_data2) - 1)
end = time.time()
print(end-start)


# ---------------------------------------------------------------------------------------------------

# Case 4 : N = 20,000
test_data1 = []
test_data2 = []

for random_value in range(0, 20000):
     
     # 각각의 동일한 테스트 데이터 생성
     value = random.randint(1, 1000)
     test_data1.append(value)
     test_data2.append(value)

print("n = 20000 ------------------")

# (bubble sort)
start = time.time()
bubble_sort(test_data1)
end = time.time()
print(end - start)


# (quick_sort)
start = time.time()
quick_sort(test_data2, 0, len(test_data2) - 1)
end = time.time()
print(end-start)


# ---------------------------------------------------------------------------------------------------

# Case 5 : N = 30,000
test_data1 = []
test_data2 = []

for random_value in range(0, 30000):
     
     # 각각의 동일한 테스트 데이터 생성
     value = random.randint(1, 1000)
     test_data1.append(value)
     test_data2.append(value)

print("n = 30000 ------------------")

# (bubble sort)
start = time.time()
bubble_sort(test_data1)
end = time.time()
print(end - start)


# (quick_sort)
start = time.time()
quick_sort(test_data2, 0, len(test_data2) - 1)
end = time.time()
print(end-start)


# ---------------------------------------------------------------------------------------------------

# Case 6 : N = 40,000

test_data1 = []
test_data2 = []

for random_value in range(0, 40000):
     
     # 각각의 동일한 테스트 데이터 생성
     value = random.randint(1, 1000)
     test_data1.append(value)
     test_data2.append(value)

print("n = 40000 ------------------")

# (bubble sort)
start = time.time()
bubble_sort(test_data1)
end = time.time()
print(end - start)


# (quick_sort)
start = time.time()
quick_sort(test_data2, 0, len(test_data2) - 1)
end = time.time()
print(end-start)

# ---------------------------------------------------------------------------------------------------

# Case 7 : N = 80,000 
test_data = []
for random_value in range(0, 80000):
     test_data.append(random.randint(1,1000))

print("n = 80000 quick_sort ------------------")

# (quick_sort)
start = time.time()
quick_sort(test_data, 0, len(test_data) - 1)
end = time.time()
print(end-start)

"""