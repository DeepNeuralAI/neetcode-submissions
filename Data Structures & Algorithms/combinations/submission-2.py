class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k > n:
            return []

        def solve(i, current):
            if len(current) == k:
                res.append(current.copy())
                return
            
            for j in range(i, n + 1):
                current.append(j)
                solve(j + 1, current)
                current.pop()
        
        res = []
        solve(1, [])
        return res