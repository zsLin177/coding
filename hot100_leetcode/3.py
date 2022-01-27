'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

对于数组或字符串类的子数组/子串问题，滑动窗口是一种常用的方法。
在每次循环中，右指针稳定右移，当遍历到重复字符时，左指针右移直到不再重复
以此作为窗口，从左向右逐步滑动即可

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        hash_set = set()
        left = 0
        right = 0
        res = 0
        while right < len(s):
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            res = max(res, right-left+1)
            hash_set.add(s[right])
            right += 1
        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(''))
