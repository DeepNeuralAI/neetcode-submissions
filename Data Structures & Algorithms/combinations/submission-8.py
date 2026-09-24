class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr, res = [], []

        def backtrack(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if i > n:
                return
            
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)
        
        backtrack(1, curr)
        return res


        