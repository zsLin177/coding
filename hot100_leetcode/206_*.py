'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''
from common import *

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        非递归
        '''
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        '''
        递归
        '''
        if not head or not head.next:
            return head
        new_head = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new_head
                


    

