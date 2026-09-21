class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while max_heap and len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            if first - second != 0:
                heapq.heappush(max_heap, first - second)
        
        return -max_heap[0] if max_heap else 0
            