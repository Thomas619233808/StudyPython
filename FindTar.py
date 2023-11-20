def search_range(nums, target):
    n = len(nums)
    start = end = -1
    # 二分查找目标值的起始下标
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            start = mid
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # 如果未找到目标值，直接返回[-1, -1]
    if start == -1:
        return [-1, -1]

    # 二分查找目标值的结束下标
    left, right = start, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            end = mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return [start, end]

nums = [1, 2, 2, 3, 4, 4, 4, 5]
target = 4
res = search_range(nums, target)
print(res)