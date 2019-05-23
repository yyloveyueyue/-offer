# -*- coding:utf-8 -*-

class Solution:
    """
    问题描述，一只青蛙一次可以跳上1级台阶或二级台阶，问跳上一个n级台阶有多少种情况
    解题思路：考虑跳上n级台阶，可考虑跳到n-1和n-2台阶
    """

    def jumpFloor(self, number):
        # write code here
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                tempArray[(i+1)%2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1)%2]

s = Solution()