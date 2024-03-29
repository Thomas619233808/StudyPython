# 假合并方法
def findmid(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    lens = len1 + len2
    # 左右指针
    left, right = -1, -1
    # 数组的开始指针
    star1, star2 = 0, 0
    for i in range(lens // 2 + 1):
        # 每次循环之前把right赋值给left，将上一轮的中位数存给left，然后用right找下一轮的中位数
        left = right
        # star1移动的条件，nums1 还有元素，nums1的值小于nums2，或 nums2没有元素
        if star1 < len1 and (star2 >= len2 or nums1[star1] < nums2[star2]):
            right = nums1[star1]
            star1 += 1
        else:
            right = nums2[star2]
            star2 += 1
    if (lens % 2) == 0:
        return (left + right) / 2.0
    else:
        return right

# 第K小数
# def findmid2(nums1, nums2):

nums1 = [1, 3]
nums2 = [2, 4]
print(findmid(nums1, nums2))
