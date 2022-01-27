'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

'''

class Solution:
    def twoSum(self, nums, target):
        j = -1
        for i in range(len(nums)):
            cur = nums[i]
            if (target-cur) in nums:
                if (nums.count(cur) == 1 and (target-cur) == cur):
                    continue
                else:
                    j = nums.index(target-cur, i+1)
                    break
        if j >= 0:
            return [i, j]
        else:
            return []

    def twoSum_hash(self, nums, target):
        hashmap = {}
        for idx, num in enumerate(nums):
            j = hashmap.get(target-num)
            if j is not None:
                return [idx, j]
            hashmap[num] = idx

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum_hash([3, 4], 7))