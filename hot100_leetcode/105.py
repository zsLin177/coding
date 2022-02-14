'''
从中序遍历和前序遍历重建二叉树
'''

from common import *

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root_val = preorder[0]
        root_val_idx = inorder.index(root_val)
        left = self.buildTree(preorder[1:root_val_idx+1], inorder[0:root_val_idx])
        right = self.buildTree(preorder[root_val_idx+1:], inorder[root_val_idx+1:])
        root = TreeNode(root_val, left, right)
        return root