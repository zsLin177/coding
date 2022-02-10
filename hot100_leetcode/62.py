'''
不同路径的个数

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1)for i in range(m+1)]
        for i in range(1, n+1):
            dp[m][i] = 1
        for i in range(1, m+1):
            dp[i][n] = 1
        for i in range(m-1, 0, -1):
            for j in range(n-1, 0, -1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        return dp[1][1]

