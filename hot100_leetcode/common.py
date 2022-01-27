class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
