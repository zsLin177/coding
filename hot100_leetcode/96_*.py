'''
不同的二叉搜索树的数目.
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

dp[i]:表示i个节点的二叉搜索树的数目
f(i) 表示以i为根的树的数目，一共n个节点，f(i) = dp[i-1] * dp[n-i]
dp[i] = f(1)+f(2)+...+f(i)
        = dp[0]*dp[i-1] + dp[1]*dp[i-2] +...+ dp[i-1]*dp[0]
'''

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += (dp[j-1]*dp[i-j])
        return dp[n]