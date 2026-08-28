class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        num_to_freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            num_to_freq[num] += 1
        
        for num, freq in num_to_freq.items():
            buckets[freq].append(num)
        

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    res.append(num)

                    if len(res) == k:
                        return res
        return res

        