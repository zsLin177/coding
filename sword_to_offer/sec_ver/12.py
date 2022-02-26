'''
矩阵路径，匹配单词
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
'''

class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[0]*n for i in range(m)]

        def search(board, word, idx, i, j, m, n):
            nonlocal visited
            if idx >= len(word):
                return True
            if i<0 or i>=m or j<0 or j>=n:
                return False
            if board[i][j] == word[idx] and not visited[i][j]:
                visited[i][j] = 1
                if search(board, word, idx+1, i, j-1, m, n):
                    return True
                if search(board, word, idx+1, i, j+1, m, n):
                    return True
                if search(board, word, idx+1, i+1, j, m, n):
                    return True
                if search(board, word, idx+1, i-1, j, m, n):
                    return True
                visited[i][j] = 0
            else:
                return False
                
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if search(board, word, 0, i, j, m, n):
                        return True
        return False