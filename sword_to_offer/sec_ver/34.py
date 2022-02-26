'''
二叉树中从根到叶子和为target的路径
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

key：
注意是到叶子的和，
经典的模版dfs(res, path)写法

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int):
        res = []
        path = []

        if root is None:
            return res

        def dfs(root, path, remain):
            nonlocal res
            if root.left is None and root.right is None and remain == root.val:
                res.append(path+[remain])
                return
            elif root.left is None and root.right is None:
                return
            else:
                if root.left:
                    dfs(root.left, path+[root.val], remain-root.val)
                if root.right:
                    dfs(root.right, path+[root.val], remain-root.val)

        
        dfs(root, path, target)
        return res
