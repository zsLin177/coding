
class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            t_s = ''.join(sorted(s))
            res[t_s] = res.get(t_s, [])
            res[t_s].append(s)
        return list(res.values())

    def groupAnagrams2(self, strs):
        '''
        回溯, 写不出来
        '''
        def dfs(strs, begin, path, res, used):
            if begin >= len(strs):
                if len(path)>0:
                    res.append(path[:])
            else:
                for i in range(begin, len(strs)):
                    if len(path) == 0 and used[i] == 0:
                        used[i] = 1
                        dfs(strs, i+1, [strs[i]], res, used)
                    elif len(path) > 0:
                        if sorted(strs[i]) == sorted(path[0]) and used[i] == 0:
                            used[i] = 1
                            dfs(strs, i+1, path+[strs[i]], res, used)
                        else:
                            dfs(strs, i+1, path, res, used)
        
        res = []
        used = [0] * len(strs)
        path = []
        dfs(strs, 0, path, res, used)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
