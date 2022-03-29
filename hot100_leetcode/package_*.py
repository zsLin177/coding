'''
背包问题
'''
import pdb


class Solution():
    def max_profit1(self, weights, values, contain):
        '''
        最经典的0-1背包问题
        '''
        n, c = len(weights), contain
        dp = [[0]*(c+1) for i in range(n+1)]
        weights = [0]+weights
        values = [0]+values
        for i in range(1, n+1):
            for j in range(1, c+1):
                if weights[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], values[i]+dp[i-1][j-weights[i]])
        return dp[n][c]

    def max_profit2(self, weights, values, contain):
        '''
        最经典的0-1背包问题
        优化存储空间
        '''
        n, c = len(weights), contain
        weights = [0]+weights
        values = [0]+values
        dp_1 = [0]*(c+1)
        for i in range(1, n+1):
            dp_2 = [0]*(c+1)
            for j in range(1, c+1):
                if weights[i] > j:
                    dp_2[j] = dp_1[j]
                else:
                    dp_2[j] = max(dp_1[j], values[i]+dp_1[j-weights[i]])
            dp_1 = dp_2
        return dp_2[-1]

    def max_profit3(self, weights, values, contain):
        '''
        最经典的0-1背包问题
        要求背包必须装满
        '''
        n, c = len(weights), contain
        weights = [0]+weights
        values = [0]+values
        dp = [[0]*(c+1) for i in range(n+1)]
        path = [[0]*(c+1) for i in range(n+1)]
        for i in range(1, c+1):
            # dp[0][0]装满, 别的都没有装满
            dp[0][i] = -float('inf')
        
        for i in range(1, n+1):
            for j in range(1, c+1):
                if weights[i] > j:
                    dp[i][j] = dp[i-1][j]
                    path[i][j] = 0
                else:
                    if dp[i-1][j] > values[i]+dp[i-1][j-weights[i]]:
                        dp[i][j] = dp[i-1][j]
                        path[i][j] = 0
                    else:
                        dp[i][j] = values[i]+dp[i-1][j-weights[i]]
                        path[i][j] = 1

        res = []
        p = n
        j = c
        while p>=1:
            if path[p][j] == 1:
                # yuan xia biao
                res.append(p-1)
                j = j-weights[p]
                p -= 1
            else:
                p -= 1
            

        return dp[n][c], res


if __name__ == '__main__':
    # w = [4, 6, 2, 2, 5, 1]
    # v = [8, 10, 6, 3, 7, 2]
    # c = 12

    w = [4, 6]
    v = [10, 8]
    c = 6
    s = Solution()

    print(s.max_profit1(w, v, c))
    print(s.max_profit2(w, v, c))
    print(s.max_profit3(w, v, c))


    