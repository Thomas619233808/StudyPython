class Solution:
    def topKFrequent(self, nums, k):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        val = list(dic.items())
        val.sort(key = lambda x:x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(val[i][0])
        return res

solution = Solution()
nums = [1,1,1,2,2,3]
res = solution.topKFrequent(nums, 2)
print(res)