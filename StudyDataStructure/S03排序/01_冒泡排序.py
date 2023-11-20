# O(n^2)
def bubble_sort(nums):
    n = len(nums) - 1
    for i in range(n):
        # 优化：加入交换标识，如果未发生交换则说明已经排序
        exchange = False
        for j in range(n - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                exchange = True
        print(nums)
        if not exchange:
            return
    return nums


nums = [9, 8, 7, 1, 2, 3, 4, 5, 6]
print(nums)
res = bubble_sort(nums)
print(res)