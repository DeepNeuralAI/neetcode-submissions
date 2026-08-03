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
        
        for j in range(i, n + 1):
            current.append(j)
            self.dfs(n, k, j + 1, current, res)
            current.pop()


        