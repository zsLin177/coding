'''
机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

travel 表示从i, j出发, 在递归调用的时候必须先判断能否从下一个点出发，
和那个匹配单词相比，就是加了限制，有的方向就不能去了，不能去的就不去了
'''

class Solution:
    def wei_sum(self, a, b):
        res = 0
        for c in str(a):
            res += int(c)
        for c in str(b):
            res += int(c)
        return res

    def movingCount(self, m: int, n: int, k: int) -> int:
        count = 0
        visited = [[0]*n for i in range(m)]

        def travel(i, j, m, n, k):
            nonlocal count, visited
            if i<0 or i>=m or j<0 or j>=n:
                return
            if not visited[i][j]:
                visited[i][j] = 1
                sum_val = self.wei_sum(i, j)
                if sum_val <= k:
                    count += 1
                if i+1<m and self.wei_sum(i+1, j)<=k:
                    travel(i+1, j, m, n, k)
                if i-1>=0 and self.wei_sum(i-1, j)<=k:
                    travel(i-1, j, m, n, k)
                if j-1>=0 and self.wei_sum(i, j-1)<=k:
                    travel(i, j-1, m, n, k)
                if j+1<n and self.wei_sum(i,j+1)<=k:
                    travel(i, j+1, m, n, k)
            else:
                return
        
        travel(0, 0, m, n, k)
        return count

            
