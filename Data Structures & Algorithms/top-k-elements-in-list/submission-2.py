class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq_map = {}

        for num in nums:
            num_to_freq_map[num] = num_to_freq_map.get(num, 0) + 1
        
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, freq in num_to_freq_map.items():
            buckets[freq].append(num)
        
        cnt = 0
        res = []
        for i in range(n, -1, -1):
            while buckets[i]:
                res.append(buckets[i].pop())
                cnt += 1
                
                if cnt == k:
                    return res
        return []

        