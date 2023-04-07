# 피보나찌 수 구하기 (반복적 방법)

# 문제 : n 번째 피보나찌 수를 구하라.
# 입력 : 양수 n
# 출력 : n 번째 피보나찌 수

def fib(n):
    f = [0 for i in range(n + 1)]
    f[1] = 1
    print(f)

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
        print(f)
    return f[n]



# 0 1 1 2 3 5
print(fib(5))


# 중복 계산이 없기 때문에 재귀적 방법보다 더 빠르다.