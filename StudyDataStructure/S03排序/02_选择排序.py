# #简单版本
# def select_sort(nums):
#     new_nums = []
#     for i in range(len(nums)):
#         min_val = min(nums)
#         new_nums.append(min_val)
#         nums.remove(min_val)
#     return new_nums
'''
每次遍历找到最小的元素，放到list前面
下一次遍历起点右移一位
'''
# O(n^2)
def select_sort(nums):
    for i in range(len(nums) - 1):
        min_ind = i # 记录无序序列最小值下标，也可以是第i次遍历
        for j in range(i, len(nums)):
            if nums[j] < nums[min_ind]:
                min_ind = j
        # 与无序序列第一个交换
        nums[i], nums[min_ind] = nums[min_ind], nums[i]
        print(nums)
    return nums

nums = [6, 7, 1, 2, 3, 5, 8, 4]
print(nums)
res = select_sort(nums)
print(res)