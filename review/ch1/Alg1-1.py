# 순차검색 알고리즘

# 문제 : n 개의 키로 구성된 배열 S에 키 x 가 있는가?
# 입력 : 양의 정수 n, 1 에서 n 까지의 첨자를 가진 키의 배열 S, 그리고 x
# 출력 : S 안에 x의 위치를 가리키는 location(S안에 x 없으면 -1)

def seq_seach(n, S ,x):
    location = 0
    while (location < n and S[location] != x):
        location += 1
    
    if (location >= n):
        location = -1
        
    return location

x = 8
test1 = [1,2,3,4,5,6,7]
test2 = [2,8,1,3,4,9]

print(seq_seach(7,test1,x))
print(seq_seach(6,test2,x))
        
