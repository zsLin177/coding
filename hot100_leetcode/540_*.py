'''
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

key:
二分查找，注意返回的条件以及如何选择哪个半区
'''

class Solution:
    def singleNonDuplicate(self, nums) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            if left == right:
                return nums[left]
            inter_idx = (left+right)//2
            if nums[inter_idx] > nums[inter_idx-1] and nums[inter_idx] < nums[inter_idx+1]:
                return nums[inter_idx]
            n = inter_idx
            if n%2 == 0:
                if nums[inter_idx] == nums[inter_idx-1]:
                    right = inter_idx
                else:
                    left = inter_idx
            else:
                if nums[inter_idx] == nums[inter_idx-1]:
                    left = inter_idx+1
                else:
                    right = inter_idx-1
