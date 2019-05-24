# -*- coding:utf-8 -*-

"""
问题描述：输入一个链表，输出该链表中倒数第k个节点
解题思路：设置两个指针A和B,一开始都指向头结点，先让A走k-1步到达第K个节点，接下来AB一起走，知道A走完，
          这样A和B继续走了n-k步，B就指向了倒数第K个节点
"""

# 定义一个链表结构
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <= 0 :
            return None

        pAhead = head
        pBhead = head

        for i in range(k - 1):
            if pAhead.next != None:
                pAhead = pAhead.next
            else:
                return None
        while pAhead.next != None:
            pAhead = pAhead.next
            pBhead = pBhead.next
        return pBhead

