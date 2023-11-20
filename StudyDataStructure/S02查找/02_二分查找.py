# 时间复杂度 O(logn)
def binary_search(nums, value):
    right = len(nums) - 1
    left = 0
    nums.sort()
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return mid
        elif nums[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

nums = [4, 3, 2, 5, 8, 10]
res = binary_search(nums, 5)
print(res)
