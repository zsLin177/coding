'''
单链表插入排序
要注意的东西实在是太多了,细节很重要，最好做的时候画图
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        new_head = head
        p = head.next
        new_head.next = None
        pre_new_head = ListNode(-10000, new_head)
        tail = new_head
        while p:
            if p.val >= tail.val:
                tail.next = p
                tmp = p.next
                tail = p
                tail.next = None
                p = tmp
            else:
                pre = pre_new_head
                inner_p = pre_new_head.next
                while inner_p and p.val >= inner_p.val:
                    pre = pre.next
                    inner_p = inner_p.next
                pre.next = p
                tmp = p.next
                p.next = inner_p
                p = tmp
                if inner_p is None:
                    tail = pre.next
        return pre_new_head.next
