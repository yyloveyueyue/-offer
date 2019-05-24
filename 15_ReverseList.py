# -*- coding:utf-8 -*-

"""
问题描述：输入一个链表，将其翻转
解题思路：3个指针，一个指向当前操作的节点，2个指向改节点的前后
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class solution:
    def ReverseList(self, head):
        pReversedHead = None
        pNode = head
        pPrev = None
        pNext = None
        while pNode != None:
            pNext = pNode.next
            if pNext == None:
                pReversedHead = pNode

            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead

def test():
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    a5 = ListNode(5)
    a6 = ListNode(6)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    s = solution()
    a_rev = s.ReverseList(a1)
    while a_rev.val != None:
        print(a_rev.val)
        a_rev = a_rev.next
        if a_rev == None:
            break

if __name__ == '__main__':
    test()