'''
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
'''

from common import *

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        new_left = self.invertTree(root.left)
        new_right = self.invertTree(root.right)
        root.left = new_right
        root.right = new_left
        return root
