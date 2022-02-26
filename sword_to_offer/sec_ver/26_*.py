'''
判断二叉树是否是另一棵树的子结构

思路：
先序遍历每个点，判断以该点为根是否包含B

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def contain(A, B):
            # 以A为根是否包含B
            if B is None:
                return True
            if A is None or A.val != B.val:
                return False
            return contain(A.left, B.left) and contain(A.right, B.right)

        if A is None or B is None:
            return False
        else:
            return contain(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)