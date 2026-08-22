class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Maintaining a candidate dict of maximum of size 2
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) > 2:
                count_copy = defaultdict(int)
                
                for candidate in count:
                    count[candidate] -= 1
                
                    if count[candidate] > 0:
                        count_copy[candidate] = count[candidate]
                
                count = count_copy

        count_required = len(nums) / 3
        res = []
        actual_count = {}
        for num in nums:
            if num in count:
                actual_count[num] = actual_count.get(num, 0) + 1

        for k in actual_count:
            if actual_count[k] > count_required:
                res.append(k)

        return res        