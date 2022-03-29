
def travel(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for i in range(m)]
    dp[0][0] = matrix[0][0]

    # 初始化
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + matrix[0][i]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + matrix[i][j]
    
    return dp[m-1][n-1]
    
    


