# -*- coding:utf-8 -*-

"""
问题：输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径，路径
      定义为从数的根节点开始往下一直到叶结点形成一条路径，返回值的list中，数组长度大的靠前。
思路：用前序遍历的方式访问节点
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root or root.val > expectNumber:
            return []

        # if not root.left and not root.right and root.val == expectNumber:
        #     return [[root.val]]
        if root.val == expectNumber:
            return [[root.val]]
        else:
            expectNumber -= root.val
            left = self.FindPath(root.left, expectNumber)
            right = self.FindPath(root.right, expectNumber)

            result = [[root.val]+ i for i in left]
            for i in right:
                result.append([root.val] + i)

        return sorted(result, key=lambda x: -len(x))

def test():
    root = TreeNode(1)
    a1 = TreeNode(2)
    a2 = TreeNode(6)
    a11 = TreeNode(4)
    a12 = TreeNode(5)
    a22 = TreeNode(6)
    a112 = TreeNode(7)
    a221 = TreeNode(8)
    a111 = TreeNode(9)
    a121 = TreeNode(11)
    a122 = TreeNode(12)
    a222 = TreeNode(10)
    root.left = a1
    root.right = a2
    a1.left = a11
    a1.right = a12
    a2.right = a22
    a11.left = a111
    a11.right = a112
    a22.left = a221
    a12.left = a121
    a12.right = a122
    a22.right = a222

    s = Solution()
    result = s.FindPath(root, 7)
    print(result)

if __name__ == '__main__':
    test()