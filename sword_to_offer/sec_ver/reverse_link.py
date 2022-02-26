'''
再来绕一绕反转链表
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head: ListNode):
        pre = None
        p = head
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre
        