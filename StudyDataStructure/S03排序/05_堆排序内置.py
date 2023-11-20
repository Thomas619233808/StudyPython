import heapq
import random

nums = list(range(100))
random.shuffle(nums)

print(nums)
heapq.heapify(nums) # 建堆

n = len(nums)
for i in range(n):
    print(heapq.heappop(nums), end=',')
