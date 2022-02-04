'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''

class Solution:
    def moveZeroes2(self, nums) -> None:
        """
        类似冒泡排序的: overtime O(n^2)
        """
        sumTimes = len(nums) - 1
        while sumTimes:
            for i in range(0, sumTimes):
                if nums[i] == 0:
                    nums[i] = nums[i+1]
                    nums[i+1] = 0
            sumTimes -= 1
    
    def moveZeroes(self, nums) -> None:
        '''
        O(n)
        '''
        # 表示当前已经存在多少个0，也就表示当前要往前挪动几个
        count = 0
        sum_num = len(nums)
        for i in range(sum_num):
            if nums[i] == 0:
                count += 1
            elif count == 0:
                continue
            else:
                nums[i-count] = nums[i]
        while count:
            nums[sum_num-count] = 0
            count -= 1
