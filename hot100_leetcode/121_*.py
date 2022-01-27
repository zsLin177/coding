'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

'''

class Solution:
    def maxProfit_1(self, prices) -> int:
        '''
        暴力：超时
        '''
        max_pro = 0
        for i in range(len(prices)-1):
            buy = prices[i]
            max_pro = max(max_pro, max(prices[i+1:])-buy)
        return max_pro

    def maxProfit(self, prices) -> int:
        '''
        动态规划，从后往前遍历，
        如果位置i之后没有比p[i]大的，那么该天的最大利润为0；
        否则该天的最大利润是i之后的最大值减去p[i]
        '''
        max_price = prices[-1]
        prices[-1] = 0  # 最后一个位置能够得到的最大利润
        for i in range(len(prices)-2, -1, -1):
            if prices[i] >= max_price:
                max_price = prices[i]
                prices[i] = 0
            else:
                prices[i] = max_price - prices[i]
        return max(prices)