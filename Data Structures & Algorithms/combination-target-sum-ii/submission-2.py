class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()

        def solve(i, current, target):
            if target == 0:
                res.append(current.copy())
                return
            
            if i == len(candidates):
                return

            if target - candidates[i] >= 0:
                current.append(candidates[i])
                solve(i + 1, current, target - candidates[i])
                current.pop()
            
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1

            solve(i + 1, current, target)

        res = []
        solve(0, [], target)
        return res