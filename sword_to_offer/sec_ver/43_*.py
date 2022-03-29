'''
统计1出现的次数, 统计从1-n的数中, 1总共出现的次数
当然可以遍历从1-n的所有数字，但是会超时
应该去统计每一位为1时，数字的数量，累加

'''

class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        max_k = len(str(n))-1
        k = 0
        while k <= max_k:
            large_part = (n//(10**(k+1)))*(10**k)
            small_part = min(max((n%(10**(k+1)))-(10**k)+1, 0), 10**k)
            tmp = large_part + small_part
            res += tmp
            k += 1
        return res