class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr, res = [], []
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
        
        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    curr.append(num)
                    count[num] -= 1
                    
                    backtrack()
                    
                    curr.pop()
                    count[num] += 1
                    
        
        backtrack()
        return res

        
   