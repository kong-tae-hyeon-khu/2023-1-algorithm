"""
Median Of Medians -> Quick Sort 의 적당한 Pivot 값을 찾기 위해 (최대한 중간값.)
"""
def medianOfMedians(arr):
    if len(arr) <= 5:
        return findMedian(arr)
    
    medians = []
    for i in range(0, int(len(arr)/5)):
        group = arr[i*5 : min((i+1)*5, len(arr))]
        
        median = findMedian(group)
        medians.append(median)
        approximate_median = medianOfMedians(medians)
        return approximate_median
    
def findMedian(arr):
    arr.sort()
    return arr[len(arr)//2]


"""
Qucik Sort
"""

def quick_sort(arr, low, high):
    if low < high :

        
        pivotIndex = partition(arr, low, high) 
        
        quick_sort(arr, low, pivotIndex - 1)
        quick_sort(arr, pivotIndex + 1, high)



def partition(arr, low, high):

    pivot = medianOfMedians(arr[low:high + 1])
   


    while low <= high :
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        
        if low <= high:
            arr[low],arr[high] = arr[high], arr[low]
            low , high = low + 1, high - 1
   
    return low - 1

   




test = [1,9,2,7,0,6]
print(test)
quick_sort(test, 0 , len(test) - 1)
print(test)
