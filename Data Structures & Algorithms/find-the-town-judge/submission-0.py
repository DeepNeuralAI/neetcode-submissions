class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = [0] * (n + 1)
        outdegrees = [0] * (n + 1)

        for a, b in trust:
            indegrees[b] += 1
            outdegrees[a] += 1
        
        for i in range(1, n + 1):
            if indegrees[i] == n - 1 and outdegrees[i] == 0:
                return i
        return -1
        