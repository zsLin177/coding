'''
求集合的所有子集合
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集

key: 回溯
'''

class Solution:
    def subsets(self, nums):

        def dfs(nums, index, path, res):
            if index >= len(nums):
                res.append(path)
            else:
                dfs(nums, index+1, path+[nums[index]], res)
                dfs(nums, index+1, path+[], res)

        res = []
        path = []
        dfs(nums, 0, path, res)
        return res