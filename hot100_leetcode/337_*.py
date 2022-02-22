'''
打家劫舍3
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。


'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(root):
            if root is None:
                return 0, 0
            rt_val = root.val
            ls, ln = dfs(root.left)
            rs, rn = dfs(root.right)
            return rt_val+ln+rn, max(ls, ln)+max(rs, rn)

        return max(dfs(root))
        
    def rob2(self, root: TreeNode) -> int:
        '''
        我原本的写法
        和上面正确的写法的思想是一致的，但是我这种写法时间复杂度太高了
        当我想得到选择root和不选择root的最大值的时候我需要遍历两次，太笨了
        其实可以只要一次
        '''

        def dfs(root, if_rob):
            if root is None:
                return 0
            rt_val = root.val
            if if_rob:
                return rt_val + dfs(root.left, False) + dfs(root.right, False)
            else:
                l1 = dfs(root.left, True)
                l2 = dfs(root.left, False)
                r1 = dfs(root.right, True)
                r2 = dfs(root.right, False)
                return max(l1+r1, l1+r2, l2+r1, l2+r2)

        val1 = dfs(root, True)
        val2 = dfs(root, False)
        return max(val1, val2)