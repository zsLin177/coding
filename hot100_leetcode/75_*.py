'''
荷兰国旗问题

用指针来维护边界, 然后一点一点扩大边界
'''

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        for i in range(p, len(nums)):
            if nums[i] == 1:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

    def sortColors2(self, nums) -> None:
        p0, p2 = 0, len(nums)-1
        p = 0
        while p <= p2:
            if nums[p] == 0:
                nums[p], nums[p0] = nums[p0], nums[p]
                p0 += 1
            while p <= p2 and nums[p] == 2:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            p += 1
        