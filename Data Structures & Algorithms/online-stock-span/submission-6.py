class StockSpanner:

    def __init__(self):
        self.stack = [] # (price, span) - monotonically decreasing 
        

    def next(self, price: int) -> int:
        current_span = 1
        
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            current_span += prev_span
        
        self.stack.append((price, current_span))

        return current_span

"""
[[100], [80], [60], [70], [60], [75], [85]]
stack = [(100, 1), (85, 6)]


"""


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)