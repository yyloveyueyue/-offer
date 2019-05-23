# -*- coding:utf-8 -*-

class Solution:
    """
    问题描述：用2个栈实现队列的pop,push操作，提示，栈是先进后出，队列是先进先出
    解题思路：2个栈stack1和stack2，执行push操作，只用往stack1中push，pop时Stack2
    对于Python的list,append和pop其实相当于栈的进出，因为pop是默认指向列表末尾的，可以用pop(0)弹出第一个元素，模拟队列，但不符合题意
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return "error"
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

