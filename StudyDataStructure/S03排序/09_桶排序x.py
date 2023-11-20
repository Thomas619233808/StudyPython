# n：桶号
def bucket_sort(nums, n = 100, max_num = 10000):
    # 创建桶
    buckets = [[] for _ in range(n)]
    for var in nums:
        # i表示var放入几号桶
        i = min(var // (max_num // n), n - 1)
        # var放桶里
        buckets[i].append(var)
        # 保持同内顺序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_nums = []
    for buc in buckets:
        sorted_nums.extend(buc)
    return sorted_nums

import random
nums = [random.randint(0, 10000) for _ in range(20)]
print(nums)
nums = bucket_sort(nums)
print(nums)
