'''
电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

递归:
输入:s
res[i]:表示字串s[0:i+1]对应的结果
res[i] = [x cat each char in get_char(s[i]) for x in res[i-1]]
'''

class Solution:
    def get_char(self, digit: str):
        digit = int(digit)
        if (digit >= 2 and digit <=6):
            return [chr(97+3*(digit-2) + i) for i in range(3)]
        elif digit == 7:
            return ['p', 'q', 'r', 's']
        elif digit == 9:
            return ['w', 'x', 'y', 'z']
        else:
            return ['t', 'u', 'v']


    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return self.get_char(digits)
        else:
            pre_reses = self.letterCombinations(digits[0:-1])
            this_num_chars = self.get_char(digits[-1])
            res = []
            for pre_res in pre_reses:
                for this_char in this_num_chars:
                    res.append(pre_res+this_char)
            return res
        
