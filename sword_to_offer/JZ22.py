# ***快慢指针，值得一看

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#
class Solution:
    def FindKthToTail_2(self , pHead: ListNode, k: int) -> ListNode:
        nodes = []
        pointer = pHead
        while pointer != None:
            nodes.append(pointer)
            pointer = pointer.next
        if k > len(nodes) or k <= 0:
            return None
        else:
            return nodes[-k]

    def FindKthToTail_3(self , pHead: ListNode, k: int) -> ListNode:
        length = 0
        pointer = pHead
        while pointer != None:
            pointer = pointer.next
            length += 1
        if k > length or k <= 0:
            return None
        else:
            cur = 0
            tgt = length - k
            pointer = pHead
            while(cur < tgt):
                pointer = pointer.next
                cur += 1
            return pointer

    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        if k <= 0:
            return None
        fast_p = pHead
        slow_p = pHead
        while k>0:
            if fast_p == None:
                return None
            fast_p = fast_p.next
            k -= 1
        while fast_p != None:
            fast_p=fast_p.next
            slow_p=slow_p.next
        return slow_p