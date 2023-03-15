# (1) 비내림차순 != 오름차순 (비슷하지만 다르다. 같은 값이 있을 수 있기 때문)
# n 개의 데이터 (키값은 1 ~ 1,000 사이의 자연수 random)

def bubble_sort(datas):
    length = len(datas)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if datas[j] > datas[j+1]:
                datas[j],datas[j+1] = datas[j+1], datas[j]    


# def quick_sort(n):
