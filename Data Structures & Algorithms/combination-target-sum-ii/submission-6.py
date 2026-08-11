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
            
            i = start + 1
            while i < n and candidates[i] == candidates[i - 1]:
                i += 1
            
            backtrack(i, target)


        backtrack(0, target)
        return res