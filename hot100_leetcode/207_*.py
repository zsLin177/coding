'''
课程表，先修课程约束，可以看成拓扑排序，有向无环图问题，
a要在b前面修，则建立一条a->b的边

有两种方法：
dfs
以及入度表bfs
'''

import collections

class Solution:
    def canFinish1(self, numCourses: int, prerequisites) -> bool:
        '''
        dfs
        '''
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])
        
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)
        
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        return valid

    def canFinish2(self, numCourses: int, prerequisites) -> bool:
        '''
        bfs
        '''
        edges = collections.defaultdict(list)
        inedges = [0] * len(numCourses)

        for lst in prerequisites:
            edges[lst[1]].append(lst[0])
            inedges[lst[0]] += 1

        # 将所有入度为 0 的节点放入队列中
        q = collections.deque([u for u in range(numCourses) if inedges[u] == 0])

        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in edges[u]:
                inedges[v] -= 1
                if inedges[v] == 0:
                    q.append(v)
        if len(res) == numCourses:
            return True
        else:
            return False
                
