'''
栈的压入和弹出顺序
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

简单说就是给定栈的压入顺序，判断是否可以pop出给定的pop顺序

key:
用一个栈来模拟出栈顺序.
'''

class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        while len(popped)>0:
            while len(stack) == 0 or stack[-1] != popped[0]:
                if len(pushed)>0:
                    stack.append(pushed.pop(0))
                else:
                    return False
            stack.pop()
            popped.pop(0)
        return True
            