import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Heap where key = (cnt, num)
        n = len(nums)
        min_heap = []

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        while min_heap:
            freq, num = heapq.heappop(min_heap)
            res.append(num)
        return res



        