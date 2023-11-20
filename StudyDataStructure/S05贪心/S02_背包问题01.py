'''
0-1背包， 对于一个商品，要么全部拿走，要么不拿，不能拿部分或多次
分数背包：
'''

goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key = lambda  x: x[0]/x[1], reverse=True)
print(goods)
# 商品元组标识 （价格， 重量）
def fractional_backpart(goods, w):
    m = [0 for _ in range(len(goods))]
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
        else:
            m[i] = w / weight
            w = 0
            break
    return m

print(fractional_backpart(goods, 50))