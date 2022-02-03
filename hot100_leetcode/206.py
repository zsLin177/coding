'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''
from common import *

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp = []
        p = head
        while p:
            tmp.append(p)
            p = p.next
        if len(tmp) == 0:
            return None
        new_head = tmp[-1]
        idx = len(tmp)-1
        while idx >= 0:
            if idx > 0:
                tmp[idx].next = tmp[idx-1]
            else:
                tmp[idx].next = None
            idx -= 1
        return new_head

