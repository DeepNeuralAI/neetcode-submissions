class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Using Hashmap 
        # Keep two candidates in hashmap -- moment there exists three, decrement one from each
        # Always maintain size 2 hashmap


        count = defaultdict(int)
        num_required = len(nums) / 3

        for num in nums:
            count[num] += 1

            if len(count) > 2:
                new_count = defaultdict(int)
                
                for k in count:
                    count[k] -= 1

                    if count[k] > 0:
                        new_count[k] = count[k]
                count = new_count
            
        res = []
        for candidate in count:
            if nums.count(candidate) > num_required:
                res.append(candidate)
        
        return res


        