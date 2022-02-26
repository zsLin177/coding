class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            pp = 0
            p = 1
            t = 1
            for i in range(2, n+1):
                # t = int((pp+p)%(7+1e9))
                t = (pp+p)
                pp = p
                p = t
            return t%MOD
            # return t

if __name__ == '__main__':
    s = Solution()
    print(s.fib(81))