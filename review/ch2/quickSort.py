test_case = [15,22,13,27,12,10,20,25]


def quicksort(low,high):
   

    if (low < high):
        index = partition(low, high)
        quicksort(low, index - 1)
        quicksort(index + 1, high)


def partition(low, high):
    pivotitem = test_case[low]; # 첫 번째 값

    j = low
    for i in range(low + 1, high + 1):
        if test_case[i] < pivotitem:
            j += 1
            test_case[i], test_case[j] = test_case[j], test_case[i]
    pivot_index = j

    test_case[low], test_case[pivot_index] = test_case[pivot_index], test_case[low]  
    return pivot_index



quicksort(0, 7)
print(test_case)