'''
计算数值的次方

实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题

快速min，递归，分奇偶讨论

'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x, n = 1/x, -n
        
        def compute(x, n):
            if n == 0:
                return 1
            elif n%2 == 0:
                return compute(x*x, n//2)
            else:
                return compute(x*x, n//2) * x
        
        return compute(x, n)