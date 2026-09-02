import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)

            if y != x and abs(y) > abs(x):
                heapq.heappush(max_heap, y - x)
        
        if not max_heap:
            return 0
        
        return -max_heap[0]




