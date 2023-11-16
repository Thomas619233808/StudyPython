'''
n个人随机瓜分一个红包，每个人至少可以拿0.01元
'''
import random
def divide_money(n, m):
    # 将金额扩大100倍，以分为单位进行计算
    total = int(m * 100)
    remaining = total
    result = []
    for i in range(n - 1):
        # 随机分配金额，每个人至少获得1分，最多不超过剩余的平均值
        share = random.randint(1, remaining - (n - i - 1))
        result.append(share / 100)  # 将得到的金额转换为元
        remaining -= share
    result.append(remaining / 100)  # 最后一个人得到剩余的金额
    return result

n = 2
m = 0.02
res = divide_money(n, m)
print(res)