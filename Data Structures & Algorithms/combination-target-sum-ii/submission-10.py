class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr, res = [], []
        candidates.sort()
        
        def backtrack(i, curr, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            if i == len(candidates) or target < 0:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                if target - candidates[j] >= 0:
                    curr.append(candidates[j])
                    backtrack(j + 1, curr, target - candidates[j])
                    curr.pop()
        
        backtrack(0, curr, target)
        return res
            
