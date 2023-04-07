# 문제 : 어떤 수 x가 n개의 수로 구성된 리스트 S 에 있는지 결정하라. S에 있으면 "예", 없으면 "아니오"로 답하시오.

# 파라미터 : S (list), n (list 의 원소의 갯수.), x(찾는 원소.)

def search(S,n,x):
    result = False
    for i in range(n):
        if (S[i] == x):
            return "예"
            
    return "아니오"

S = [10,7,11,5,13,8]
n = 6
x = 5
print(search(S,n,x))