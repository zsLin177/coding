'''
完全平方数
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

dp[i]:表示数字i的结果
我的递推公式更慢:
bottom = (i+1)//2
for j in range(i-1, bottom-1, -1):
    dp[i] = min(dp[i], dp[j]+dp[i-j])
我是直接分解为两个数的和

更好的:
sq = int(math.sqrt(i))
for j in range(sq, 0, -1):
    dp[i] = min(dp[i], 1+dp[i-j*j])
应该分解为一个平方数和另一个数的和

'''

import math, pdb
class Solution:
    def numSquares(self, n: int) -> int:
        res = 10000
        def func(num, path):
            nonlocal res
            if num==0:
                res = min(res, len(path))
            else:
                ceil = int(math.sqrt(num))
                for i in range(ceil, 0, -1):
                    val = i*i
                    func(num-val, path+[val])
        path = []
        func(n, path)
        return res

    def numSquares2(self, n: int) -> int:
        dp = [0] + [i for i in range(1, n+1)]
        for i in range(2, n+1):
            sq = int(math.sqrt(i))
            if sq*sq == i:
                dp[i] = 1
            else:
                bottom = (i+1)//2
                for j in range(i-1, bottom-1, -1):
                    dp[i] = min(dp[i], dp[j]+dp[i-j])
        return dp[n]

    def numSquares3(self, n: int) -> int:
        dp = [0] + [i for i in range(1, n+1)]
        for i in range(2, n+1):
            sq = int(math.sqrt(i))
            if sq*sq == i:
                dp[i] = 1
            else:
                for j in range(sq, 0, -1):
                    dp[i] = min(dp[i], 1+dp[i-j*j])
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares2(7691))