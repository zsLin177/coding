# ****值得一看

# 这一题要求时间复杂度为log(n)，优先考虑二分。难在确定下一步的区间选择：
# 如果mid>right，说明两头高，中间低，最小的在中间
# 如果mid<=right, 说明从mid到right符合非递减趋势，最小值在left到mid之间
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        left = 0
        right = len(rotateArray)-1
        while(left < right):
            tmp_idx = ((left+right)//2)+1
            tmp = rotateArray[tmp_idx]
            if(tmp < rotateArray[tmp_idx-1]):
                return tmp
            elif(tmp > rotateArray[right]):
                left = tmp_idx+1
            elif(tmp <= rotateArray[right]):
                right = tmp_idx-1

        return rotateArray[left]
