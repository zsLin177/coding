'''
找出所有和为target的数字组合

key:
回溯，关键就是要去重复（树的同一层不适用已经用过的）
一般回溯的模版:
for i in range(i, j):
    dfs(i, path) # 排除重复
    dfs(all, path, i) # 顺序可以不同
'''

class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        path = []

        def dfs(candidates, begin, path, res, target):
            if target == 0 and path != []:
                res.append(path)
            elif target < 0:
                return
            else:
                for i in range(begin, len(candidates)):
                    dfs(candidates, i, [candidates[i]]+path, res, target-candidates[i])
        
        dfs(candidates, 0, path, res, target)
        return res


if __name__ == '__main__':
    s= Solution()
    print(s.combinationSum([2,3,6,7], 7))