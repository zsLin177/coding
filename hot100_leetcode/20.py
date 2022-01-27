'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

'''
class Solution:
    '''
    应栈来做
    '''
    def isMatch(self, l, r):
        if l == '(':
            if r == ')':
                return True
        elif l == '[':
            if r == ']':
                return True
        elif l == '{':
            if r == '}':
                return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '[', '{']
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    l = stack.pop()
                    if not self.isMatch(l, c):
                        return False
        if len(stack) > 0:
            return False
        return True
