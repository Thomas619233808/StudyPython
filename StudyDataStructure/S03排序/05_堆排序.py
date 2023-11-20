'''
    堆的性质：一棵完全二叉树，每个节点大于等于其子节点的值，为最大堆，反之为最小堆
    堆堆父子节点列表下标的关系为：父节点 = 子节点 * 2 + 1
    堆排序：
    1.先构造堆
    2.得到堆顶元素，为最大值
    3.去掉堆顶元素，将最后一个元素放置堆顶，调整堆使其有序
    4.堆顶为第二大元素
    5.重复步骤3，直到堆清空
'''

def sift(nums, root, end):
    """
    :param nums:
    :param root: 堆的根节点位置
    :param end: 堆的最后一个元素
    :return:
    """
    i = root # 最开始指向根节点
    j = 2 * i + 1 # 指向左子节点
    tmp = nums[root] # 暂存堆顶
    while j <= end: # 位置j有数
        if j + 1 <= end and  nums[j + 1] > nums[j]: # 右孩子大
            j = j + 1 # j指向右孩子
        if nums[j] > tmp: # 如果左孩子比根节点大
            nums[i] = nums[j] # 则左孩子升至根节点
            i = j  # 往下一层
            j = 2 * i + 1 # 重新定位i的左孩子节点
        else: # tmp比左孩子大，把tmp放回i的位置
            nums[i] = tmp # 把tmp放到某一级根节点
            break
    else:
        nums[i] = tmp # 把tmp放到叶子节点

def heap_sort(nums):
    n = len(nums)
    # 从最末的最小堆开始建堆，该小堆的根节点为 (子节点 - 1)//2
    # 子节点坐标为n - 1，得根节点坐标为 (n - 2)//2
    for i in range((n - 2) // 2, -1, -1):
        # i指向当前调整的根节点
        # end一直指向整个大堆末尾，不用更新，保证不越界即可
        sift(nums, i, n - 1)
    # 堆建立完成

    for i in range(n - 1, -1, -1):
        # i 一直指向当前堆的最后一个元素
        nums[0], nums[i] = nums[i], nums[0]
        # 首尾交换之后，root不再是最大值，i指针前移，需要重新建堆
        # 重建堆之后，再次交换首尾元素
        sift(nums, 0, i - 1) # i - 1是新的end


nums = [i for i in range(10)]
import random
random.shuffle(nums)
print(nums)
heap_sort(nums)
print(nums)


