def printArray(array):
    if not array:return []
    left = 0
    right = len(array[0]) - 1
    top = 0
    but = len(array) - 1
    res = []

    while True:
        # 从左往右打印
        for i in range(left, right + 1):
            res.append(array[top][i])
        top += 1
        if top > but: break

        # 从上往下打印
        for i in range(top, but + 1):
            res.append(array[i][right])
        right -= 1
        if left > right: break

        # 从右往左打印
        for i in range(right, left - 1, -1):
            res.append(array[but][i])
        but -= 1
        if top > but: break

        # 从下往上打印
        for i in range(but, top - 1, -1):
            res.append(array[i][left])
        left += 1
        if left > right: break

    return res

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
res = printArray(array)
print(res)
