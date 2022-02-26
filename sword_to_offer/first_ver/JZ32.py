# -*- coding:utf-8 -*-
# 这道题要求拼接后的字符串数值最小，排序，把会造成大数字的往后放，若ab>ba，则把a放到b后面
# 用冒泡排序
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if(len(numbers) <= 1):
            return self.generate(numbers)
        else:
            return self.generate(self.sort(numbers))

    def sort(self, numbers):
        remain_counts = len(numbers) - 1
        while(remain_counts):
            for i in range(0, remain_counts):
                if(self.compare(numbers[i], numbers[i+1])):
                    tmp = numbers[i+1]
                    numbers[i+1] = numbers[i]
                    numbers[i] = tmp
            remain_counts -= 1
        return numbers

    def compare(self, a, b):
        if((str(a)+str(b)) > (str(b)+str(a))):
            return True
        else:
            return False

    def generate(self, lst):
        if(len(lst) == 0):
            return ''
        else:
            res = ''
            for x in lst:
                res += str(x)
            return res