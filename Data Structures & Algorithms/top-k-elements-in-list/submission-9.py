import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Min Heap with (cnt, num) as key
        min_heap = []
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        pairs = []
        for num, freq in count.items():
            pairs.append((freq, num))
        
        for freq, num in pairs:
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                if freq > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (freq, num))
        
        res = []
        while min_heap:
            freq, num = heapq.heappop(min_heap)
            res.append(num)
        
        return res



