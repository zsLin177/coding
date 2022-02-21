'''
最长上升子序列 和 最长上升子串

给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

'''

class Solution:
    def lengthOfLIS(self, nums) -> int:
        '''
        子序列
        '''
        dp  = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
            res = max(res, dp[i])
        return res

    def lengthOfLISeq(self, nums) -> int:
        '''
        子串
        '''
        if len(nums) == 1:
            return 1
        res = 1
        start = 0
        while start<len(nums):
            p = start+1
            while p<len(nums) and nums[p] > nums[p-1]:
                p += 1
            res = max(res, p-start)
            start = p
        return res
            

