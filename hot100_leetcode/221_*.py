'''
矩阵中的最大正方形
key: 
dp[i][j]表示以i,j位置为右下角的最大全1正方形的边长
难的就是递推公式:
dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
推导十分精彩: https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/tong-ji-quan-wei-1-de-zheng-fang-xing-zi-ju-zhen-2/
'''
import math
import pdb
class Solution:
    def maximalSquare(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        # dp[i][j]表示以i,j位置为右下角的最大全1正方形的边长
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue
                else:
                    if dp[i-1][j-1] > 0:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        res = -1
        for i in range(m):
            for j in range(n):
                res = max(res, dp[i][j])
        
        return res*res

if __name__ =='__main__':
    s=Solution()
    a = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    print(s.maximalSquare(a))

