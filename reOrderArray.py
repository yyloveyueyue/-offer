# -*- coding:utf-8 -*-

class Solution:
    """
    问题描述：输入一个整数数组，使得所有的奇数位于数组前半部分，偶数位于后半部分，且奇数与奇数之间，偶数与偶数之间的相对位置不变
    解题思路：使用sorted函数中的key,key为输入一个排序标准，以奇偶也就是%2是否为0进行排序
    """
    def reOrderArray(self, array):
        # write code here
        return sorted(array,key=lambda c:c % 2,reverse=True)

s = Solution()
print(s.reOrderArray([1,2,3,4,5,6]))