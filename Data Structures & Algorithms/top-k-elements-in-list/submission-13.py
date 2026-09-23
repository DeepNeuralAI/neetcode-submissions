class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
        
        
                


        