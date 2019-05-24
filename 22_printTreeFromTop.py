# -*- coding:utf-8 -*-

"""
问题描述，从上往下打印一个二叉树，同层节点从左往右
解题思路，使用一个队列，若节点有子节点，就把子节点放到队列的末尾
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintTree(self, root):
        if root is None:
            return []

        queue = []
        result = []

        queue.append(root)
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)

        return result

def test():
    root = TreeNode(1)
    a1 = TreeNode(2)
    a2 = TreeNode(3)
    a11 = TreeNode(4)
    a12 = TreeNode(5)
    a22 = TreeNode(6)
    a112 = TreeNode(7)
    a221 = TreeNode(8)
    root.left = a1
    root.right = a2
    a1.left = a11
    a1.right = a12
    a2.right = a22
    a11.right = a112
    a22.left = a221

    s = Solution()
    result = s.PrintTree(root)
    print(result)

if __name__ == '__main__':
    test()