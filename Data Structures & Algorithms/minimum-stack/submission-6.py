class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.mini or self.mini and self.mini[-1] >= val:
            self.mini.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        val = self.stack.pop()
        if val == self.mini[-1]:
            self.mini.pop()

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.stack:
            return
        
        return self.mini[-1]
        
