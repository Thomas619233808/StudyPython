def insert_sort(nums):
    for i in range(1, len(nums)): # i表示摸牌的下标
        pre = i - 1 # 手里的牌最右边那张的下标
        cur = nums[i] # 此时摸的牌
        while pre >= 0 and nums[pre] > cur:
            # 摸牌比手牌小
            # 手牌每张右移一格
            nums[pre + 1] = nums[pre]
            # 继续比较手牌
            pre -= 1
        # 摸牌比手牌大，直接放右边
        nums[pre + 1] = cur
    return nums

nums = [6, 7, 1, 2, 3, 5, 8, 4]
print(nums)
res = insert_sort(nums)
print(res)