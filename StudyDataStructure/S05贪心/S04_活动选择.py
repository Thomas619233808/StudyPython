'''
假设有n个活动，有些活动要占用同一片场地， 而场地某时刻只能提供一个活动使用
活动开始和结束时间（s1,f1)
'''

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 保证活动为结束时间排序
activities.sort(key = lambda x:x[1])
# print(activities)

def activity_selection(nums):
    res = [nums[0]]
    for i in range(1, len(nums)):
        # 活动的开始时间大于等于上个入选的活动结束时间，则不冲突
        if nums[i][0] >= res[-1][1]:
            res.append(nums[i])
    return res

print(activity_selection(activities))