# -*- coding:utf-8 -*-

class Solution:
    """
    问题描述：有一个排序好的二维数组array，在其中查找target
    解题思路：先看每一行的最后一个数，比taget大，列号j-1,否则，行号i+1
    """
    @classmethod
    def find(cls, array, target):

        if array == []:
            return -1
        num_row = len(array)
        num_col = len(array[0])

        # 定义开始查找的行列号
        row = 0
        col = num_col - 1
        while col >= 0 and row < num_row:
            if array[row][col] == target:
                return row, col
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return -1



# sol = Solution()
# array = [[1,3,5],[7,10,13]]
# print(sol.find(array, 0))

array = [[1,3,5],[7,10,13]]
print(Solution.find(array, 0))

