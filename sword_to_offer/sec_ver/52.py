# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLen(self, head):
        if head is None:
            return 0
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        return length


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = self.getLen(headA)
        len_b = self.getLen(headB)
        if len_a > len_b:
            long = headA
            short = headB
            step = len_a - len_b
        else:
            long = headB
            short = headA
            step = len_b - len_a
        
        while step > 0:
            long = long.next
            step -= 1

        while long and short:
            if long == short:
                return long
            long = long.next
            short = short.next
        return None
        
