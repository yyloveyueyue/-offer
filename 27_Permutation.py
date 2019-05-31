# -*- coding:utf-8 -*-

"""
问题描述：输入一个字符串，按字典序打印出该字符串中字符的所有排序，例如输入字符串，输出a,b,c的所有可能排序
解题思路：固定一个元素，求出后面所有字符的排列
"""


class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(0,len(charList)):
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            temp = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for j in temp:
                pStr.append(charList[i] + j)

        return pStr

ss = 'a'
s = Solution()
print(s.Permutation(ss))