'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        斐波那契数列，直接递归
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)

    def climbStairs2(self, n: int) -> int:
        '''
        循环吧
        '''
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        pp = 1
        p = 2
        k = 3
        while k <= n:
            new = p + pp
            pp = p
            p = new
            k += 1
        
        return new

        

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs2(44))