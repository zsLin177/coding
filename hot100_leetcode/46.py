'''
全排列

'''

class Solution:
    def permute(self, nums):
        def dfs(nums, left, right, res):
            if left == right:
                res.append(nums[:])
            else:
                for i in range(left, right+1):
                    tmp = nums[i]
                    nums[i] = nums[left]
                    nums[left] = tmp

                    dfs(nums, left+1, right, res)

                    tmp = nums[i]
                    nums[i] = nums[left]
                    nums[left] = tmp
        
        res = []
        dfs(nums, 0, len(nums)-1, res)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2]))

