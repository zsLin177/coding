'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
'''

from common import *

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        p = head
        tmp = []
        while p:
            tmp.append(p.val)
            p = p.next
        return tmp == list(reversed(tmp))

if __name__ == '__main__':
    s = Solution()
    s.isPalindrome()