# 어떤 문제를 재귀적으로 작은 하위 문제로 분할.
# 이러한 하위 문제를 독립적으로 해결.
# 문제의 솔루션을 결합하여 최종 결과를 얻는 문제 해결 전략.
# 재귀는 문제를 더 간단한 하위 문제로 분해할 수 있기 때문에 분할 및 정복 접근법에서 핵심적인 역할.

# Merge Sort -> 쪼개진 것을 정렬.

def merge(left,right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if (left[left_index] <= right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = int(len(list)/2)
    left = merge_sort(list[0:mid])
    right = merge_sort(list[mid:len(list)])

    return merge(left,right)

print("Merge Sort")
test = [2,3,1,6,4]
print(merge_sort(test))

# Binary-Search 
def binary_search(list, obj):
    mid = int(len(list)/2)
    if (list[mid] == obj):
        return mid
    
    elif (list[mid] > obj):
        return binary_search(list[mid + 1 : len(list)], obj)
    
    else:
        return binary_search(list[0 : mid], obj)
    

print("Binary Search")
test = [2,3,4,1,7,8]
print(binary_search(test,3))
    

