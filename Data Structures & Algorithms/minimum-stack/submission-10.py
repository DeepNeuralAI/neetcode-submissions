class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, val: int) -> None:
        if not self.s1:
            self.s2.append(val)
            self.s1.append(val)
        else:
            current_min = min(val, self.s2[-1])
            self.s2.append(current_min)
            self.s1.append(val)

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()
        
    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.s2[-1]
        
