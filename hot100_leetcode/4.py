'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

'''
import pdb
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        new_lst = sorted(nums1 + nums2)
        if len(new_lst) % 2 == 0:
            return (new_lst[len(new_lst)//2] + new_lst[len(new_lst)//2-1])/2
        else:
            return new_lst[len(new_lst)//2]

    def findKth(self, nums1, nums2, k):
        '''
        找两个有序数组中的第K小个数
        '''
        if len(nums1) == 0:
            return nums2[k-1]
        elif len(nums2) == 0:
            return nums1[k-1]
        
        if k == 1:
            if nums1[0] <= nums2[0]:
                return nums1[0]
            else:
                return nums2[0]
        idx1 = int(len(nums1)/(len(nums1) + len(nums2)) * (k-1))
        idx2 = k - idx1 - 2
        if nums1[idx1] == nums2[idx2]:
            return nums1[idx1]
        elif nums1[idx1] < nums2[idx2]:
            return self.findKth(nums1[idx1+1:], nums2[0:idx2+1], k-idx1-1)
        else:
            return self.findKth(nums1[0:idx1+1], nums2[idx2+1:], k-idx2-1)

    def findMedianSortedArrays2(self, nums1, nums2) -> float:
        total = len(nums2) + len(nums1)
        if total%2 == 1:
            return self.findKth(nums1, nums2, total//2 + 1)
        else:
            return (self.findKth(nums1, nums2, total//2) + self.findKth(nums1, nums2, total//2 + 1)) / 2 

        

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays2([2], []))
    # print(s.findKth([1,2], [3,4], 2))
