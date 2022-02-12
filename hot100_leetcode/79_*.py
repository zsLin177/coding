'''
单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

key:
回溯的时候，需要注意该位置是否已经使用过，所以也要注意恢复mark
'''

class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        def travel(board, m, n, word, idx, i, j, mark):
            if idx >= len(word):
                return True
            if i >= m or j >= n or i<0 or j<0:
                return False
            if mark[i][j] == 1:
                return False
            if board[i][j] == word[idx]:
                mark[i][j] = 1
                up = travel(board, m, n, word, idx+1, i-1, j, mark)
                if up:
                    return True
                left = travel(board, m, n, word, idx+1, i, j-1, mark)
                if left:
                    return True
                right = travel(board, m, n, word, idx+1, i, j+1, mark)
                if right:
                    return True
                low = travel(board, m, n, word, idx+1, i+1, j, mark)
                if low:
                    return True
                # 恢复
                mark[i][j] = 0
                return False
            else:
                return False
        mark = [[0]*n for k in range(m)]
        for i in range(m):
            for j in range(n):
                if travel(board, m, n, word, 0, i, j, mark):
                    return True
        return False