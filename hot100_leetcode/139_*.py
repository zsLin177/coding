'''
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

key:
dp[i]:表示s[0:i-1]是否可以由字典组成
'''

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:       
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1, n+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
            

                
