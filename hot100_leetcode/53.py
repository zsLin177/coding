'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
'''

class Solution:
    def maxSubArray(self, nums) -> int:
        '''
        动态规划 O(n)
        dp[i] 表示以nums[i]结尾的和最大的连续子数组的和
        '''
        dp = nums[:]
        path = [1] * len(nums)

        for i in range(1, len(nums)):
            if dp[i-1] >= 0:
                dp[i] = dp[i-1] + dp[i]
                path[i] = path[i-1] + 1
        
        return max(dp)