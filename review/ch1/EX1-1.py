# 문제 : n 개의 수로 구성된 리스트 S를 비내림차순(nondecreasing order)으로 정렬(sort)하라.
# 파라미터 : S (리스트), n(리스트 구성 원소 갯수)
# 사례 
    # 입력 : S = [10,7,11,5,13,8], n = 6
    # 출력 : S = [5,7,8,10,11,13]

# 참고 : 비내림차순 -> 점점 증가하는 순서 vs. 내림차순

def sort_nonde(S, n ):
    for i in range(n):
        for j in range(n):
            if (S[i] < S[j]):
                # Swap.
                S[i], S[j] = S[j], S[i]

S = [10,7,11,5,13,8]
print(S)
sort_nonde(S,6)
print(S)