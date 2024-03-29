'''
写一个排序函数，根据输入参数asc或desc决定排序的类型是升序还是降序
'''
class Solution:
    def SortList(self, nums, sortType):
        self.QuickSort(nums, 0, len(nums) - 1, sortType)
        return nums

    def Partition(self, nums, left, right, sortType):
        # 基准值选为列表最后一个元素
        tmp = nums[right]
        # i表示比基准值小的最后一个元素的下标
        i = left - 1
        for j in range(left, right):
            # 如果j指向元素小于基准值且排序类型为升序 或 j指向元素大于基准值且排序类型为降序
            # 更新i指针后，交换i、j指向的元素
            if (nums[j] < tmp and sortType == "asc") or (nums[j] > tmp and sortType == "desc"):
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        # 将基准值放到对应位置
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        # 返回基准值的下标
        return i + 1

    def QuickSort(self, nums, left, right, sortType):
        if left < right:
            tmp = self.Partition(nums, left, right, sortType)
            self.QuickSort(nums, left, tmp - 1, sortType)
            self.QuickSort(nums, tmp + 1, right, sortType)


nums = [20,15,33,0,8,46,20,17,62,16]
print("Origin List:", nums)
s = Solution()
print("Asc List", s.SortList(nums.copy(), "asc"))
print("Desc List", s.SortList(nums.copy(), "desc"))