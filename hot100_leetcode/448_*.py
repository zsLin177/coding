'''
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
'''

class Solution:
    def findDisappearedNumbers(self, nums):
        '''
        normal
        '''
        if_in = [0] * (len(nums)+1)
        for num in nums:
            if_in[num] = 1
        res = []
        for i in range(1, len(nums)+1):
            if if_in[i] == 0:
                res.append(i)
        return res

    def findDisappearedNumbers2(self, nums):
        '''
        奇技淫巧:
        当前元素是 nums[i]nums[i]，那么我们把第 nums[i] - 1nums[i]−1 位置的元素 乘以 -1，表示这个该位置出现过。当然如果 第 nums[i] - 1nums[i]−1 位置的元素已经是负数了，表示 nums[i]nums[i] 已经出现过了，就不用再把第 nums[i] - 1nums[i]−1 位置的元素乘以 -1。最后，对数组中的每个位置遍历一遍，如果 ii 位置的数字是正数，说明 ii 未出现过。
        '''
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                continue
            else:
                nums[idx] = -nums[idx]
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res