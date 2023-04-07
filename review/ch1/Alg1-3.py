# 교환 정렬

# 문제 : 비내림차순(nondecreasing order) 으로  n 개의 키를 정렬하라
# 입력 : 양의 정수 n, 키의 배열 S(첨자는 1부터 n)
# 출력 : 키가 비내림차순으로 정렬된 배열 S

def exchangesort(n, S):

    for i in range(n):
        for j in range(i + 1,n):
            if (S[i] > S[j]):
                S[i],S[j] = S[j],S[i]


test = [1,5,3,4,2,9,10,6,6]
print(test)
exchangesort(9,test)
print(test)
