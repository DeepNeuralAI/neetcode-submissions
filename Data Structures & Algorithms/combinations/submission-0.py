class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, 1, [], res)
        return res


    def dfs(self, n, k, i, current, res):
        if len(current) == k:
            res.append(current.copy())
            return
        
        if i > n:
            return
        
        current.append(i)
        self.dfs(n, k, i + 1, current, res)
        current.pop()

        self.dfs(n, k, i + 1, current, res)

        