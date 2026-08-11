class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()
        current, res = [], []
        n = len(candidates)

        def backtrack(start, target):
            if target == 0:
                res.append(current.copy())
                return
            
            if target < 0 or start == n:
                return

            if target >= candidates[start]:
                current.append(candidates[start])
                backtrack(start + 1, target - candidates[start])
                current.pop()
            
            while (start + 1) < n and candidates[start + 1] == candidates[start]:
                start += 1
            
            backtrack(start + 1, target)


        backtrack(0, target)
        return res