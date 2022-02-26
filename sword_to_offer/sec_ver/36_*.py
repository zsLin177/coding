'''
二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # an postorder travel return min and max

        def postorder_travel(root):
            if root.left is None and root.right is None:
                # 一个节点的时候也要把构成循环，容易忘掉
                root.left =root
                root.right = root
                return root, root
            
            left_min, left_max = root, root
            if root.left:
                left_min, left_max = postorder_travel(root.left)
                root.left = left_max
                left_max.right = root
            
            right_min, right_max = root, root
            if root.right:
                right_min, right_max = postorder_travel(root.right)
                root.right = right_min
                right_min.left = root
            left_min.left = right_max
            right_max.right = left_min
            return left_min, right_max
        
        if root is None:
            return None
        return postorder_travel(root)[0]