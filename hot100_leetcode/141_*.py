'''
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

key:
判断是否链表是否存在环，可以设置快慢指针，如果没有环，那么快指针会率先到达none，
如果有环，那么快慢指针肯定会相遇，就跟操场跑步一样，快的人总会追上慢的人。

快慢指针：
处理环上的问题，比如环形链表、环形数组等。
需要知道链表的长度或某个特别位置上的信息的时候（倒数第几个，那就先走几步）
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        p = head
        s = set()
        while p is not None:
            if p.val in s:
                return True
            else:
                s.add(p)
            p = p.next
        return False

    def hasCycle2(self, head) -> bool:
        '''
        快慢指针，存储空间为O(1)
        '''
        s = f = head
        while f and f.next:
            s, f = s.next, f.next.next
            if s == f:
                return True
        return False