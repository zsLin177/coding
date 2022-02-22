'''
前k个高频率元素

给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
'''

class Solution:
    def topKFrequent(self, nums, k: int):
        hash_dict = {}
        for num in nums:
            hash_dict[num] = hash_dict.get(num, 0)+1
        times = list(hash_dict.values())
        times.sort(reverse=True)
        low_line = times[k-1]
        res = [key for key in hash_dict.keys() if hash_dict[key]>=low_line]
        return res
        