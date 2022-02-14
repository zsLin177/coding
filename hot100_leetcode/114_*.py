'''
二叉树展开成链表
'''

from common import *

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(pre, flag, root):
            if root is None:
                return

            if flag:
                pre[0].left = None
                pre[0] = root
                preorder(pre, 0, root.left)
                preorder(pre, 1, root.right)
            else:
                tmp = pre[0].right
                pre[0].right = root
                pre[0].left = None
                pre[0] = root
                preorder(pre, 0, root.left)
                preorder(pre, 1, root.right)
                preorder(pre, 0, tmp)

        pre = [TreeNode(-101)]
        preorder(pre, 0, root)
        return root
