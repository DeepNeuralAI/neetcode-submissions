class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        num_freq_map = {}
        
        for num in nums:
            num_freq_map[num] = num_freq_map.get(num, 0) + 1
        
        for num, freq in num_freq_map.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(n, -1, -1):
            if not buckets[i]:
                continue
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
        return []
            


        