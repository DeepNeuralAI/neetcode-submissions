class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp = []
        curMin = self.stack[-1]
        
        while self.stack:
            curMin = min(curMin, self.stack[-1])
            temp.append(self.stack.pop())
        
        while temp:
            self.stack.append(temp.pop())

        return curMin        
