# -*- coding:utf-8 -*-

class Solution:
    """
    问题描述，输入一个整数，输出该数的二进制表示中1的个数，其中复数用补码表示
    解题思路，每个非零整数n与n-1进行按位与运算，n的二进制中，最右边的1就会变成0，乘几次n变为0,就是有几个1
    """
    @classmethod
    def Numberof1(cls, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count


print(Solution.Numberof1(5))