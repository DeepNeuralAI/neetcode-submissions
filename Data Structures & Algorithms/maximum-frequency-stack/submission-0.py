class FreqStack:

    def __init__(self):
        self.num_to_count = defaultdict(int)
        self.groups = defaultdict(list)
        self.maxFreq = 0
        
    def push(self, val: int) -> None:
        self.num_to_count[val] += 1
        self.maxFreq = max(self.maxFreq, self.num_to_count[val])
        self.groups[self.num_to_count[val]].append(val)

    def pop(self) -> int:
        val = self.groups[self.maxFreq].pop()
        self.num_to_count[val] -= 1

        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()