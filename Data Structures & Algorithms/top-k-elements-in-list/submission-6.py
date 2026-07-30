class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        num_to_freq = defaultdict(int)

        for num in nums:
            num_to_freq[num] += 1
        
        heap = []
        for num, count in num_to_freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for cnt, num in heap]