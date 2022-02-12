'''
验证是否为搜索二叉树

key:
中虚便利， 验证是否当前的都比前一个大
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = [-float('inf')]
        def inorder(pre, root):
            if not root:
                return True
            if not inorder(pre, root.left):
                return False
            if root.val <= pre[0]:
                return False
            pre[0] = root.val
            return inorder(pre, root.right)
        return inorder(pre, root)
