'''
寻找数组中所有不同的三元组
'''


def find_diff_3tuples(nums):
    res = []

    def dfs(nums, path):
        nonlocal res
        if len(path) == 3:
            res.append(path)
        else:
            for i in range(len(nums)):
                dfs(nums[0:i]+nums[i+1:], path+[nums[i]])
    
    dfs(nums, [])
    return res

if __name__ == '__main__':
    print(find_diff_3tuples([1,2,3, 4]))