'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

key:动态规划, 
设输入 nn 个骰子的解（即概率列表）为 f(n)f(n) ，其中「点数和」 xx 的概率为 f(n, x)f(n,x) 。

'''

class Solution:
    def dicesProbability(self, n: int):
        dp_1 = [0]+[1/6] * 6
        if n == 1:
            return dp_1[1:]
        else:
            for i in range(2, n+1):
                dp_2 = [0]*i
                for j in range(i, i*6+1):
                    tmp_res = 0
                    for k in range(1, min(7, j)):
                        if j-k > len(dp_1)-1:
                            continue
                        tmp_res += (1/6)*dp_1[j-k]
                    dp_2.append(tmp_res)
                dp_1 = dp_2
            return dp_2[n:]

