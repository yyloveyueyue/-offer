# -*- coding:utf-8 -*-

"""
问题描述：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果
解题思路：后序遍历特点，尾元素一定是根节点，同时小于尾元素的是左子树，大于尾元素的是右子树
"""

class Solution:
    def VerifySquenceOfBST(self, sequence):

        if sequence == []:
            return False

        length = len(sequence)
        root = sequence[-1]

        # 找到左子树和右子树分界的序号i

        for i in range(length):
            if sequence[i] > root:
                break

        for j in range(i, length):
            if sequence[j] < root:
                return False

        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        right = True
        if j < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:length-1])

        return (left and right)

def test():
    sequence = [1,5,7,13,16,15,10]
    s = Solution()
    print(s.VerifySquenceOfBST(sequence))

if __name__ == '__main__':
    test()