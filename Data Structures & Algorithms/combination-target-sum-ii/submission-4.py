class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()
        current, res = [], []

        def backtrack(start, target):
            if target == 0:
                res.append(current.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                
                if candidates[i] > target:
                    break

                current.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                current.pop()
        
        backtrack(0, target)
        return res