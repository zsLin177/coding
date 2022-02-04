'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
'''
from common import *

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_p = self.diameterOfBinaryTree(root.left)
        rigt_p = self.diameterOfBinaryTree(root.right)
        return max(left_p, rigt_p, self.deep(root.left)+self.deep(root.right))

    def deep(self, root: TreeNode):
        if root is None:
            return 0
        left = self.deep(root.left)
        right = self.deep(root.right)
        return max(left, right) + 1