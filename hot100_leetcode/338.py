'''
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
'''

class Solution:
    def countBits(self, n: int):
        ans = []
        for i in range(n+1):
            ans.append(bin(i).count('1'))
        return ans

    def countBits2(self, n: int):
        '''
        dp:
        如果 ii 是偶数，那么它的二进制 1 的位数与 i / 2i/2 的二进制 1 的位数相等
        如果 ii 是奇数，那么它的二进制 1 的位数 = i - 1 的二进制位数 + 1i−1的二进制位数+1；因为奇数的二进制末尾是 1，如果把末尾的 1 去掉就等于 i - 1。又 i - 1 是偶数，所以奇数 ii 的二进制 1 的个数等于 i/2i/2 中二进制 1 的位数 +1.

        answer[i] = answer[i >> 1] + (i & 1)
        '''
        ans = [0]*(n+1)
        for i in range(1, n+1):
            ans[i] = ans[i//2] + (i&1)
        return ans

    