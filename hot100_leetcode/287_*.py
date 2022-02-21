'''
寻找重复的数字
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。


我们对 \textit{nums}nums 数组建图，每个位置 ii 连一条 i\rightarrow \textit{nums}[i]i→nums[i] 的边。
由于存在的重复的数字 \textit{target}target，因此 \textit{target}target 这个位置一定有起码两条指向它的边，
因此整张图一定存在环，且我们要找到的 \textit{target}target 就是这个环的入口
key:出发点一定要不在环的内部


'''

class Solution:
    def findDuplicate1(self, nums) -> int:
        '''
        time:O(n),存在环的链表寻找入口
        '''
        fast = slow = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while fast!=slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def findDuplicate2(self, nums) -> int:
        '''
        time:O(nlgn),  二分查找
        '''
        l = 1
        r = len(nums)-1
        res = -1
        while l<=r:
            mid = (l+r)//2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if cnt <= mid:
                l = mid+1
            else:
                # cnt>mid (mid >= target)
                r = mid-1
                res = mid
        return res
