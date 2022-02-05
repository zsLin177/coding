'''
三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
'''

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        
        res = []
        # 排序
        nums.sort()
        for k in range(len(nums)-2):
            if nums[k] > 0:
                # nums[k] 之后都是大于0的，说明之后不会存在结果
                break
            else:
                if k > 0 and nums[k] == nums[k-1]:
                    # 去重 比如[-1, -1, 0, 1]
                    continue
                i, j = k+1, len(nums)-1
                while i < j:
                    s = nums[k] + nums[i] + nums[j]
                    if s > 0:
                        j -= 1
                        # 移动到不重复的
                        while nums[j] == nums[j+1] and j > i:
                            j -= 1
                    elif s < 0:
                        i += 1
                        while nums[i] == nums[i-1] and i < j:
                            i += 1
                    else:
                        res.append([nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while nums[j] == nums[j+1] and j > i:
                            j -= 1
                        while nums[i] == nums[i-1] and i < j:
                            i += 1

        return res


