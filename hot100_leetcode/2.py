'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''

# Definition for singly-linked list.
from common import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p_a = l1
        p_b = l2
        h_c = ListNode(-1)
        p_c = h_c

        c = 0
        while (p_a is not None) and (p_b is not None):
            newc = (p_a.val + p_b.val + c) // 10
            r = (p_a.val + p_b.val + c) % 10
            c = newc
            cur_node = ListNode(r)
            p_c.next = cur_node
            p_c = cur_node
            p_a = p_a.next
            p_b = p_b.next

        if p_a is None and p_b is None:
            if c != 0:
                p_c.next = ListNode(1)
            return h_c.next
        elif p_a is None:
            if c == 0:
                p_c.next = p_b
            else:
                p_c.next = self.addTwoNumbers(ListNode(1), p_b)
            return h_c.next
        else:
            if c == 0:
                p_c.next = p_a
            else:
                p_c.next = self.addTwoNumbers(ListNode(1), p_a)
            return h_c.next


if __name__ == "__main__":
    node_lst = build_link([[9,9,9,9,9,9,9],[9,9,9,9]])
    print_link(node_lst)
    s = Solution()
    print_link([s.addTwoNumbers(node_lst[0], node_lst[1])])