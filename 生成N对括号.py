def generate_parenthesis(n):
    res = []
    dfs(res, "", 0, 0, n)
    return res

def dfs(res, cur, leftnum, rightnum, n):
    # 终止条件，当左右括号用完之后，将它们添加到列表
    if len(cur) == 2 * n:
        res.append(cur)
        return

    # 添加左括号的条件：当左括号数量小于n，添加左括号
    if leftnum < n:
        dfs(res, cur + "(", leftnum + 1, rightnum, n)

    # 添加右括号的条件：当右括号数量小于左括号数量，添加右括号
    if rightnum < leftnum:
        dfs(res, cur + ")", leftnum, rightnum + 1, n)

print(generate_parenthesis(3))