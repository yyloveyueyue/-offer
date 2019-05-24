# -*- coding:utf-8 -*-

"""
问题描述：给定2个二叉树AB，判断B是否为A的子树，默认空树不是任意一个数的子树
解题思路：现在A中找到一个叶子节点值等于B的根节点，在看此节点下
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solutin:
    def HasSubTree(self, proot1, proot2):
        result = False
        if proot1 != None and proot2 != None:
            if proot1.val == proot2.val:
                result = self.DoesTree1hasTree2(proot1, proot2)
            if not result:
                result = self.HasSubTree(proot1.left, proot2)
            if not result:
                result = self.HasSubTree(proot1.left, proot2)



        return result


    def DoesTree1hasTree2(self, proot1, proot2):
        if proot2 == None:
            return True
        if proot1 == None:
            return False
        if proot1.val != proot2.val:
            return False

        return self.DoesTree1hasTree2(proot1.left, proot2.left) and self.DoesTree1hasTree2(proot1.right, proot2.right)