import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort - where indices are frequency OR -> n space and time
        # Min heap of size k? 

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        heap = []
        for (num, freq) in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for (freq, num) in heap:
            res.append(num)
        
        return res

            
        




