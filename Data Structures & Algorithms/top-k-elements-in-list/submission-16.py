import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort - where indices are frequency OR -> n space and time
        # Min heap of size k? 
        n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        buckets = [[] for _ in range(n + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(n, 0, -1):
            if not buckets[i]:
                continue
            
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res


            
        




