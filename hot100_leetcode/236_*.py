'求最近公共祖先'
'''

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(path, root, stop_value):
            if root is None:
                return
            if root.val == stop_value:
                path.append(root)
                return path
            else:
                l = dfs(path+[root], root.left, stop_value)
                if l:
                    return l
                else:
                    return dfs(path+[root], root.right, stop_value)
        
        path_p = dfs([], root, p.val)
        path_q = dfs([], root, q.val)
        max_l = min(len(path_p), len(path_q))
        i = 0
        while i<max_l and path_p[i].val == path_q[i].val:
            i += 1
        return path_q[i-1]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q) # 判断左子树是否包含p或者q
        right = self.lowestCommonAncestor(root.right, p, q) # 判断右子树是否包含p或者q
        if not left and not right: return # 1.
        if not left: return right # 3. 返回从右子树找的结果
        if not right: return left # 4.
        return root # 2. if left and right:

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tmp_map = {}
        node_map ={}

        def dfs(root):
            nonlocal tmp_map, node_map
            node_map[root.val] = root
            if root.left:
                tmp_map[root.left.val] = root.val
                dfs(root.left)
            if root.right:
                tmp_map[root.right.val] = root.val
                dfs(root.right)
        
        tmp_map[root.val] = None
        dfs(root)
        if_visited = {key:0 for key in tmp_map.keys()}
        pointer = p.val
        while pointer is not None:
            if_visited[pointer] = 1
            pointer = tmp_map[pointer]
        
        # print(if_visited)
        # print(tmp_map)
        pointer = q.val
        while pointer is not None and if_visited[pointer]==0:
            pointer = tmp_map[pointer]
        if pointer is not None:
            return node_map[pointer]
        else:
            return None
