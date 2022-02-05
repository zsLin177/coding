'''
给你一个字符串 s，找到 s 中最长的回文子串。
'''

class Solution:
    def longestPalindrome1(self, s: str) -> str:
        '''
        暴力解法
        '''
        max_len = 0
        res = ''
        for i in range(len(s)):
            cur_len = len(s) - i
            if cur_len <= max_len:
                return res
            while cur_len:
                cur_s = s[i:i+cur_len]
                rev_cur_s = cur_s[: : -1]
                if cur_s == rev_cur_s:
                    if cur_len > max_len:
                        max_len = cur_len
                        res = cur_s
                    break
                cur_len -= 1
        return res

    def longestPalindrome2(self, s: str) -> str:
        '''
        TODO: 用的hash，记录每个字符出现的位置，当字符再次出现的时候，看与之前
        出现的位置之间的字符串是否是回文，且有多长。
        '''
        hash_set = {}
        max_len = 0
        res = ''
        for i in range(len(s)):
            if s[i] not in hash_set.keys():
                hash_set[s[i]] = [i]
                if max_len < 1:
                    max_len = 1
                    res = s[i]
            else:
                for last_idx in hash_set[s[i]]:
                    cur_s = s[last_idx:i+1]
                    if cur_s == cur_s[: : -1]:
                        if (i-last_idx+1) > max_len:
                            max_len = i-last_idx+1
                            res = cur_s
                        break
                hash_set[s[i]].append(i)
        return res

    def longestPalindrome3(self, s: str) -> str:
        '''
        动态规划
        dp[i]代表以下标i结尾的最长回文子串长度，
        对于每个dp[i]，都要先访问 (i-1) - dp[i-1]，也就是看能不能与前一个dp的字串组成回文串，如果不能，还得继续往后判断，直到最差的情况为dp[i] = 1
        '''
        if len(s) <= 1:
            return s
        else:
            dp = [1] * len(s)
            for i in range(1, len(s)):
                for j in range(i-1-dp[i-1], i):
                    if j < 0:
                        continue
                    cur_s = s[j:i+1]
                    if cur_s == cur_s[::-1]:
                        dp[i] = i-j+1
                        break
        maxl = max(dp)
        maxindex = dp.index(max(dp))
        return s[maxindex-maxl+1:maxindex+1]



if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome3("babad"))
