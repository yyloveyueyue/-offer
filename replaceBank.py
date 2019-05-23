# -*- coding:utf-8 -*-

class Solution:
    """
    问题描述：将一个字符串中的空格全部替换为%20
    解题思路：设置两个指针，从旧字符串和新字符串的末尾开始往前移动
    """
    @classmethod
    def replaceBank(cls, s):
        # s表示原字符串
        if len(s) <= 0 or s == None or not isinstance(s, str):
            return ''

        # 统计空格数
        numbank = 0
        for i in s:
            if i == ' ':
                numbank += 1

        newStrLen = len(s) + numbank * 2
        newList = newStrLen * ['0']

        indexoforigin = len(s) - 1
        indexofnew = len(newList) - 1

        while indexoforigin >= 0 and indexofnew >= indexoforigin:
            if s[indexoforigin] == ' ':
                newList[indexofnew -2 : indexofnew + 1] = ['%','2','0']
                indexofnew -= 3
                indexoforigin -= 1
            else:
                newList[indexofnew] = s[indexoforigin]
                indexofnew -= 1
                indexoforigin -= 1

        newStr = ''.join(newList)

        return newStr


s = 'abc abc  abc'
print(Solution.replaceBank(s))