'''
数组中的第K个最大元素
利用快速排序的思想，当安排的是第n-k个位置时候，返回该值就是答案
不需要排序所有
'''

class Solution:
    def quicksort(self, nums):

        def sort(nums, l, r):
            if l >= r:
                return
            value = nums[l]
            i, j = l, r
            while i < j:
                while j > i and nums[j] >= value:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= value:
                    i += 1
                nums[j] = nums[i]
            nums[i] = value

            sort(nums, l, i-1)
            sort(nums, i+1, r)
        sort(nums, 0, len(nums)-1)

    def findKthLargest(self, nums, k: int) -> int:
        
        def quick_search(nums, l, r, k):
            if l == r and l == k:
                return nums[l]
            value = nums[l]
            i, j = l, r
            while i < j:
                while j > i and nums[j] >= value:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= value:
                    i += 1
                nums[j] = nums[i]
            nums[i] = value
            if i == k:
                return value
            elif i > k:
                return quick_search(nums, l, i-1, k)
            else:
                return quick_search(nums, i+1, r, k)

        return quick_search(nums, 0, len(nums)-1, len(nums)-k)

if __name__ == '__main__':
    s= Solution()
    nums = [3,4, 1, 5, 34, 3214, 0, -1, 34, -9]
    s.quicksort(nums)
    print(nums)
