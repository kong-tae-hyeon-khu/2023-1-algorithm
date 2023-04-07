# 피보나찌 수 구하기 (재귀적 방법)

# 문제 : n 번째 피보나찌 수를 구하라.
# 입력 : 양수 n
# 출력 : n 번째 피보나찌 수


def fib(n):
    if (n <= 1):
        return n
    
    else:
        return fib(n - 1) + fib(n - 2)
    


# 0 1 1 2 3 5
print(fib(5))

