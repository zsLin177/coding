'''
删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

链表 倒数第几个 快慢指针，快指针先走几步
'''

from common import *

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        slow = fast = head
        while n:
            fast = fast.next
            n -= 1
        if fast is None:
            return head.next
        while fast:
            pre = slow
            slow = slow.next
            fast = fast.next
        pre.next = slow.next
        return head
