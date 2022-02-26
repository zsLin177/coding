class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return int整型
#
class Solution:
    def TreeDepth(self , pRoot: TreeNode) -> int:
        '''
        深度遍历，递归实现
        '''
        if pRoot == None:
            return 0
        else:
            return 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))

    def TreeDepth2(self, pRoot: TreeNode) -> int:
        '''
        层次遍历
        '''
        lst = []
        if pRoot == None:
            return 0
        lst.append(pRoot)
        depth = 0
        while len(lst)>0:
            depth += 1
            this_layer_num = len(lst)
            while this_layer_num:
                cur_node = lst.pop(0)
                if cur_node.left != None:
                    lst.append(cur_node.left)
                if cur_node.right != None:
                    lst.append(cur_node.right)
                this_layer_num -= 1
        return depth
