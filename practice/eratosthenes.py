import math

def sieve_of_eratosthenes(n):

    primes = [True] * (n + 1)
    # 0 과 1은 소수 취급 X
    primes[0] = False
    primes[1] = False

    # 2 ~ n 까지 True
    print(primes)


    for i in range(2, math.floor((math.sqrt(n)))): # 2 부터 i의 제곱근까지.
        
        if primes[i]: # Check Mark

            for j in range(i*i, n+1):

                if (j %  i == 0): # j 가 i 의 배수이면,
                    primes[j] = False

                
    result = []


    for num in range(2, n + 1):
        if (primes[num]):
            result.append(num)
    
    return result




print(sieve_of_eratosthenes(30))
