'''
跳跃游戏:
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
'''

class Solution:
    def canJump(self, nums) -> bool:
        right_most = 0
        for i in range(len(nums)):
            if i > right_most:
                return False
            else:
                right_most = max(right_most, i+nums[i])
                if right_most >= len(nums)-1:
                    return True
