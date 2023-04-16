def digit_len(n):
    n_len = 0
    while (n != 0):
        n = n // 10
        n_len += 1
    return n_len


# 큰 정수 u & v
def prod(u, v):
    # u 의 자리수, v 의 자리수
    u_len = digit_len(u)
    v_len = digit_len(v)
    n = max(u_len, v_len)

    if (u == 0 or v == 0):
        return 0
    
    elif n <= 3:
        return u * v

    else :
        m = n // 2

        x = u // (10**m)
        y = u % (10**m)

        w = v // (10**m)
        z = v % (10**m)

        return prod(x , w) * (10 ** (2*m)) + (prod(x,z) + prod(w,y)) * 10**m + prod(y,z)
    

print(prod(5682, 200))

# Ver 2.
def prod2(u, v):  # 덧셈 횟수는 늘어나지만, 곱셈 횟수는 감소. 
    # u 의 자리수, v 의 자리수
    u_len = digit_len(u)
    v_len = digit_len(v)
    n = max(u_len, v_len)

    if (u == 0 or v == 0):
        return 0
    
    elif n <= 3:
        return u * v

    else :
        m = n // 2

        x = u // (10**m)
        y = u % (10**m)

        w = v // (10**m)
        z = v % (10**m)

        r = prod2(x+y, w+z)
        p = prod2(x, w)
        q = prod(y,z)

        return p * 10 ** (2*m) + (r-p-q)*10**m + q
    
print(prod2(5682, 200))