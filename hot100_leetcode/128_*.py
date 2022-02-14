class Solution:
    def longestConsecutive(self, nums) -> int:
        '''
        nlgn
        '''
        nums.sort()
        dict_map = {}
        max_res = 0
        for i in range(len(nums)-1, -1, -1):
            tmp = dict_map.get(nums[i]+1, 0) + 1
            dict_map[nums[i]] = tmp
            max_res = max(tmp, max_res)
        return max_res

    def longestConsecutive2(self, nums) -> int:
        '''
        o(n)
        不要先想花里胡哨的算法
        '''
        num_set = set(nums)
        res = 0
        for num in num_set:
            # 这个很关键，找连续的第一个怎么找，num-1不在就是连续的第一个
            if num-1 not in num_set:
                c_num = num
                c_length = 1
                while c_num+1 in num_set:
                    c_num += 1
                    c_length += 1
                res = max(res, c_length)
        return res
        

        