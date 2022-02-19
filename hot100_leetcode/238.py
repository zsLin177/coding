'''
数组中除了自己外的所有数字的乘积

key:
两个dp
dp1[i]表示以nums[i]结尾的结果即dp1[i] = dp1[i-1]*nums[i-1]
dp2[i]表示以nums[i]结尾的结果即dp2[i] = dp2[i-1]*nums[i+1]
然后两个相乘
'''

class Solution:
    def productExceptSelf(self, nums):
        # 两个dp
        dp1 = [1]* len(nums)
        for i in range(1, len(nums)):
            dp1[i] = dp1[i-1]*nums[i-1]

        dp2 = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            dp2[i] = dp2[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            dp1[i] *= dp2[i]
        return dp1