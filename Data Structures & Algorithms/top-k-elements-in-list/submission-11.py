class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = defaultdict(int)
        maxFreq = 0

        for num in nums:
            count[num] += 1
            maxFreq = max(maxFreq, count[num])
        
        buckets = [[] for _ in range(maxFreq + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(maxFreq, -1, -1):
            if not buckets[i]:
                continue
            
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
        return res




        