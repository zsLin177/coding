'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

key:滑动窗口
'''

class Solution:
    def findContinuousSequence(self, target: int):
        res = []
        i, j, s = 1, 2, 3
        while i<j:
            if s == target:
                res.append(list(range(i, j+1)))
                s -= i
                i += 1
            elif s<target:
                j += 1
                s += j
            else:
                s -= i
                i += 1
        return res
                
