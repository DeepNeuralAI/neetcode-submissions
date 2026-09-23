class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Maintaining a candidate dict of maximum of size 2
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            
            if len(count) > 2:
                copy = defaultdict(int)
                
                for k in count:
                    count[k] -= 1

                    if count[k] > 0:
                        copy[k] = count[k]
                count = copy
        
        res = []
        for k in count:
            if nums.count(k) > len(nums) / 3:
                res.append(k)
        
        return res
