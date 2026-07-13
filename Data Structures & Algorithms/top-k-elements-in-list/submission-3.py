class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for _ in range(len(nums) + 1)]
        num_to_freq = defaultdict(int)

        for num in nums:
            num_to_freq[num] += 1
        
        for num, freq in num_to_freq.items():
            counts[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            if not counts[i]:
                continue
            
            while counts[i] and k > 0:
                res.append(counts[i].pop())
                k -= 1
            
            if k == 0:
                break
        
        return res

        