class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
            return 0
        left = right = 0
        maxlen = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                right = i
            else:
                if right - left + 1 > maxlen:
                    maxlen = right - left + 1
                left = right = i
        return max(maxlen, right - left + 1)

    def digui(self, nums):
        if not nums:
            return 0
        n = len(nums)
        # dp[i] 表示第i个位置的连续递增元素个数
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

solution = Solution()
nums = [1,3,5,4,7]
res = solution.findLengthOfLCIS(nums)
res1 = solution.digui(nums)
print(res)
print(res1)
