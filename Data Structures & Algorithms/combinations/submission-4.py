class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr, res = [], []


        def backtrack(start):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if start == n + 1:
                return
            
            curr.append(start)
            backtrack(start + 1)
            curr.pop()

            backtrack(start + 1)
        
        backtrack(1)
        return res