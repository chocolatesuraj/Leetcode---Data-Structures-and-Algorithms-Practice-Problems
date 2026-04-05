class MyStack:

    def __init__(self):
        self.queue=deque()
        self.temp=deque()

    def push(self, x: int) -> None:
        while self.queue:
            a=self.queue.pop()
            self.temp.appendleft(a)
        self.queue.appendleft(x)
        while self.temp:
            a=self.temp.pop()
            self.queue.appendleft(a)
    def pop(self) -> int:
        a=self.queue.pop()
        return a
        

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
