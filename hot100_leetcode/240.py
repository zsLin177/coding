'''
搜索二维矩阵
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
'''

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def search(i, j, m, n, matrix, target):
            if i>=m or j<0:
                return False
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                return search(i+1, j, m, n, matrix, target)
            else:
                return search(i, j-1, m, n, matrix, target)
        
        return search(0, n-1, m, n, matrix, target)
