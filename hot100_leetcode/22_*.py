'''
括号生成:
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

动态规划：难点在于怎么确定哪对括号是新的，把最左边的括号作为新加的一组，
那么还剩下i-1组，可以有p组在新括号里面，q组在新括号右边，(p+q=i-1)
'''

class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        
        all_res = [[None], ['()']]
        for i in range(2, n+1):
            i_res = []
            for p in range(i):
                q = i-1-p
                if p == 0:
                    s_p = ['']
                else:
                    s_p = all_res[p]
                if q == 0:
                    s_q = ['']
                else:
                    s_q = all_res[q]
                for t_p in s_p:
                    for t_q in s_q:
                        i_res.append('(' + t_p + ')' + t_q)
            all_res.append(i_res)
        return all_res[n]
                

