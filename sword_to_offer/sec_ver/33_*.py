'''
判断一个序列是否为二叉搜索树的后序遍历序列

key:
二叉搜索树的中序遍历是上升的

'''

class Solution:
    def verifyPostorder(self, postorder) -> bool:
        inorder = sorted(postorder)

        def if_match(inorder, postorder):
            if inorder == [] and postorder == []:
                return True
            if len(inorder) != len(postorder):
                return False
            root = postorder[-1]
            if root not in inorder:
                return False
            
            idx_inorder = inorder.index(root)
            right_num = len(inorder)-1-idx_inorder
            return if_match(inorder[idx_inorder+1:], postorder[len(inorder)-1-right_num: len(inorder)-1]) and if_match(inorder[0:idx_inorder], postorder[0:len(inorder)-1-right_num])
        
        return if_match(inorder, postorder)