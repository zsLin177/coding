'''
二叉树大层次遍历
'''
class Solution:
    def levelOrder(self, root):
        res = []
        queue = []
        if not root:
            return []
        queue.append(root)
        this_layer_num = 1
        next_layer_num = 0
        while len(queue)>0:
            this_layer_nodes = []
            while this_layer_num:
                tmp = queue.pop(0)
                this_layer_nodes.append(tmp.val)
                this_layer_num -= 1
                if tmp.left:
                    queue.append(tmp.left)
                    next_layer_num += 1
                if tmp.right:
                    queue.append(tmp.right)
                    next_layer_num += 1
            res.append(this_layer_nodes)
            this_layer_num = next_layer_num
            next_layer_num = 0
        return res