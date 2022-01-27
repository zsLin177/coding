'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
'''

from common import *

class Solution:
    '''
    merge 
    '''
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        head_c = ListNode(-1)
        p_c = head_c
        p_a = list1
        p_b = list2
        while (p_a is not None) and (p_b is not None):
            if p_a.val <= p_b.val:
                p_c.next = p_a
                p_a = p_a.next
            else:
                p_c.next = p_b
                p_b = p_b.next
            p_c = p_c.next

        if p_a is None and p_b is not None:
            p_c.next = p_b
        elif p_a is not None and p_b is None:
            p_c.next = p_a
        return head_c.next

