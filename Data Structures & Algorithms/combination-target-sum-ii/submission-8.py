class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr, res = [], []
        candidates.sort()

        def backtrack(start, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if target - candidates[i] >= 0:
                    curr.append(candidates[i])
                    backtrack(i + 1, target - candidates[i])
                    curr.pop()
        
        backtrack(0, target)
        return res
