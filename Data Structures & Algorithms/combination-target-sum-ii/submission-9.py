class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(i, curr_sum, subset):
            if curr_sum == target:
                res.append(subset.copy())
                return
            
            if i == len(candidates):
                return
            
            for start in range(i, len(candidates)):
                if start > i and candidates[start] == candidates[start - 1]:
                    continue
                
                if curr_sum + candidates[start] <= target:
                    subset.append(candidates[start])
                    backtrack(start + 1, curr_sum + candidates[start], subset)
                    subset.pop()

        res = []
        backtrack(0, 0, [])
        return res