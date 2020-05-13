def mult(a, b):
    if b == 1:
        return a
    elif a == 1:
        return b
    else:
        return a + mult(a, b - 1)

print(mult(1, 3))

def fib_memorize(n, d):
    if n in d:
        return d[n] 
    else:
        ans = fib_memorize(n - 1, d) + fib_memorize(n - 2, d) 
        d[n] = ans 
        return ans

base_case = {0: 1, 1: 1}

print(fib_memorize(12, base_case))