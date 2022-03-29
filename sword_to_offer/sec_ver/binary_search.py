'''
二分查找的合辑, 包括普通二分查找, 以及查找左右边界
'''

def bin_search(nums, target):
    '''
    普通二分查找
    '''
    if len(nums) == 0:
        return -1
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid-1
        else:
            l = mid+1
    return -1


def bin_search_left_edge(nums, target):
    '''
    包含重复元素，寻找最左边的那个
    '''
    if len(nums) == 0:
        return -1
    l, r = 0, len(nums)-1
    idx = -1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] >= target:
            r = mid-1
            idx = mid
        else:
            l = mid+1
    if idx == -1:
        return -1
    elif nums[idx] == target:
        return idx
    else:
        return -1

def bin_search_right_edge(nums, target):
    '''
    包含重复元素，寻找最右边的那个
    '''
    if len(nums) == 0:
        return -1
    l, r = 0, len(nums)-1
    idx = -1
    while l<=r:
        mid = (l+r+1)//2
        if nums[mid] <= target:
            l = mid+1
            idx = mid
        else:
            r = mid-1
    if idx == -1:
        return -1
    elif nums[idx] == target:
        return idx
    else:
        return -1



if __name__ == "__main__":
    print(bin_search_right_edge([0,0,0,0,1,1,1,2,2,3,4,4], 1))


