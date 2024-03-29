import heapq

def find_top_10_largest(data):
    min_heap = []
    # 遍历数据集
    for num in data:
        if len(min_heap) < 10:
            # heappush构建小根堆，存在min_heap， 添加的新元素是num
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            # heapreplace删除堆中的最小值，并用新的值取代它，并重新构建小根堆
            heapq.heapreplace(min_heap, num)

    # 将堆中的元素从小到大排列
    top_10_largest = sorted(min_heap)
    return top_10_largest

# 示例数据集，假设是一亿个数
huge_dataset = [i for i in range(1, 100000001)]

# 调用函数找到最大的10个数
result = find_top_10_largest(huge_dataset)

# 打印结果
print(result)
