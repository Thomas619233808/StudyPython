'''
给定两个序列x，y，求x，y的长度最大的公共子序列
'''

def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]

def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # 1左上 2上 3左
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] =c[i][j - 1]
                b[i][j] = 3
    return c[m][n], b

def lcs_trackback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1: # 来自左上 则匹配
            res.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(res))

x = 'ABCBDAB'
y = 'BDCABA'
print(lcs_trackback(x, y))
