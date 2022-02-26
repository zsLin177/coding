# ***判断两个树，是否是子结构，值得一看
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot1 TreeNode类 
# @param pRoot2 TreeNode类 
# @return bool布尔型
#
class Solution:
    def HasSubtree(self , pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        if pRoot1 == None or pRoot2 == None:
            return False
        if self.issame(pRoot1, pRoot2):
            return True
        elif(self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)):
            return True
        else:
            return False
    
    def issame(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot1.val != pRoot2.val:
            return False
        right = True
        left = True
        if pRoot2.left != None:
            left = self.issame(pRoot1.left, pRoot2.left)
        if(pRoot2.right != None):
            right = self.issame(pRoot1.right, pRoot2.right)
        return left and right