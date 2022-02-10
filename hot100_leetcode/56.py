'''
合并区间:
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

'''

class Solution:
    def merge(self, intervals):
        # 按照起始排序
        intervals.sort(key=lambda t:t[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                tmp = [res[-1][0], max(res[-1][-1], intervals[i][1])]
                res.pop()
                res.append(tmp)
            else:
                res.append(intervals[i])
        return res
