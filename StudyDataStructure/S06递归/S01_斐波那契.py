def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)

# 动态规划（DP）思想：推导式、最优子结构
def fib_no_rec(n):
    f = [0, 1, 1]
    if n > 2:
        for i in range(n - 2):
            num = f[-1] + f[-2]
            f.append(num)
        return f[n]

print(fib_no_rec(100))
