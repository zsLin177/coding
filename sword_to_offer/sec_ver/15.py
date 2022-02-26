'''
二进制数字中包含的1的数量

任何数a 若a&1=1,则a的二进制最右边为1，否则为0
a>>1， 二进制右移动一位,除以2
a<<1,左
a&b,二进制与操作
a|b,二进制或操作
a^b,二进制异或操作
~a,按位取反
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n&1
            n >>= 1
        return res