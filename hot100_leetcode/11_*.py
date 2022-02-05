'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
'''



class Solution:
    def maxArea(self, height) -> int:
        '''
        暴力
        '''
        res = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                tmp = (j-i) * min(height[i], height[j])
                res = max(res, tmp)
        return res

    def maxArea2(self, height) -> int:
        '''
        双指针:
        在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽 底边宽度 -1−1​ 变短：
        若向内 移动短板 ，水槽的短板 min(h[i], h[j])min(h[i],h[j]) 可能变大，因此下个水槽的面积 可能增大 。
        若向内 移动长板 ，水槽的短板 min(h[i], h[j])min(h[i],h[j])​ 不变或变小，因此下个水槽的面积 一定变小 。
        因此，初始化双指针分列水槽左右两端，循环每轮将短板向内移动一格，并更新面积最大值，直到两指针相遇时跳出；即可获得最大面积。

        '''
        i, j, res = 0, len(height)-1, 0
        while i<j:
            res = max(res, min(height[j], height[i])*(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res
        




        