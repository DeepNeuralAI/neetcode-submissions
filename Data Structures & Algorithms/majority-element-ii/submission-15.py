class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Maintaining a candidate dict of maximum of size 2
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) > 2:
                count_copy = defaultdict(int)
                
                for key in list(count):
                    count[key] -= 1

                    if count[key] == 0:
                        del count[key]
                
        count_required = len(nums) / 3
        res = []
        
        for candidate in count:
            if nums.count(candidate) > count_required: 
                res.append(candidate)
        return res        