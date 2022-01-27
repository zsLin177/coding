

class MinStack:

    def __init__(self):
        self.data = []


    def push(self, val: int) -> None:
        if len(self.data) == 0:
            self.data.append((val, val))
        else:
            self.data.append((val, min(val, self.getMin())))


    def pop(self) -> None:
        self.data.pop(-1)

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()