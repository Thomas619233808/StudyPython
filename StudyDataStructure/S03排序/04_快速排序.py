def partition(nums, left, right):
    tmp = nums[left]
    while left < right:
        # 从右往左找比tmp小的数
        while left < right and nums[right] >= tmp:
            right -= 1  # 右指针往左
        nums[left] = nums[right] # 找到比right小的数，和left交换
        # 从左往右找比tmp大的数
        while left < right and nums[left] <= tmp:
            left += 1  # 左指针往右走
        nums[right] = nums[left] # 找到比left大的数，和right交换
    nums[left] = tmp
    return left

def quick_sort(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)


nums = [6, 7, 1, 2, 3, 5, 8, 4]
print(nums)
quick_sort(nums, 0, len(nums) - 1)
print(nums)