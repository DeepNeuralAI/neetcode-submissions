import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Heap to return minimum count
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        heap = []
        for num in counts:
            heapq.heappush(heap, (counts[num], num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for count, num in heap:
            res.append(num)
        
        return res


        

        