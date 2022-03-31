'''
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。


约瑟夫环问题：
key：直接模拟会超时
dp[i]: 表示0, 1, 2, ..., i-1的结果
dp[i] = (dp[i-1]+m)%i
直接记住这个递推公式
'''

class Solution:
    def lastRemaining1(self, n: int, m: int) -> int:
        '''
        模拟法，超时
        '''
        lst = [i for i in range(n)]
        remain = n
        i = 0
        while remain > 1:
            to_del_idx = (i+(m-1))%remain
            lst.pop(to_del_idx)
            remain -= 1
            i = (to_del_idx)%remain
        return lst[0]

    def lastRemaining(self, n: int, m: int) -> int:
        dp = 0
        for i in range(2, n+1):
            dp = (dp+m)%i
        return dp
    

if __name__ == "__main__":
    s = Solution()
    print(s.lastRemaining(82002, 120659))