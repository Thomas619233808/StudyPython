'''
    分解：将列表越分越小，直到分成一个元素
    终止条件：一个元素是有序的
    合并：将两个有序的列表归并，列表越来越大
'''
# O(nlogn)

def merger(nums, left, mid, right):
    i = left
    j = mid + 1
    numstmp = []
    # 合并两个序列
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            numstmp.append(nums[i])
            i += 1
        else:
            numstmp.append(nums[j])
            j += 1
    # 将较长序列直接加入
    while i <= mid:
        numstmp.append(nums[i])
        i += 1
    while j <= right:
        numstmp.append(nums[j])
        j += 1
    nums[left:right + 1] = numstmp

# nums = [2, 4, 5, 7, 1, 3, 6, 8]
# merger(nums, 0, 3, 7)
# print(nums)

def merge_sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2
        # 将左边序列排序
        merge_sort(nums, left, mid)
        # 将右边序列排序
        merge_sort(nums, mid + 1, right)
        # 合并左右序列
        merger(nums, left, mid, right)

nums = list(range(10))
import random
random.shuffle(nums)
print(nums)
merge_sort(nums, 0, len(nums) - 1)
print(nums)