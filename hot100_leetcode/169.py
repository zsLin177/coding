'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''

class Solution:
    def majorityElement(self, nums) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        threshold = len(nums) // 2
        for key, val in d.items():
            if val > threshold:
                return key

    def majorityElement2(self, nums) -> int:
        '''
        摩尔投票法，空间O(1)
        '''
        count = 1
        major = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                major = nums[i]
                count += 1
            else:
                if nums[i] == major:
                    count += 1
                else:
                    count -= 1
        return major



if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement2([3, 3]))