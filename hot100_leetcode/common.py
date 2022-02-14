class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Preorder1(root, res):
    '''
    digui
    '''
    if root:
        res.append(root.val)
        Inorder1(root.left, res)
        Inorder1(root.right, res)

def Preorder2(root):
    '''
    diedai
    '''
    res = []
    stack = []
    node = root
    while node or stack:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right

def Inorder1(root, res):
    '''
    digui
    '''
    if root:
        Inorder1(root.left, res)
        res.append(root.val)
        Inorder1(root.right, res)
    
def Inorder2(root):
    '''
    diedai
    '''
    stack = []
    res = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node)
        node = node.right
    
def Postorder1(root, res):
    if root:
        Postorder1(root.left)
        Postorder1(root.right)
        res.append(root.val)

def Postorder2(root):
    '''
    use one stack
    利用类似的先顺序遍历'root, right, left'，然后逆序就行了
    '''
    res = []
    stack = []
    node  = root
    while node or stack:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.right
        node = stack.pop()
        node = node.left
    res.reverse()
    return res


def build_link(input):
    '''
    input: [1,2,3] or [[1,2,3],[2,4]]
    '''
    if type(input[0]) != list:
        input = [input]
    
    res_lst = []
    for lst in input:
        head_node = ListNode(lst[0])
        p_node = head_node
        for num in lst[1:]:
            cur_node = ListNode(num)
            p_node.next = cur_node
            p_node = cur_node
        res_lst.append(head_node)
    return res_lst

def print_link(node_lst):
    for head_node in node_lst:
        p = head_node
        while p is not None:
            print(p.val, end=' ')
            p = p.next
        print()

if __name__ == "__main__":
    node_lst = build_link([[1,2,3],[2,4]])
    print_link(node_lst)
