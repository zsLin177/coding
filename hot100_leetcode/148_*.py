'''
单链表的merge排序
自底向上
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:

    def reverse(self, head):
        pre = head
        curr = head.next
        pre.next = None
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return pre

    def sortList(self, head):
        def merge(head1, head2):
            dummpy = ListNode(-1)
            p, p1, p2 = dummpy, head1, head2
            while p1 and p2:
                if p1.val <= p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
                p.next = None
            if p1:
                p.next = p1
            elif p2:
                p.next = p2
            return dummpy.next

        p = head
        if not p:
            return p
        length = 0
        while p:
            length += 1
            p = p.next
        
        sub_length = 1
        dummpy = ListNode(-1, head)
        while sub_length < length:
            pre, curr = dummpy, dummpy.next
            while curr:
                head1 = curr
                for i in range(1, sub_length):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, sub_length):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                merged = merge(head1, head2)
                pre.next = merged
                while pre.next:
                    pre = pre.next
                curr = succ
            sub_length += sub_length
        return dummpy.next

        
if __name__ == "__main__":
    from common import *
    s = Solution()
    head = build_link([1,2,3])[0]
    print_link([s.reverse(head)])
    