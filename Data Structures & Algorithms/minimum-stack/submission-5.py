class MinStack:

    def __init__(self):
        self.stack = []
        self.current_minis = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.current_minis.append(val)
        elif val < self.current_minis[-1]:
            self.current_minis.append(val)
        else:
            self.current_minis.append(self.current_minis[-1])
        
        self.stack.append(val)
        
    def pop(self) -> None:
        if not self.stack:
            return
        
        value = self.stack.pop()
        self.current_minis.pop()
        
    def top(self) -> int:
        if not self.stack:
            return
        
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return
        
        return self.current_minis[-1]
        
