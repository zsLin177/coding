'''
环形链表
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        不用快慢指针
        '''
        hash_set = set()
        while head:
            if head in hash_set:
                return head
            else:
                hash_set.add(head)
            head = head.next
        return None

    def detectCycle2(self, head: ListNode) -> ListNode:
        '''
        快慢指针
        数学推导：
        慢指针第一圈没跑完就会和快指针相遇, 快慢指针相遇的时候, 
        用另一个指针从head和slow一起走，最终会在入口相遇.
        '''
        slow = fast = head
        while fast:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if fast == slow:
                p = head
                while p != slow:
                    slow = slow.next
                    p = p.next
                return p
        return None
