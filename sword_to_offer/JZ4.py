class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pre int整型一维数组 
# @param vin int整型一维数组 
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , pre, vin) -> TreeNode:
        if(len(pre) == 0):
            return None
        else:
            head_val = pre[0]
            root = TreeNode(head_val)
            left_num = vin.index(head_val)
            left_pre = pre[1:1+left_num]
            left_vin = vin[0:left_num]
            right_pre = pre[1+left_num:]
            right_vin = vin[left_num+1:]
            root.left = self.reConstructBinaryTree(left_pre, left_vin)
            root.right = self.reConstructBinaryTree(right_pre, right_vin)
            return root
