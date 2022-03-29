class Solution:
    def bin_search_left(self, nums, tgt):
        left = 0
        right = len(nums)-1
        idx = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] >= tgt:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        if idx == -1:
            return -1
        elif nums[idx] == tgt:
            return idx
        else:
            return -1
    
    def bin_search_right(self, nums, tgt):
        left = 0
        right = len(nums)-1
        idx = -1
        while left <= right:
            mid = (left + right + 1)//2
            if nums[mid] <= tgt:
                idx = mid
                left = mid + 1
            else:
                right = mid - 1
        if idx == -1:
            return -1
        elif nums[idx] == tgt:
            return idx
        else:
            return -1

    def search(self, nums, target) -> int:
        lb = self.bin_search_left(nums, target)
        if lb == -1:
            return 0
        else:
            rb = self.bin_search_right(nums, target)
            return rb-lb+1

if __name__ == "__main__":
    s = Solution()
    print(s.bin_search_right([5,7,7,8,8,10], 9))