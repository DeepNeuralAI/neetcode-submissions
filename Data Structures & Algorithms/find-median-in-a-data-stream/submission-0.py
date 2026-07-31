from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small or num < -self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)
        
        if len(self.small) - len(self.large) > 1:
            val = -heappop(self.small)
            heappush(self.large, val)
        elif len(self.large) - len(self.small) > 1:
            val = heappop(self.large)
            heappush(self.small, -val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        
        