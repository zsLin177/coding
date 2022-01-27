# -*- coding:utf-8 -*-
# 这题推荐使用递归的做法，如果不考虑递归的话，需要考虑的情形有点麻烦。
# 链表的递归，主要是靠相邻的两个节点来if else。
# 以phead作为开始链表，如果phead==phead.next那么。。。；如果phead!=phead.next，那么phead保留，并且后面从phead.next考虑
import pdb
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication_norecur(self, pHead):
        if(pHead == None or pHead.next == None):
            return pHead
        elif(pHead.next.val == pHead.val and pHead.next.next == None):
            return None
        else:
            pp = ListNode(-1)
            pp.next = pHead
            p = pHead
            cur = pHead.next
            # pdb.set_trace()
            while(cur!= None):
                while(cur!=None and cur.val > p.val):
                    pp = p
                    p = cur
                    cur = cur.next
                if(cur!=None):
                    dup_val = cur.val
                    while(cur!=None and cur.val == dup_val):
                        cur = cur.next
                    if(cur!=None):
                        pp.next = cur
                        if(pp.val == -1):
                            pHead = cur
                        p = cur
                        cur = cur.next
                    else:
                        pp.next = cur
            if(pp.val == -1):
                return pp.next
            else:
                return pHead
    
    def deleteDuplication(self, pHead):
        if(pHead == None):
            return None
        if(pHead != None and pHead.next == None):
            return pHead
        if(pHead.val == pHead.next.val):
            cur = pHead.next
            while(cur!=None and cur.val == pHead.val):
                cur = cur.next
            return self.deleteDuplication(cur)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead

def build(lst):
    if(len(lst) == 1):
        return ListNode(lst[0])
    else:
        head = ListNode(lst[0])
        p = head
        for i in range(1, len(lst)):
            p.next = ListNode(lst[i])
            p = p.next
        return head

if __name__ == "__main__":
    lst = [1,2,3,3,4,4,5]
    pHead = build(lst)
    s = Solution()
    s.deleteDuplication(pHead)