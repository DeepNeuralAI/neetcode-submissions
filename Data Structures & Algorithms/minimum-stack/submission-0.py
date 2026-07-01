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
        curMin = float('inf')
        while self.stack:
            cur = self.stack.pop()
            curMin = min(curMin, cur)
            temp.append(cur)
        
        while temp:
            self.stack.append(temp.pop())

        return curMin        
