class Solution:
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        x = 0
        y = col - 1
        # 使用每行的最后一列作为比较值
        while x < row and y >= 0:
            # 如果比较值大于目标值，则y坐标往左移
            if matrix[x][y] > target:
                y -= 1
            # 如果比较值小于目标值，则直接从下一行开始对比
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False

    def searchMatrix2(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = (left + right) // 2
            x = mid // col
            y = mid % col
            midval = matrix[x][y]
            if midval == target:
                return True
            elif midval < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


solution = Solution()
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 3
target1 = 21
res = solution.searchMatrix(matrix, target)
res1 = solution.searchMatrix(matrix, target1)
res3 = solution.searchMatrix2(matrix, target)
res4 = solution.searchMatrix2(matrix, target1)
print(res)
print(res1)
print("---二分查找---")
print(res3)
print(res4)

