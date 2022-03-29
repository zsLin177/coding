'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1
'''

class MaxQueue:

    def __init__(self):
        self.queue = []
        self.dequeue = []


    def max_value(self) -> int:
        if self.dequeue:
            return self.dequeue[0]
        else:
            return -1


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        if len(self.dequeue) == 0:
            self.dequeue.append(value)
        else:
            while len(self.dequeue) > 0 and self.dequeue[-1]<value:
                self.dequeue.pop()
            self.dequeue.append(value)

    def pop_front(self) -> int:
        if self.queue:
            v = self.queue.pop(0)
            if v == self.dequeue[0]:
                self.dequeue.pop(0)
            return v
        else:
            return -1        



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()