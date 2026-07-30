class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        num_to_freq = defaultdict(int)

        for num in nums:
            num_to_freq[num] += 1
        
        # Bucket Sort
        counts = [[] for _ in range(n + 1)]

        for num, count in num_to_freq.items():
            counts[count].append(num)
        
        res = []
        for i in range(n, -1, -1):
            for num in counts[i]:
                res.append(num)

                if len(res) == k:
                    return res

                
        return res

        