'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

不用存储空间，用异或运算:
    一个值连续跟两个相同的数异或仍未其本身，可用来统计列表中只出现一次的元素

'''

class Solution:
    def singleNumber(self, nums) -> int:
        tmpd = {}
        for num in nums:
            tmpd[num] = tmpd.get(num, 0) + 1
        for key, value in tmpd.items():
            if value == 1:
                return key

    def singleNumber2(self, nums) -> int:
        '''
        不用存储空间，用异或运算:
        一个值连续跟两个相同的数异或仍未其本身，可用来统计列表中只出现一次的元素
        '''
        for i in range(1, len(nums)):
            nums[0] = nums[0] ^ nums[i]
        return nums[0]