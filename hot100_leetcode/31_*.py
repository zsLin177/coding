'''
按照字典顺序的下一个排列

注意到下一个排列总是比当前排列要大，除非该排列已经是最大的排列。我们希望找到一种方法，能够找到一个大于当前序列的新序列，且变大的幅度尽可能小。具体地：

我们需要将一个左边的「较小数」与一个右边的「较大数」交换，以能够让当前排列变大，从而得到下一个排列。

同时我们要让这个「较小数」尽量靠右，而「较大数」尽可能小。当交换完成后，「较大数」右边的数需要按照升序重新排列。这样可以在保证新排列大于原来排列的情况下，使变大的幅度尽可能小。

'''

class Solution:
    def reverse(self, nums, l, r):
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1
        
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        i = len(nums) - 2
        # 从右往左找到第一个较小的数字
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        # 如果没有的话，说明就是最大的，直接逆序返回最小的
        if i == -1:
            self.reverse(nums, 0, len(nums)-1)
            return
        
        # 继续逆序找到第一个较大的数字
        j = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        
        # 交换
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

        # 对交换后的右边序列按照升序排列，因为肯定是降序的，所以直接取反即可
        self.reverse(nums, i+1, len(nums)-1)
        
