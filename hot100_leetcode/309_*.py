'''
股票可以多次买入，包含冷冻期

给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）

key:
股票问题，可以用dp进行状态转移，这题弄懂就ok了

我自己的dp超时，但是应该也是对的:
dp[i]:表示在第i天进行首次买入能得到的最大的利润
for i in range(len(prices)-2, -1, -1):
    for j in range(i+1, len(prices)):
        dp[i] = max(dp[i], prices[j]-prices[i]+max(dp[j+2:]+[0]))

'''

class Solution:
    def maxProfit2(self, prices) -> int:
        dp = [0] * len(prices)
        res = 0
        if len(prices) == 1:
            return 0
        for i in range(len(prices)-2, -1, -1):
            for j in range(i+1, len(prices)):
                dp[i] = max(dp[i], prices[j]-prices[i]+max(dp[j+2:]+[0]))
            res = max(res, dp[i])
        print(dp)
        return res

    def maxProfit(self, prices) -> int:
        res = 0
        # 当天结束后，持有股票（不在冷冻期）的状态下的最大利润
        state1 = -prices[0]
        # 当天结束后，处于冷冻期 的状态下的最大利润
        state2 = 0
        # 当天结束后，不在冷冻期，也没股票 的状态下的最大利润
        state3 = 0
        for i in range(1, len(prices)):
            st1 = max(state1, state3-prices[i])
            st2 = state1 + prices[i]
            st3 = max(state3, state2)
            res = max(st1, st2, st3)
            state1, state2, state3 = st1, st2, st3
        return res



if __name__ == '__main__':
    s = Solution()
    s.maxProfit([1,2,3,0,2])
