'''
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

普通思路:
让长度长的先走多的步数，然后再一起走，直到结束或者遇到首个相同的。

nb思路:
指针 A 先遍历完链表 headA ，再开始遍历链表 headB ，当走到 node 时，共走步数为:
    a+(b-c)
指针 B 先遍历完链表 headB ，再开始遍历链表 headA ，当走到 node 时，共走步数为:
    b+(a-c)
若两链表 有 公共尾部 (即 c > 0c>0 ) ：指针 A , B 同时指向「第一个公共节点」node 。
若两链表 无 公共尾部 (即 c = 0c=0 ) ：指针 A , B 同时指向 nullnull 。

具体见getIntersectionNode2

网友评论:
错的人就算走过了对方的路也还是会错过。
走到尽头见不到你，于是走过你来时的路，等到相遇时才发现，你也走过我来时的路。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLength(self, head):
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        return length

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        len_a = self.getLength(headA)
        len_b = self.getLength(headB)
        diff = abs(len_a-len_b)
        if len_a > len_b:
            short = headB
            long = headA
        else:
            short = headA
            long = headB
        
        while diff:
            long = long.next
            diff -= 1
        
        while long != short:
            long = long.next
            short = short.next
        return long

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        a,b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a