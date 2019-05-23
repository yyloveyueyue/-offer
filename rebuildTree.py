# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rebuildTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        root.left = self.rebuildTree(pre[1:i + 1], tin[:i])
        root.right = self.rebuildTree(pre[i + 1:], tin[i+1:])
        return root


sol =Solution()
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
root = sol.rebuildTree(pre, tin)
print(root)