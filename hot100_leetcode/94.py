'''
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
'''

from common import *

class Solution:
    def inorderTraversal(self, root: TreeNode):
        if root is None:
            return []
        res = []
        if root.left is not None:
            res += self.inorderTraversal(root.left)
        res.append(root.val)
        if root.right is not None:
            res += self.inorderTraversal(root.right)
        return res
