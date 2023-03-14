"""
Insertion - Sort(A)
for j = 2 to length(A)
    key = A[j]
    i = j - 1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i - 1
        A[i + 1] = key
    return A
"""


def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while (i >= 0 and A[i] > key):
            A[i + 1] = A[i]
            i = i - 1
            A[i + 1] = key
    return A

a = [2,3,1,4,7,5]
print(InsertionSort(a))