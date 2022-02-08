'''
二分查找找左右边界
就可以直接背下来
'''

class Solution:
    def bin_search(self, nums, target, l, r):
        '''
        normal 二分查找
        '''
        while l<=r:
            k = (l+r)//2
            if nums[k] == target:
                return k
            elif nums[k] > target:
                r = k-1
            else:
                l = k+1
        return -1

    def bin_left_edge(self, nums, target, l, r):
        '''
        查找左边界
        '''
        while l<r: #不要等号
            mid = (l+r)//2 # 下取整，取靠左边的那个
            if nums[mid] >= target:
                r = mid
            else:
                # 如果nums[mid] < target
                l = mid + 1
        return r
    
    def bin_right_edge(self, nums, target, l, r):
        '''
        查找右边界
        '''
        while l < r:
            mid = (l+r+1)//2 # 上去整
            if nums[mid]<=target:
                left = mid
            else:
                r = mid-1
        return r

    def searchRange(self, nums, target: int):
        if len(nums) == 0:
            return [-1, -1]
        init_idx = self.bin_search(nums, target, 0, len(nums)-1)
        if init_idx == -1:
            return [-1, -1]
        else:
            end_idx = init_idx+1
            while end_idx<len(nums) and nums[end_idx] == target:
                end_idx += 1
            str_idx = init_idx-1
            while str_idx>-1 and nums[str_idx] == target:
                str_idx -= 1
            return [str_idx+1, end_idx-1]

