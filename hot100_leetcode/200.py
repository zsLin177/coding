'''
岛屿数量

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

key:深度递归
'''

class Solution:
    def numIslands(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0]*n for i in range(m)]
        res = 0

        def travel(visited, i, j, m, n, grid):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if visited[i][j]:
                return
            else:
                visited[i][j] = 1
                if (i+1)<m and grid[i+1][j] == '1':
                    travel(visited, i+1, j, m, n, grid)
                if (i-1)>=0 and grid[i-1][j] == '1':
                    travel(visited, i-1, j, m, n, grid)
                if (j+1)<n and grid[i][j+1] == '1':
                    travel(visited, i, j+1, m, n, grid)
                if (j-1)>=0 and grid[i][j-1] == '1':
                    travel(visited, i, j-1, m, n, grid)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    res += 1
                    travel(visited, i, j, m, n, grid)
        
        return res

