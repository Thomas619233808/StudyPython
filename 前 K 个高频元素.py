'''
给定一个整数数组 nums 和一个整数 k ，请返回其中出现频率前 k 高的元素。可以按 任意顺序 返回答案。
'''

def topKFrequent(nums, k):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    val = list(dic.items())
    val.sort(key=lambda x: x[1], reverse=True)
    res = []
    for i in range(k):
        res.append(val[i][0])
    return res

nums = [1,1,1,2,2,3]
k = 2
res = topKFrequent(nums, k)
print(res)