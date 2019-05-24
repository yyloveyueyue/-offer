# -*- coding:utf-8 -*-

"""
问题描述：顺时针打印一个矩阵
解题思路：首先判断每一圈开始时的坐标点，是否小于行数的一半且小于列数的一半。
          打印时一行一列打印，除了第一行直接打印，后面都要判断
"""

class Solution:
    def printMatrix(self, matrix):
        if not matrix:
            return

        rows = len(matrix)
        colnums = len(matrix[0])
        start = 0
        result = []
        while start * 2 < rows and start * 2 < colnums:
            self.printMatrixInCircle(matrix, colnums, rows, start, result)
            start += 1
        return result


    def printMatrixInCircle(self, matrix, colnums, rows, start, result):
        endX = colnums - 1 - start
        endY = rows - 1 -start

        # 从左往右打印一行
        for i in range(start, endX + 1):
            result.append(matrix[start][i])

        # 从上往下打印一列
        if start < endY:
            for i in range(start + 1, endY + 1):
                result.append(matrix[i][endX])

        # 从右往左打印一行
        if start < endY and start < endX:
            for i in range(endX - 1, start - 1, -1):
                result.append(matrix[endY][i])

        # 从下往上打印一行
        if start < endX and start < endY - 1:
            for i in range(endY - 1, start , -1):
                result.append(matrix[i][start])