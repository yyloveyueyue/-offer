# -*- coding:utf-8 -*-

"""
问题描述：合并两个单调递增的链表，合并后的链表也是单调不减的
解题思路：设置一个指针，从2个链表的头结点开始比较，指针指向值小的，并继续循环比较next
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        pMergeHead = None
        if pHead1.val < pHead2.val :
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)
        return pMergeHead


def test():
    a1 = ListNode(1)
    a2 = ListNode(3)
    a3 = ListNode(5)
    a4 = ListNode(9)
    a5 = ListNode(11)
    a6 = ListNode(13)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6
    b1 = ListNode(2)
    b2 = ListNode(4)
    b3 = ListNode(6)
    b4 = ListNode(7)
    b5 = ListNode(8)
    b6 = ListNode(9)
    b1.next = b2
    b2.next = b3
    b3.next = b4
    b4.next = b5
    b5.next = b6
    s = solution()
    a_rev = s.Merge(a1, b1)
    while a_rev.val != None:
        print(a_rev.val)
        a_rev = a_rev.next
        if a_rev == None:
            break

if __name__ == '__main__':
    test()