# 배열의 수 더하기

# 문제 : n 개의 수로 된 배열 S에 있는 모든 수를 더하라
# 입력 : 양의 정수 n, 수의 배열 S (첨자는 0부터 n-1)
# 출력 : S에 있는 수의 합, sum



def sum(n, S) :
    result = 0

    for i in range(n):
        result = result + S[i]

    return result


test = [1,2,3,4,5,6,9]
print(sum(7,test))
