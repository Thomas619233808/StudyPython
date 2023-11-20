'''
给出钢条的出售价格与钢条长度，求总长度为n的如何切割钢条得到最大收益
'''

# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
def cut_rod(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod(p, i) + cut_rod(p, n - i))
        return res

print(cut_rod(p, 9))

def cut_rod_2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_2(p, n - i))
        return res

print(cut_rod_2(p, 9))

# 自顶向下
def cut_rod_dp(p, n):
    dp = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + dp[i - j])
        dp.append((res))
    return dp[n]

print(cut_rod_dp(p, 9))

# 重构解
def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0 # 价格的最大值
        res_s = 0 # 价格最大值方案对应左边不切割的长度
        for j in range(1, i + 1):
            res_r = p[j] + r[i - j]
            res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s

r, s = cut_rod_extend(p, 9)
print(s)
