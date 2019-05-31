# -*- coding:utf-8 -*-

"""
问题描述：输入一个复杂链表（每个节点有节点值，两个指针，一个指向下一个节点，一个指向任意节点，
        返回结果为复制后复杂链表的Head
解题思路：复制原始链表的每个节点，将复制的节点链接在原始节点的后面，然后复制random指针，最后拆分
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, pHead):
        if not pHead:
            return None
        pNode = pHead

        # 复制
        while pNode:
            pClone = RandomListNode(pNode.label)
            pClone.next = pNode.next
            pNode.next = pClone
            pNode = pClone.next

        pNode = pHead

        # 复制random指针
        while pNode:
            pClone = pNode.next
            if pNode.random != None:
                pClone.random = pNode.random.next
            pNode = pClone.next

        pNode = pHead
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneHead.next
        pNode = pNode.next

        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next

        return pCloneHead