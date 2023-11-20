def sift(nums, low, high):
    i = low
    j = 2 * i + 1
    tmp = nums[low]
    # 小根堆
    while j <= high :
        if j + 1 <= high and nums[j + 1] < nums[j]:
            j = j + 1
        if nums[j] < tmp:
            nums[i] = nums[j]
            i = j
            j = 2 * i + 1
        else:
            break
    nums[i] = tmp

def topk(nums, k):
    heap = nums[0: k]
    # 前k项建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 遍历nums剩余元素，如果比堆顶大则放入
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heap[0] = nums[i]
            sift(heap, 0, k - 1)
    # 输出
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap

import random
nums = list(range(100))
random.shuffle(nums)
print(topk(nums, 10))
