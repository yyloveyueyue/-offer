# -*- coding:utf-8 -*-

"""
问题描述： 输入一颗二叉搜索树，将改二叉搜索树转换成一个排序的双向链表，要求不能创建任何
           新的节点，只能调整树中结点指针的指向
解题思路： 左右子树分治，中序遍历，递归实现。根据二叉搜索树的特点，根节点的左边连接左子树最右的节点
           根节点的右边连接右子树最左边的节点
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None

        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        if left:
            while left.right:
                left = left.right

            pRootOfTree.left = left
            left.right = pRootOfTree

        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        if right:
            while right.left:
                right = right.left
            pRootOfTree.right = right
            right.left = pRootOfTree

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree


root = TreeNode(20)
a1 = TreeNode(10)
a2 = TreeNode(30)
a11 = TreeNode(5)
a12 = TreeNode(15)
a21 = TreeNode(25)
a22 = TreeNode(35)
a111 = TreeNode(1)
a112 = TreeNode(6)
a121 = TreeNode(13)
a122 = TreeNode(17)
a211 = TreeNode(22)
a212 = TreeNode(27)
a221 = TreeNode(33)
a222 = TreeNode(37)
root.left = a1
root.right = a2
a1.left = a11
a1.right = a12
a2.left = a21
a2.right = a22
a11.left = a111
a11.right = a112
a12.left = a121
a12.right = a122
a21.left = a211
a21.right = a212
a22.left = a221
a22.right = a222

s = Solution()
result = s.Convert(root)
print(result.val)

