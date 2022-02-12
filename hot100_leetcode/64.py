'''
最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步
'''

class Solution:
    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for i in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]
        for i in range(n-2, -1, -1):
            dp[m-1][i] = dp[m-1][i+1]+grid[m-1][i]
        
        for i in range(m-2, -1, -1):
            dp[i][n-1] = dp[i+1][n-1]+grid[i][n-1]
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = grid[i][j]+min(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]