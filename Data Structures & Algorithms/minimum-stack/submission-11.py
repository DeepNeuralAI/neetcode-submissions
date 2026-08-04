class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, val: int) -> None:
        if not self.s1:
            self.s2.append(val)
            self.s1.append(val)
            return

        if val <= self.s2[-1]:
            self.s2.append(val)
        self.s1.append(val)

    def pop(self) -> None:
        val = self.s1.pop()
        
        if self.s2[-1] == val:
            self.s2.pop()
        
    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.s2[-1]
        
