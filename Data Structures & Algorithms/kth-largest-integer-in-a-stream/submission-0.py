from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for i in range(len(nums)):
            if len(self.heap) < self.k:
                heappush(self.heap, nums[i])
            elif nums[i] > self.heap[0]:
                heappop(self.heap)
                heappush(self.heap, nums[i])
            
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappop(self.heap)
            heappush(self.heap, val)
        
        return self.heap[0]
        

        
        

        
