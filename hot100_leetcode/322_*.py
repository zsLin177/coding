'''
零钱问题

1、dp 零钱兑换所需要的最少硬币数量
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。
1.1 dp[i]表示凑成i所需要的最少硬币的数量
for money in coins:
    if money <= i:
        dp[i] = min(dp[i], 1+dp[i-money])
1.2 贪心，不一定是最优解

2、组成零钱一共有多少种组成方式
'''



class Solution:
    def coinChange(self, coins, amount) -> int:
        '''
        零钱兑换所需要的最少硬币数量
        dp
        '''
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for money in coins:
                if money <= i:
                    dp[i] = min(dp[i], 1+dp[i-money])
        return dp[amount] if dp[amount] != float('inf') else -1  

    def coinChange1(self, coins, amount) -> int:
        '''
        零钱兑换所需要的最少硬币数量
        贪心
        '''
        coins.sort(reverse=True)

        def search(coins, amount, start_idx):
            count = 0
            remain = amount
            for coin in coins[start_idx:]:
                count += int(remain/coin)
                remain -= int(remain/coin)*coin
                if remain == 0:
                    break
            if remain == 0:
                return 1, count
            else:
                return 0, -1
        
        for i in range(len(coins)):
            flag, count = search(coins, amount, i)
            if flag == 1:
                return count
        
        return -1

    def coinChang2(self, coins, amount) -> int:
        '''
        零钱兑换一共有多少种方式
        dp
        '''
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] += dp[i-coin]
        return dp[amount]

if __name__ == '__main__':
    s = Solution()
    print(s.coinChange1([11, 5, 1], 15))
    print(s.coinChange([11, 5, 1], 15))
    print(s.coinChange1([11, 2], 12))
            
            


