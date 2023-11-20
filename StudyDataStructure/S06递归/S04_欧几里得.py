'''
欧几里得算法
求最大公约数
'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd2(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

print(gcd(12, 16))