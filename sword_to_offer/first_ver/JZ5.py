# -*- coding:utf-8 -*-
# 这题让用两个栈来做队列，在python中根本没有必要，python的list类就行了，在头部pop(0)，在尾部append，应该是针对c++那种才有意义
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if(len(self.stack2)>0):
            return self.stack2.pop(0)
        else:
            self.stack2 += self.stack1
            self.stack1 = []
            return self.stack2.pop(0)