class MinStack:

    def __init__(self):
        self.mini = []
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini:
            self.mini.append(val)
        else:
            min_val = min(self.mini[-1], val)
            self.mini.append(min_val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.mini.pop()
        return val
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
        
