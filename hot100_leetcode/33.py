'''
搜索旋转排序树组:
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
'''

class Solution:
    def reverse(self, nums, l, r):
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1

    def bin_search(self, nums, target, l, r):
        while l<=r:
            k = (l+r)//2
            if nums[k] == target:
                return k
            elif nums[k] > target:
                r = k-1
            else:
                l = k+1
        return -1


    def search(self, nums, target: int) -> int:
        '''
        normal: O(n)
        先找到旋转点，然后恢复，然后二分查找，最后映射下标
        或者是，不需要恢复，在两段进行二分查找
        '''
        k = 0
        while k < len(nums)-1:
            if nums[k] > nums[k+1]:
                break
            k += 1
        # self.reverse(nums, 0, k)
        # self.reverse(nums, k+1, len(nums)-1)
        # self.reverse(nums, 0, len(nums)-1)
        idx1 = self.bin_search(nums, target, 0, k)
        if idx1 > -1:
            return idx1
        else:
            idx2 = self.bin_search(nums, target, k+1, len(nums)-1)
            if idx2 > -1:
                return idx2
            else:
                return -1

    def search2(self, nums, target: int) -> int:
        '''
        unnormal: O(logn)
        只要需要找到旋转点，那么就是O(n),尝试不去查找旋转点
        '''
        l = 0
        r = len(nums)-1
        while l<=r:
            if nums[l] < nums[r]:
                return self.bin_search(nums, l, r)
            # nums[l] > nums[r]
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if target > nums[r] and target < nums[l]:
                return -1
            k = (l+r)//2
            if nums[k] == target:
                return k
            if nums[k] > nums[l]:
                if target > nums[k]:
                    l = k+1
                else:
                    if target > nums[l]:
                        l = l+1
                        r = k-1
                    else:
                        l = k+1
                        r = r-1
            else:
                if target < nums[k]:
                    r = k-1
                else:
                    if target < nums[r]:
                        l = k+1
                        r = r-1
                    else:
                        l = l+1
                        r = k-1

            
            
