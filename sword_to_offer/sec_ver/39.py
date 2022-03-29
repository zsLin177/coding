'''
摩尔投票法:
当众数的数量超出数组数量的一半的时候，可以用摩尔投票法，找出那个数字
不断的假设，抵消
'''

class Solution:
    def majorityElement(self, nums) -> int:
        x = None
        vote = 0
        for num in nums:
            if vote == 0:
                x = num
                vote += 1
            elif num == x:
                vote += 1
            else:
                vote -= 1
        return x