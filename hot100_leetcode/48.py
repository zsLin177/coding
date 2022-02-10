'''
旋转矩阵
顺时针90旋转矩阵

key：
对于矩阵中第 i 行的第 j个元素，在旋转后，它出现在倒数第 i列的第 j 个位置。
matrix[j][n-i-1] = matrix[i][j]

先上下翻转: m[i][j]==>m[n-i-1][j]
再对角反转: m[n-i-1][j]==>m[j][n-i-1]

若是要沿着逆时针90:先左右翻转再对角
'''

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 上下翻转
        for i in range(len(matrix)//2):
            for j in range(len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[len(matrix)-i-1][j]
                matrix[len(matrix)-i-1][j] = tmp
        
        # 沿着主对角线反转
        for i in range(len(matrix)):
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        
        

