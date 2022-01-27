'''
给定一个二叉树，检查它是否是镜像对称的。
'''

from common import *

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isTwoSymmetric(root.left, root.right)
        
    def isTwoSymmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None and right is not None:
            return False
        if right is None and left is not None:
            return False
        if left.val != right.val:
            return False
        
        condi1 = self.isTwoSymmetric(left.left, right.right)
        condi2 = self.isTwoSymmetric(left.right, right.left)
        return condi1 and condi2