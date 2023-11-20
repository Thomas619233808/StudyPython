'''
    首先取一个整数d1 = n/2，将所有元素分为d1个组，每组相邻元素间距为d1，在各组进行插入排序
    取第二个证书d2 = d1/2，重复上述步骤，知道d1=1
'''

def insert_sort_gap(nums, gap):
    for i in range(gap, len(nums)):
        cur = nums[i]
        pre = i - gap
        while pre >= 0 and nums[pre] > cur:
            nums[pre + gap] = nums[pre]
            pre -= gap
        nums[pre + gap] = cur

def shell_sort(nums):
    d = len(nums) // 2
    while d >= 1:
        insert_sort_gap(nums, d)
        d //= 2

nums = list(range(10))
import random
random.shuffle(nums)
print(nums)
shell_sort(nums)
print(nums)