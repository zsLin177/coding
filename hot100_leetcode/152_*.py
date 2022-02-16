'''
乘积最大的连续字数组
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

和53:和最大的连续字数组对应
两者的递推公式不一样
我们可以根据正负性进行分类讨论。

考虑当前位置如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，这样就可以负负得正，并且我们希望这个积尽可能「负得更多」，即尽可能小。如果当前位置是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，并且希望它尽可能地大。于是这里我们可以再维护一个 f_{\min}(i)f 
min
​
 (i)，它表示以第 ii 个元素结尾的乘积最小子数组的乘积，那么我们可以得到这样的动态规划转移方程：

'''
class Solution:
    def maxProduct(self, nums) -> int:
        max_p, min_p, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            tmp_max_p = max(max_p*nums[i], min_p*nums[i], nums[i])
            tmp_min_p = min(max_p*nums[i], min_p*nums[i], nums[i])
            max_p = tmp_max_p
            min_p = tmp_min_p
            res = max(res, max_p)
        return res
        