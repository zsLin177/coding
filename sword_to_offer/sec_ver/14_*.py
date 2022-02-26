'''
剪断绳子

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

dp:
this_step = max(j*dp[i-j], j*(i-j))
dp[i] = max(dp[i], this_step)

此外，如果题目要求对答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
那么就一般就不推荐dp了，至少dp存储的不可以是中途取模的结果，取模之后dp就不是原来的意义了，
但是python还可以。。。然后最终返回的结果取模就行了，取模不要用1e9，要用10**9
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        '''
        dp
        '''
        dp = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                this_step = max(j*dp[i-j], j*(i-j))
                dp[i] = max(dp[i], this_step)
        return dp[n]

    def cuttingRope2(self, n: int) -> int:
        '''
        数学：尽可能多的把绳子切分为长度为3的小段，对于最终的剩余的小段要进行特判
        '''
        if n <= 3:
            return n-1
        a, b = n//3, n%3
        if b == 0:
            return 3**a
        elif b == 1:
            return (3**(a-1)) * 4
        else:
            return (3**a) * 2