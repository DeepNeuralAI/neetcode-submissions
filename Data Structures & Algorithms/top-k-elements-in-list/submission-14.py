import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using a Heap with Modified Key
        min_heap = []
        
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        for num, freq in counts.items():
            min_heap.append((-freq, num))
        
        heapq.heapify(min_heap)
        res = []

        while k > 0:
            freq, num = heapq.heappop(min_heap)
            res.append(num)
            k -= 1
        
        return res

        

                


        