import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for st in stones:
            heapq.heappush(max_heap, -st)
        
        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            if first - second < 0:
                heapq.heappush(max_heap, first - second)
        
        if max_heap:
            return -max_heap[0]
        
        return 0
